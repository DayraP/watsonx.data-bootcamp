# updated to version 3 of watsonx.data API as recieved from Maritta Stephen (translated from sh to python)
import os
import sys
import time
import threading
import logging
import requests
import json
from typing import Optional, Dict, Any

from dotenv import load_dotenv


class WXDProvisioner:
    """Watson X Data provisioning automation class."""
    
    def __init__(self, host_name: str, username: str, apikey: str, crn: str, log_file: str = "provision_wxd.log"):
        self.host_name = host_name
        self.username = username
        self.apikey = apikey
        self.crn = crn
        self.log_file = log_file
        
        # Initialize API endpoints - Updated to v3
        self.base_url = f"https://{self.host_name}/lakehouse/api/v3"
        self.auth_api = f"{self.base_url}/auth/authenticate"
        self.pg_assign_api = f"{self.base_url}/configure/pg_assign"
        self.pg_assign_status_api = f"{self.base_url}/configure/pg_assign"
        self.mds_patch_api = f"{self.base_url}/configuration/mds"
        self.mds_get_api = f"{self.base_url}/configuration/mds"
        self.endpoints_api = f"{self.base_url}/endpoints"
        
        # Token management
        self.token = ""
        self.token_lock = threading.Lock()
        self.stop_event = threading.Event()
        self.token_refresh_interval = 900  # 15 minutes
        
        # Setup logging
        self._setup_logging()
        
    def _setup_logging(self):
        """Configure logging for the provisioner."""
        self.logger = logging.getLogger("wxd_provisioner")
        self.logger.setLevel(logging.INFO)
        
        # Clear existing handlers
        self.logger.handlers.clear()
        
        # Create formatter
        formatter = logging.Formatter("[%(asctime)s] %(message)s")
        
        # File handler
        file_handler = logging.FileHandler(self.log_file)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        
        # Console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)
    
    def _safe_json(self, response: requests.Response) -> Dict[str, Any]:
        """Safely parse JSON response."""
        try:
            return response.json()
        except ValueError:
            return {"raw_text": response.text}
    
    def authenticate(self) -> bool:
        """Authenticate and acquire access token."""
        self.logger.info("Authenticating...")
        payload = {
            "username": self.username,
            "password": self.apikey,
            "instance_id": self.crn,
            "instance_name": ""
        }
        
        try:
            response = requests.post(self.auth_api, json=payload, timeout=30)
        except Exception as e:
            self.logger.error(f"Auth request failed: {e}")
            return False
        
        data = self._safe_json(response)
        # only for debug purposes return the full response
        self.logger.debug(json.dumps(data))
        
        token = data.get("access_token") if isinstance(data, dict) else None
        if not token:
            self.logger.error(f"Authentication failed: {data}")
            return False
        
        with self.token_lock:
            self.token = token
        
        self.logger.info("Authentication successful. Token acquired.")
        return True
    
    def _token_refresher(self):
        """Background token refresh thread."""
        while not self.stop_event.wait(self.token_refresh_interval):
            if not self.authenticate():
                self.logger.error("Token refresh failed. Will retry on next interval.")
    
    def _get_auth_headers(self) -> Dict[str, str]:
        """Get authorization headers with current token."""
        with self.token_lock:
            token = self.token
        return {
            "Authorization": f"Bearer {token}",
            "authinstanceid": self.crn
        }
    
    def pg_assign(self) -> bool:
        """Initiate PG assignment."""
        self.logger.info("Calling PG Assign API...")
        
        while not self.stop_event.is_set():
            try:
                response = requests.post(
                    self.pg_assign_api,
                    headers=self._get_auth_headers(),
                    timeout=30
                )
            except Exception as e:
                self.logger.error(f"PG assign request failed: {e}")
                time.sleep(5)
                continue
            
            data = self._safe_json(response)
            self.logger.info(json.dumps(data))
            
            msg_code = None
            if isinstance(data, dict):
                msg_code = data.get("response", {}).get("message_code")
            
            if msg_code == "Success":
                self.logger.info("PG Assign started.")
                return True
            
            self.logger.info(f"PG Assign failed, retrying... Response: {data}")
            time.sleep(5)
        
        return False
    
    def wait_for_pg_assign(self) -> bool:
        """Wait for PG assignment to complete."""
        self.logger.info("Waiting for PG Assign to complete...")
        
        while not self.stop_event.is_set():
            try:
                response = requests.get(
                    self.pg_assign_status_api,
                    headers=self._get_auth_headers(),
                    timeout=30
                )
            except Exception as e:
                self.logger.error(f"PG assign status request failed: {e}")
                time.sleep(5)
                continue
            
            data = self._safe_json(response)
            self.logger.info(json.dumps(data))
            
            status = None
            if isinstance(data, dict):
                status = data.get("pg_assignresponse", {}).get("pg_assign", {}).get("status")
            
            self.logger.info(f"PG Assign status: {status}")
            if status == "SUCCESS":
                return True
            
            time.sleep(5)
        
        return False
    
    def patch_mds(self) -> bool:
        """Patch MDS configuration."""
        self.logger.info("Patching MDS...")
        payload = {"mds_enabled": True, "is_quickstart": True}
        
        while not self.stop_event.is_set():
            try:
                headers = {**self._get_auth_headers(), "Content-Type": "application/json"}
                response = requests.patch(
                    self.mds_patch_api,
                    headers=headers,
                    json=payload,
                    timeout=30
                )
            except Exception as e:
                self.logger.error(f"MDS patch request failed: {e}")
                time.sleep(5)
                continue
            
            data = self._safe_json(response)
            self.logger.info(json.dumps(data))
            
            errors = []
            status = None
            if isinstance(data, dict):
                errors = data.get("errors") or []
                status = data.get("status")
            
            err_msg = errors[0].get("message") if errors and isinstance(errors[0], dict) else ""
            
            if status == "PROVISIONING":
                self.logger.info("MDS provisioning started.")
                return True
            elif "Metadata service is already in running state" in err_msg:
                self.logger.info("MDS already provisioned. Skipping patch.")
                return True
            
            self.logger.info(f"Retrying MDS patch... Response: {data}")
            time.sleep(5)
        
        return False
    
    def wait_for_mds(self) -> bool:
        """Wait for MDS to be running."""
        self.logger.info("Waiting for MDS to be RUNNING...")
        
        while not self.stop_event.is_set():
            try:
                response = requests.get(
                    self.mds_get_api,
                    headers=self._get_auth_headers(),
                    timeout=30
                )
            except Exception as e:
                self.logger.error(f"MDS status request failed: {e}")
                time.sleep(5)
                continue
            
            data = self._safe_json(response)
            self.logger.info(json.dumps(data))
            
            status = None
            if isinstance(data, dict):
                status = data.get("mds_service", {}).get("status")
            
            self.logger.info(f"MDS service status: {status}")
            if status == "RUNNING":
                return True
            
            time.sleep(30)
        
        return False
    
    def provision_cas_and_cpg(self) -> bool:
        """Provision CAS and CPG services."""
        for service in ("cas", "cpg"):
            url = f"{self.base_url}/{service}/"
            self.logger.info(f"Provisioning {service}...")
            
            while not self.stop_event.is_set():
                try:
                    response = requests.post(
                        url,
                        headers=self._get_auth_headers(),
                        timeout=30
                    )
                except Exception as e:
                    self.logger.error(f"{service} provision request failed: {e}")
                    time.sleep(10)
                    continue
                
                data = self._safe_json(response)
                self.logger.info(json.dumps(data))
                
                msg_code = ""
                err_msg = ""
                if isinstance(data, dict):
                    msg_code = str(data.get("message_code", "")).lower()
                    errs = data.get("errors") or []
                    err_msg = str(errs[0].get("message", "")) if errs and isinstance(errs[0], dict) else ""
                
                if msg_code == "success":
                    self.logger.info(f"{service} provisioning started successfully.")
                    break
                elif "resource already exists" in msg_code or service in err_msg.lower() or "already" in err_msg.lower() or "being provisioned" in err_msg.lower():
                    self.logger.info(f"{service} already provisioned or being provisioned. Skipping...")
                    break
                
                self.logger.info(f"Unexpected {service} response. Retrying... Response: {data}")
                time.sleep(20)
        
        return True
    
    def wait_for_endpoints(self) -> bool:
        """Wait for CAS and CPG endpoints to be running."""
        self.logger.info("Waiting for CAS and CPG endpoints to be RUNNING...")
        
        while not self.stop_event.is_set():
            try:
                response = requests.get(
                    self.endpoints_api,
                    headers=self._get_auth_headers(),
                    timeout=30
                )
            except Exception as e:
                self.logger.error(f"Endpoints request failed: {e}")
                time.sleep(5)
                continue
            
            data = self._safe_json(response)
            self.logger.info(json.dumps(data))
            
            cas_status = None
            cpg_status = None
            if isinstance(data, dict):
                endpoints = data.get("endpoints") or []
                for ep in endpoints:
                    service_type = ep.get("service_type", "").lower()
                    service_status = ep.get("service_status", "").lower()
                    if service_type == "cas":
                        cas_status = service_status
                    elif service_type == "cpg":
                        cpg_status = service_status
            
            self.logger.info(f"CAS: {cas_status}, CPG: {cpg_status}")
            if cas_status == "running" and cpg_status == "running":
                return True
            
            time.sleep(30)
        
        return False
    
    def provision(self) -> bool:
        """Execute the full provisioning workflow."""
        self.logger.info(f"Started processing {self.crn}")
        
        # Initial authentication
        if not self.authenticate():
            return False
        
        # Start token refresh thread
        refresh_thread = threading.Thread(target=self._token_refresher, daemon=True)
        refresh_thread.start()
        
        try:
            # Execute provisioning steps
            steps = [
                ("PG Assign", self.pg_assign),
                ("Wait for PG Assign", self.wait_for_pg_assign),
                ("Patch MDS", self.patch_mds),
                ("Wait for MDS", self.wait_for_mds),
                ("Provision CAS and CPG", self.provision_cas_and_cpg),
                ("Wait for Endpoints", self.wait_for_endpoints)
            ]
            
            for step_name, step_func in steps:
                self.logger.info(f"Executing step: {step_name}")
                if not step_func():
                    self.logger.error(f"Step failed: {step_name}")
                    return False
            
            self.logger.info("WXD provisioning completed successfully!")
            return True
            
        finally:
            self.logger.info("Stopping background token refresh process...")
            self.stop_event.set()
            refresh_thread.join(timeout=5)


def main():
    load_dotenv('instructor-prep/scripts/auto-setup/.env_setup', override=True)
    
    host_name, username, apikey, crn = (
        os.getenv("WXD_INSTANCE_HOST", ""),
        os.getenv("WXD_USERNAME", ""),
        os.getenv("CLOUD_API_KEY", ""),
        os.getenv("WXD_INSTANCE_CRN", "")
    )

    # check that all variables are set
    if not all([host_name, username, apikey, crn]):
        print("Error: One or more required environment variables are not set.")
        sys.exit(1)
    
    provisioner = WXDProvisioner(host_name, username, apikey, crn)
    success = provisioner.provision()
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()