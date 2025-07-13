# Agentic RAG Application

- [Agentic RAG Application](#agentic-rag-application)
  - [1. Introduction](#1-introduction)
  - [2.  Prerequisites](#2--prerequisites)
  - [3. Ingest Data into Milvus](#3-ingest-data-into-milvus)
    - [3.1. Open watsonx.ai Project](#31-open-watsonxai-project)
    - [3.2 Import Jupyter Notebook with the script from local folder](#32-import-jupyter-notebook-with-the-script-from-local-folder)
    - [3.3 Open and run the Jupyter Notebook](#33-open-and-run-the-jupyter-notebook)
  - [4. Integrate agent into watsonx Orchestrate](#4-integrate-agent-into-watsonx-orchestrate)
  - [5. Chat with the deployed Agent](#5-chat-with-the-deployed-agent)



## 1. Introduction
This lab implements an Agentic RAG pipeline using watsonx.data Milvus vector database, and watsonx Orchestrate as the user interface for interacting with the agent. 

The application uses:
- **watsonx.data Milvus**: For vector database storage and similarity search
- **LangChain**: For building the RAG pipeline
- **LangGraph**: For orchestrating the RAG workflow
 
## 2.  Prerequisites
- Completed  [Environment Setup](env-setup/wealth-mgr-env-setup.md)
- env.txt 
- Data uploaded to Milvus bucket in Cloud Object Storage
  
  
## 3. Ingest Data into Milvus

Ingestion will be performed using python `langchain` library with customizable parameters for document loading and splitting. 
In mulvus default database you will create a new collection corresponding to the pre-defined `MV_COLLECTION_NAME`, collection schema is defined in code:
![milvus-schema](attachments/2025-07-07-11-43-10-pasted-vscode.png)
It contains five fields:
* `id` that will be auto-generated;
* `text_embedding` will contain vectors of embedded chunks;
* `title` of the document;
* `page` where corresponding text chunk is located;
* `text` full chunk of text to be embedded.

Embedding model is specified in `SENTENCE_TRANSFORMER` env variable and will be available from HuggingFace using `HuggingFaceEmbeddings` from langchain.

After performing text embeddings, we insert data into collection and create index to perform vector search. Currently, parameters of vector-search are pre-defined in the code:
![vector-index](attachments/2025-07-07-11-50-27-pasted-vscode.png)

Then we load vectors into memory and test semantic search locally.
  
### 3.1. Open watsonx.ai Project
1. Open watsonx.ai Studio Service - From [Cloud Resource list](https://cloud.ibm.com/resources) select `AI / Machine Learning` resources -> `watsonx.ai Studio` service -> open in `IBM watsonx`
<img src="./attachments/2025-06-15-21-03-23-pasted-vscode.png" alt="alt text" width="75%"><br>
2. Login and from the quick access page -> `Recent work` Select the project you created during [Environment Setup](../env-setup/wealth-mgr-env-setup.md).
![get-project-wx-studio](attachments/2025-06-15-21-05-27-pasted-vscode.png)
3. Check that you can see env.txt file in the list of all assets on `Assets` tab
![view-env.txt](attachments/2025-06-15-12-39-24-pasted-vscode.png)
4. Check that Connections are available, we will be using them in the lab
![](attachments/2025-06-16-16-07-01-pasted-vscode.png)

### 3.2 Import Jupyter Notebook with the script from local folder

1. Go to project Assets, select `New asset +`:
  [new-asset](attachments/2025-06-11-13-32-03-pasted-vscode.png)

2. Select `Work with data and models in Python or R notebooks` asset type
![select-asset](attachments/2025-06-11-13-44-23-pasted-vscode.png)

3. Import Jupyter Notebook from local file:
![browse-jn](attachments/2025-06-11-13-50-39-pasted-vscode.png)

4. Select [1_add_data_milvus_collection_wxai.ipynb](1_add_data_milvus_collection_wxai.ipynb)

5. Append name with your initials: `-name-first3lettersSurname` and click `Create`
  ![add-jn](attachments/2025-06-11-17-07-04-pasted-vscode.png)

### 3.3 Open and run the Jupyter Notebook

1. It should open automatically right after creation, if not then from `Your Project` -> `Assets`:
    * click on the Jupyter Notebook
    * and then click on pencil to Edit, it will open Jupyter Notebook in edit mode
    ![edit-notebook](attachments/2025-06-15-23-41-37-pasted-vscode.png) 

2. Trust Jupyter Notebook in the right upper corner:
  ![trust-jn](attachments/2025-06-11-14-04-09-pasted-vscode.png)
3. Add a Project Token to reach assets from the Project

     * Click on the second cell with import so it's active
     * Insert cell below by clicking on `+` sign
    ![](attachments/2025-06-12-16-50-45-pasted-vscode.png)
     * From the upper menu select 3 dots sign to insert a project token snippet:
    ![insert-project-token](attachments/2025-06-16-16-17-01-pasted-vscode.png)
     * So now it should look like this (sequence is important):
    ![](attachments/2025-06-16-16-18-26-pasted-vscode.png)
4. Run all cells consequtively starting from packages installations in the first cell and check outputs

## 4. Integrate agent into watsonx Orchestrate

1. Launch `watsonx Orchestrate` from cloud resources: https://cloud.ibm.com/resources

   <img width="750" alt="proj_id" src="./attachments/Launch_Orchestrate.png">

2. From the Hamburger menu on the top left go to `Build`, `Agent Builder` 
3. From the manage agents screen click `Create Agent`

    <img width="750" alt="proj_id" src="./attachments/Create_New_Agent.png"><br>

   * Choose `Create from Scratch`
   * Name the agent,`Equity Research -{your name}`
   * Under `Profile`, `Description`, paste the text below.  
     ```
     An agent to help researching the Equity market based on the past, and current market performance.  This agent will also provide insights into the emerging trends.   By analyzing market research documents details, the agent answers questions about equity market trends.  If the answer to the question is not contained in your knowledge base, instead of responding you should initiate a transfer to the supervisor agent, copying the users query verbatim.
     ```

   * Under `Knowledge` ,`Description`, paste the text below.  

     ```
     These  knowledge file had the details of the Equity market and can be used to answer questions to users.   Contains information about market trends and insights for the past and current performance.  If the answer to the question is not contained in your knowledge base, instead of responding you should initiate a transfer to the supervisor agent, copying the users query verbatim.
     ```

   * Scroll down to `Documents`, `Content Repository` and select `Connect Content Repository` 

     <img width="750" alt="proj_id" src="./attachments/Choose_Content_Repo.png"><br>

   * Select `Milvus` as the content repository

     <img width="750" alt="proj_id" src="./attachments/Choose_Milvus.png"><br>

   * Provide the Milvus connection credentials

     * For GRPC Host - use `MILVUS_HOST` from .env_all
     * For GRPC Port - use `MILVUS_PORT` from .env_all
     * For Authentication Type - choose `Basic Authentication`
     * For `Username`, enter `ibmlhapikey`
     * For `Password`, use `CLOUD_API_KEY` from .env_all
     * Click `Next`
     
     <img width="750" alt="proj_id" src="./attachments/Milvus_Connection_Details.png"><br>

   * Provide the Milvus Configuration details

     * For `Database`, enter `default`
     * For `Collection`, enter your Collection name from the previous step, example, `your initials_equity_research`
     * For `Index` enter `text_embedding`
     * For `embedding_model_id`, enter `sentence-transformers/all-MiniLM-L6-v2`
     * For `Title`, enter `title`
     * For `Body`, enter `body`
     * Click `Save`
  
     <img width="750" alt="proj_id" src="./attachments/Milvus_Conf_Details.png"><br>
 
      **Ensure** Chat with Documents is enabled under the Behavior section.<br>
      <img width="750" alt="proj_id" src="./attachments/2025-07-11_08-16-25.png"><br>
      

4. Deploy the agent by clicking the `Deploy` button on the top right 
<img width="750" alt="proj_id" src="./attachments/Deploy_Agent.png"><br>

## 5. Chat with the deployed Agent

  1. Click the Hamburger menu on the top left and choose Chat
  2. Select the agent you want the chat with, e.g., Equity Research
   <img width="750" alt="proj_id" src="./attachments/Chat_with_Agent.png">

  3. Test the agent by asking questions related to the Equity Research documents.  Here are some sample questions :<br>

      ```What are the main insights from the equity market in 2024?```<br>
      ```What is an ETF?```<br>
      ```What are the main insights from the equity market in 2024?```<br>

  4. Evaluate the responses, reasoning and document sources 

      <img width="750" alt="proj_id" src="./attachments/reasoning.png">
      <img width="750" alt="proj_id" src="./attachments/view_sources.png">


