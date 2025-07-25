# Content to share with students and wx.ai setup 

## 1. Text file with credentials and configurations

Prepare text file that contains content below needed by students to perform the labs.


```
## Information for the student text reference

# COS information from COS Credentials or autosetup .env_output
COS_API_KEY=""
COS_INSTANCE_CRN=""

# watsonx.data back-end environment Cloud API Key  This key must be provided to students for their project connections to the backend Techzone environment.  
BACK-END_CLOUD_API_KEY=""

#watsonx.data URL to make it easier for students to switch between environments.  Launch watsonx.data and copy URL so students do not have to use resource lists across 2 techzone environments. Example:  https://eu-gb.lakehouse.cloud.ibm.com/#/home?crn=crn:v1:bluemix:public:lakehouse:eu-gb:a/281f7c9c22bd48d18e6eb14ee62fe9e7:990839c8-1d60-4e34-b4c7-e47ada3cf2f2::
WXD_URL=""

#Cloud Object Storage Instance URL to make it easier for students to switch between environments.  Launch COS service and copy URL.  Example:  https://cloud.ibm.com/objectstorage/crn%3Av1%3Abluemix%3Apublic%3Acloud-object-storage%3Aglobal%3Aa%2F281f7c9c22bd48d18e6eb14ee62fe9e7%3Ab4605ef0-0ddf-431b-b276-8a0a03c3f721%3A%3A
COS_INSTANCE_URL=""

## ------content they will use in their env file ----------
# Spark Engine ID  -> Update with Engine ID provided by instructor
SPARK_ENGINE_ID=""

# COS buckets -> Update with COS bucket names provided by instructor
HIVE_BUCKET=""
WXD_BUCKET=""
MILVUS_BUCKET=""
INPUT_BUCKET=""

# watsonx data catalogs -> Should not need to change unless provided by instructor
HIVE_CATALOG="hive_catalog"
ICEBERG_CATALOG="iceberg_data"
```

If you use auto-setup, then you can copy `SPARK_ENGINE_ID` and bucket names from the generated `moderator-prep/scripts/auto-setup/.env_output`.

In case of manual setup, use bucket names from your reference file, and `SPARK_ENGINE_ID` is available in watsonx.data UI -> `Infrastructure Manager` -> click on spark engine -> Details -> `Engine Id`.

## 2.  watsonx.data Engine connection information  

Students will need to create watsonx.ai connections to Milvus and Presto for the labs.  In this step, you will export connection information for each engine in JSON format to make it easy for students to create these connections. 

1. Go to watsonx.data, from IBM Cloud Resource List -> select `watsonx.data` service.
2. Under hamburger menu, go to `Configurations`, `Connection Information`. 
3.  Select Presto Engine and `Export Json`.  Save as `presto.json`
4.  Select Milvus Engine and select `Export Json`.   Save as `milvus.json`


## 3 Return to the instructions

Go back to [techzone-env-setup.md](../techzone-env-setup.md).