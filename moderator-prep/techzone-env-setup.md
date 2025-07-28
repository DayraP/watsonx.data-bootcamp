# Bootcamp watsonx.data Environment

- [Bootcamp watsonx.data Environment](#bootcamp-watsonxdata-environment)
  - [1. Prerequisities](#1-prerequisities)
    - [1.1 Environments](#11-environments)
    - [1.2 Data Sources](#12-data-sources)
      - [1.2.1 Netezza](#121-netezza)
      - [1.2.2 Postgres SQL](#122-postgres-sql)
  - [2. Setup Overview](#2-setup-overview)
    - [2.1 Provision and setup watsonx.data backend Environment](#21-provision-and-setup-watsonxdata-backend-environment)
    - [2.2 Upload data (binary files and pdfs)](#22-upload-data-binary-files-and-pdfs)
    - [2.3 Prepare handover configurations](#23-prepare-handover-configurations)
    - [2.4 Share the watsonx.data Techzone environment](#24-share-the-watsonxdata-techzone-environment)
    - [2.5 Share access to watsonx.data](#25-share-access-to-watsonxdata)
    - [2.6 :raised\_hands: **Congratulations!!** The backend environment is now ready for labs.](#26-raised_hands-congratulations-the-backend-environment-is-now-ready-for-labs)
  - [3. Client Environment Setup](#3-client-environment-setup)
    - [3.1 Create a workshop reservation for the bootcamp](#31-create-a-workshop-reservation-for-the-bootcamp)
    - [3.2 Share environment information with the Students](#32-share-environment-information-with-the-students)



## 1. Prerequisities
### 1.1 Environments

The bootcamp will use a single shared Techzone environment for the watsonx.data components, shared by all students, to be created by the instructor.  The watsonx.data back-end Techzone environment uses the [watsonx.data ONLY bundle](https://techzone.ibm.com/collection/67d1edfa2aa18c25d43edb04) uses the following services:
- Cloud Object storage
- watsonx.data
- watsonx.data intelligence

The bootcamp also requires individual Techzone environments for each student where they will work in projects and their own watsonx Orchestrate environment.  The [student bundle](https://techzone.ibm.com/collection/client-engineering-agentic-ai-labs/journey-workshop-environments) requires: 
-  watsonx.ai studio
-  watsonx.ai runtime
-  watsonx Orchestrate
-  Cloud Object storage

For instructor self education, you can use just the back-end bundle to test the labs, as the bundle includes watsonx.ai studio, runtime and Orchestrate, but because Orchestrate is a trial service it should not be used for multiple students.


### 1.2 Data Sources
During labs you will work both with structured and unstructured (text data).  
🗃️ Structured data include:
- historic equity transactions for 2019 - 2025 (stored in `Netezza`);
- customer data incl. their personal information and some bank scoring data (will be stored in `Postgres`);
- dumps from other systems in `json/parquet` format that include tax percentage per trading country, accounts/ clients information, and historic data for holdings of different assets for up to 2023.

:exclamation: All of the structured and semi-structured data for this lab were generated and do not correspond to any real equity transactions or bank clients.

📁 Files required for labs execution could be found in `./data` folder:
   - `./data/customers.csv` is a text file with customers data information that will be in later steps uploaded into Postgres.
   - `./data/input_data_hive` - parquet files with the information on accounts, historical holdings and tax liability that will be used in Lab2, they will be linked to hive catalog -> as part of moderator prep you will this directory it at a later step in COS bucket;
      - `tax_liability.json` was created by LLM based on the list of countries and random persentage numbers -> do not correspond to the reality, serve only for educational purposes.
  - `./data/pdfs` contain pdfs with equity market information for Agentic Rag, first you will ingest them from COS bucket during Lab4 -> as part of moderator prep you will upload those files at a later step in COS bucket.

🗄️ Data stores to make available for labs:
   #### 1.2.1 Netezza  
To showcase DWH offload capability you will need Netezza connection with `INVESTMENTS` database that was created and filled with data. Currently we use NPS instance from @Daniel Hancock. There we have a user `STUDENT_01` generated with access limited to `INVESTMENTS` database (SELECT and LIST access for `equity_transactions` and `equity_transactions_ly` schemas).

**Netezza credentials are in the boxnote [here](https://ibm.box.com/s/ic3jx96uck8t1s4gvs3wak3hliesjnuo).**  
Data description in Netezza can be found [here](../Labs/Lab1_Data_Warehouse_Optimization/Data-description.md).
   #### 1.2.2 Postgres SQL  
Postgres SQL customer table will be used to demonstrate federation capabilities of watsonx.data Presto and will be added as a data source.  

-  Currently we have a Postgres SQL instance available in the `watsonx-events` account.  

-  :warning: If the `Postgres xdata bootcamp` service is not available once you provision your bundle, you will need to manually create the service and populate it with data.  

Postgres xdata bootcamp credentials [here](https://ibm.box.com/s/k6iabvkkw4plh711tm2c74bnky3ug34r)<br>
Steps to provision Postgres and populate with data [here](./instructions/Postgres-provisioning.md)


## 2. Setup Overview
The instructor will pre-setup the techzone environment and then share with the bootcamp participants.  All students will use the same the same watsonx.data service instance.

  
### 2.1 Provision and setup watsonx.data backend Environment

1. Request a watsonx.data [environment](https://techzone.ibm.com/my/reservations/create/67e6c2a9bc768d343f1c08ea) in Techzone, that will be shared with all bootcamp participants.  -Select option for  `Demo` with corresponding `opportunity ID`
2. Provision and setup watsonx.data bootcamp Environment**

   There are 2 options:
      - [Half-automatic setup](./instructions/Autosetup-watsonx-environment.md): some parts of the provisioning are automated incl. COS buckets, watsonx.data engines and services using watsonx.data API and COS API, as those APIs change you might need to adjust python script. 
      - [Manual setup](./instructions/UI-watsonx-environment-setup.md): all of the setup is done in UI.

### 2.2 Upload data (binary files and pdfs)

Folder `moderator-prep/data` contains directories with files that are required for the second lab (`files` or `input_data_hive`) and for Lab4 - Rag Agent (`pdfs`).

Upload them to the corresponding COS buckets following [instructions](./instructions/Add-cos-files.md).  
:warning: Make sure files are available at local directory [moderator-prep/data](./data).

### 2.3 Prepare handover configurations

Follow instructions [here](./instructions/wx-ai-env-prep.md)

### 2.4 Share the watsonx.data Techzone environment
   - Invite students to Techzone Env
      - Go to your IBM Techzone, `My reservations` https://techzone.ibm.com/my/reservations
      - Find the reservation you created for the Lab -> `More options` -> `Share`
      ![share-env](attachments/2025-07-15-19-46-59-pasted-vscode.png)
      - There enter emails of users that you will share environment with. 
   Users will receive either an email with invitation to IBM Cloud Account or see a new notification in IBM Cloud. Once they accept this invitation they will be added to the account and a resource group with services in this environment.

   Note:  If users do not receive an invitation, you can manually invite them via IBM Cloud by following instructions in [1.2 Students did not receive techzone invitation ](../Troubleshooting/README.md)
   
### 2.5 Share access to watsonx.data 
In this step, you will grant access to the watsonx.data buckets, catalogs, and engines that you provisioned for the class.  To make this easy, we will be using the techzone admin group for your reservation.  

1.  Find the name of the admin group for the techzone environment
    -  For techzone environments using the `watsonx-events` account, the admin group name matches the `Environment` setting in the techzone reservation
   ![resource-group](./attachments/resource-group.png)
    -  For techzone environments in Toronto, using the `itz-sas-xxx` account, to find the admin name, go to `Manage`, `Access (IAM)`, `Access groups`.  The group name should start with `itz-...`

2. Share access in watsonx.data
     - Go to watsonx.data instance -> Access Control -> Add access
  ![access-control](./attachments/access-control.png)
     - Select all components of watsonx.data by selecting `Items` box
     - Click `Next`
     - Search for / Select the admin group for the techzone environment
     - Click `Next`
     - Choose the role next `Admin` or all components, remember to scroll right to select all engines/sources/services:
       - catalogs: hive_catalog/ iceberg_data / nz_catalog / postgres_catalog (User)
       - source databases: INVESTMENTS_NZ / Postgres (Reader)
       - engines: presto / spark / milvus (User)
       - buckets: hive/ milvus / cos-bucket (Writer)
     - Click `Save`
     - You should receive a notification on the status

### 2.6 :raised_hands: **Congratulations!!** The backend environment is now ready for labs.   

## 3. Client Environment Setup

Instructors will create a Techzone workshop to reserve the individual client environments

Clients will follow [instructions](../env-setup/README.md) to setup their individual environments as part of the bootcamp.

### 3.1 Create a workshop reservation for the bootcamp

The workshop reservation must be made at least **7 days** before your start date. Choose a reservation date 1-2 days before your workshop start date to give yourself time for access, troubleshooting, and setup! 

When creating a workshop reservation, you will need:
- Name & description of workshop
- Number of attendees
- ISC Opportunity code & customer name

Please use any of the six bundles listed in [this collection](https://techzone.ibm.com/collection/client-engineering-agentic-ai-labs/journey-workshop-environments) for your TechZone workshop.

Details on reserving your [workshop environment](https://ibm.ent.box.com/notes/1803626814108)! 
If any of your environments fail to provision, simply contact support through the link on the workshop page. See additional [troubleshooting](troubleshooting.md) tips!

### 3.2 Share environment information with the Students   

1. Assign users to the techzone workshop once it becomes available.
2. Share the information from `Step 2.2` with the students to enable them to complete their [environment setup](../env-setup/README.md):
   -  Text file with credentials and configurations 
   -  presto.json
   -  milvus.json
   -  [Instructions](../env-setup/README.md) to setup their individual environments as part of the bootcamp.
  