
# watsonx.data Client bootcamp

- [watsonx.data Client bootcamp](#watsonxdata-client-bootcamp)
  - [1. Prerequisities](#1-prerequisities)
    - [1.1 Environment](#11-environment)
    - [1.2 Data](#12-data)
      - [1.2.1 Netezza](#121-netezza)
      - [1.2.2 Postgres SQL](#122-postgres-sql)
  - [2. Overview of the available labs](#2-overview-of-the-available-labs)
    - [Lab1: Data Warehouse Optimization](#lab1-data-warehouse-optimization)
    - [Lab2: Spark](#lab2-spark)
    - [Lab3: Data Protection Rules](#lab3-data-protection-rules)
    - [Lab4: RAG Agent](#lab4-rag-agent)
    - [Lab5: Natural Language to SQL Agent](#lab5-natural-language-to-sql-agent)
  - [3. Setup Overview](#3-setup-overview)
  - [Optional Pre-work](#optional-pre-work)


The bootcamp will use a shared Techzone environment for all students, to be created by the instructor. 

## 1. Prerequisities
### 1.1 Environment
TechZone [bundle](https://techzone.ibm.com/my/reservations/create/67e6c2a9bc768d343f1c08ea), which has all the components needed for the hands-on labs, including:

   * watsonx.data
   * Cloud Object Storage (COS)
   * watsonx.data Intelligence (Formerly IKC)
   * watsonx.ai Studio & Runtime
   * watsonx Orchestrate

At this step you need to request a new environment in Techzone (Demo with corresponding opportunity ID), at later steps you will do pre-setup and share reservation/ services with bootcamp participants.

### 1.2 Data
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

**Netezza credentials are in the boxnote [here](https://ibm.ent.box.com/notes/1873722995947).**  
Data description in Netezza can be found [here](../Labs/Lab1_Data_Warehouse_Optimization/Data-description.md).
   #### 1.2.2 Postgres SQL  
Postgres SQL customer table will be used to demonstrate federation capabilities of watsonx.data Presto and will be added as a data source.  
:warning: Contact @anna.istomina or @jennifer.wales if there is Postgres instance available, if not you will need to follow [the steps](./instructions/Postgres-provisioning.md) to provision and fill it will data.  
**Latest Postgres credential are availble [here](https://ibm.ent.box.com/notes/1873722995947).**


## 2. Overview of the available labs

### Lab1: Data Warehouse Optimization 

[Data Warehouse Optimization Lab](../Labs/Lab1_Data_Warehouse_Optimization/Lab_1_Data_Offload_Guide.md) demonstrates how to reduce the operational cost of running the Data Warehouse environment. In-addition to reducing the operations cost of the Data Warehouse the data will be unified in the Open Hybrid Lakehouse, watsonx.data platform for Analytical and AI applications.

### Lab2: Spark

[Data Lakehouse Lab](../Labs/Lab2_Data_Lakehouse/Lab2_Data_Lakehouse_Guide.md) demonstrates:
- Workflow with hive and iceberg catalogs to handle different workflows.
- Support for data federation so that data can be consumed from the source rather than making additional copies. 
- Using the fit for purpose engine (Spark) to Transform, aggregate and cleanse the data in-order to expose high quality data for Analytical and AI applications.

### Lab3: Data Protection Rules
*Currently limited to demo*

Follow instructions in the [Data Governance Guide](../Labs/Lab3_Data_Governance/Lab%203%20wdi%20Data%20Protection%20Guide%20v2.md) aims at showing watsonx.data capabilities to integrate with Knowledge Catalog to explore your data, establish efficient access to data and protect sensitive data.

### Lab4: RAG Agent

This lab implements an Agentic RAG pipeline using watsonx.data Milvus vector database, and watsonx Orchestrate as the user interface for interacting with the agent. 

Follow the steps in the [Agentic RAG Guide](../Labs/Lab4_Agentic_RAG/Agentic_RAG_Guide.md) to create the RAG agent.

### Lab5: Natural Language to SQL Agent

This lab creates an agent that can convert user Natural Language queries into SQL queries and leveraging the presto engine in watsonx.data, query the data and respond back to the user with the answer.  

Follow instructions in the [Natural Language to SQL Guide](../Labs/Lab5_NL2SQL/NL2SQL_Guide.md)to create the NL2SQL Agent.


## 3. Setup Overview
You will pre-setup environment that you will later share with the bootcamp participants: you will be using the same account and services' instances.
1. Provision and setup watsonx.data bootcamp Environment  
There are 2 options:
   - [Half-automatic setup](./instructions/Autosetup-watsonx-environment.md): some parts of the provisioning are automated incl. COS buckets, watsonx.data engines and services using watsonx.data API and COS API, as those APIs change you might need to adjust python script. 
   - [Manual setup](./instructions/UI-watsonx-environment-setup.md): all of the setup is done in UI.
2. Upload data (binary files and pdfs)  
Folder `moderator-prep/data` contains directories with files that are required for the second lab (`files` or `input_data_hive`) and for Lab4 - Rag Agent (`pdfs`). 
You will upload them to the corresponding COS buckets following [instructions](./instructions/Add-cos-files.md).  
:warning: Make sure files are available at local directory [moderator-prep/data](./data).
3. Prepare handover configurations and setup watsonx.ai connections ->
Follow instructions [here](./instructions/wx-ai-env-prep.md)
4. Share your Techzone environment and watsonx.data access:
   - Invite students to Techzone Env
      - Go to your IBM Techzone, `My reservations` https://techzone.ibm.com/my/reservations
      - Find the reservation you created for the Lab -> `More options` -> `Share`
      ![share-env](attachments/2025-07-15-19-46-59-pasted-vscode.png)
      - There enter emails of users that you will share environment with.  
   Users will recieve either an email with invitation to IBM Cloud Account or see a new notification in IBM Cloud. Once they accept this invitation they will be added to the account and a resource group with services in this environment.
   - Find your resource group so you can share acess to it
     - In your Techzone reservations click on the right Techzone reservation and copy `Environment`, that is your resource group -> the same one your should see in IBM Cloud Resource List / Groups
  ![resource-group](./attachments/resource-group.png)
   - Share access in watsonx.data
     - Go to watsonx.data instance -> Access Control -> Add access
  ![access-control](./attachments/access-control.png)
     - There select all component of watsonx.data with Items box
     - Click Next
     - There search for a resource group corresponding to your account and select it -> Next
     - Choose `Admin` roles for all components, remember to scroll left to select all engines/sources/services
     - Save
   - Share connections in watsonx.ai
     - Go to watsonx.ai -> In Hamburger menu select `Data/ Connectivity`
     - Go to `Access control` tab -> Add collaborators -> Add user group
  ![connectivity-access](./attachments/wxai-connectivity-access.png)
     - There select search for your resource group
     - Select Editor access and click Add
  ![editor-access-connections](./attachments/editor-access-connections.png)


 
## Optional Pre-work 
In order to maximize the benefits of attending the bootcamp, the attendees should plan to complete the [IBM watsonx.data Technical Essentials Course](https://learn.ibm.com/course/view.php?id=16226) (3 hours).

For users who are new to databases, it is recommended that you complete the following **optional** learning activities as well.