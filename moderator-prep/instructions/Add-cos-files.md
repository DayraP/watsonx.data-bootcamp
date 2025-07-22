# Add required files to COS

There are 2 options to upload files:

1. Manually upload directories to the corresponding COS buckets using COS UI
2. Run the script with files upload (for more experienced users that know python)

You need to upload data from local `moderator-prep/data` into COS buckets that you've created in the previous step:
- `files` contain csvs and json files with structured data for Lab2 that are transformed and uploaded by the script;
- `pdfs` contain text/ unstructured data on equity research for Lab4;
- `input_data_hive` directory is used in UI manual upload only -> it contains transformed data in case you are not able to run the script and can upload this folder directly in COS hive bucket manually (as a backup)

## 1. Option: Manually upload files

### 1.1 Upload files to COS for Lab 2 
Upload required files into COS hive bucket  

* Open your Cloud Object Storage instance from resource list, under `Storage`:  https://cloud.ibm.com/resources
![select-cos-instance](../attachments/2025-06-15-19-29-18-pasted-vscode.png)
* Go to the bucket that starts with `hive` created during the environment setup
* Inside the bucket, click `Upload` and then click `Upload folders`
![upload-files](../attachments/2025-06-15-20-45-54-pasted-vscode.png)
* Navigate to `moderator-prep/data/input_data_hive` and upload it.  
![select-folder](../attachments/2025-06-15-20-47-46-pasted-vscode.png) 

After upload, you should see the following folder structure in `input_data_hive`:
![hive-bucket-content](../attachments/2025-06-15-20-49-01-pasted-vscode.png)

### 1.2 Upload pdfs for Lab 4
We will begin by uploading the equity research data from the data folder to Cloud Object Storage (COS). Once uploaded, the data will be split, vectorized, and then loaded into Milvus.

* Open your Cloud Object Storage instance from cloud resources, under `Storage`:  https://cloud.ibm.com/resources
<img width="750" alt="api_key" src="../attachments/cos_navigation.png">

* Go to the bucket that starts with `input-data` created during the environment setup
* Inside the bucket, click `Upload` and then click `upload folders`
* Navigate to the classroom Repo, `moderator-prep/data/pdfs` and select `pdfs` and upload it.

<img width="750" alt="api_key" src="../attachments/click_upload.png">

After upload, you should see the files in the bucket.

<img width="750" alt="api_key" src="../attachments/data_upload.png">


## 2 Option: Run the script



### 2.1 Create and activate a virtual environment

> In case you didn't provision Postgres before create a new environment for data preparation first. If you already have virtual env -> you can continue using it.

- Create python venv in the root directory
```sh
# create virtual environment
python3 -m venv venv
```
- Activate python env
```
# On Windows
venv\Scripts\activate
```
```
# On macOS/Linux
source venv/bin/activate
```

### 2.2 Install requirements 
Install requirements for the add_data_postgres Notebook into python environment

```sh
pip install -r ./requirements_data_prep.txt
```

### 2.3 Environment file

> In case you didn't provision Postgres before copy `.env_load` template first.

- Copy the template in the root folder with the name .env_all

```sh
cp "moderator-prep/scripts/data-prep/env_load.example" "moderator-prep/scripts/data-prep/.env_load"
```

- Update env_load with the values for CLOUD_API_KEY and COS from `moderator-prep/scripts/auto-setup/.env_output` if you run `Auto-setup.ipynb` script, if not you can find them manually:
  - Take CLOUD_API_KEY from your reference file (you've used it in auto setup)  
  
  CLOUD_API_KEY = "\<IAM CLOUD API KEY>"

  - From you [IBM Cloud Resource list](https://cloud.ibm.com/resources), go to your COS Instance, and go to the `Service Credentials` tab. Here you should see credentials that you've created during the previous step of environment setup, copy from there `resource_instance_crn`

  COS_INSTANCE_CRN = "\<resource_instance_crn>"

  - Return to the `Buckets` tab and copy location, e.g. for Frankfurt `eu-de`

  COS_BUCKETS_LOCATION = "\<buckets location>"

### 2.4 Run script in Jupyter Notebook

- Open [moderator-prep/scripts/data-prep/add_files_cos.ipynb](../scripts/data-prep/add_files_cos.ipynb) by clicking the link or by navigating to the notebook
- Change the Kernel to venv python before running the notebook
- Run all 

## 3 Return to the instructions

Go back to [techzone-env-setup.md](../techzone-env-setup.md), and continue starting at step `2.3 Prepare handover configurations`