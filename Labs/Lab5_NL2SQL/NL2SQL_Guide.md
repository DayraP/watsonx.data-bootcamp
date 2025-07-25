# Natural Language to SQL Agent

**Table of contents**
- [Natural Language to SQL Agent](#natural-language-to-sql-agent)
  - [1. Introduction](#1-introduction)
  - [2.  Prerequisites](#2--prerequisites)
  - [3. Create and Deploy NL2SQL Agent](#3-create-and-deploy-nl2sql-agent)
    - [3.1. Open watsonx.ai Project](#31-open-watsonxai-project)
    - [3.2 Import Jupyter Notebook with the script from local folder](#32-import-jupyter-notebook-with-the-script-from-local-folder)
    - [3.3 Open and run the Jupyter Notebook](#33-open-and-run-the-jupyter-notebook)
  - [4. Integrate agent into watsonx Orchestrate](#4-integrate-agent-into-watsonx-orchestrate)
    - [4.1 Get the endpoint of the agent](#41-get-the-endpoint-of-the-agent)
    - [4.2 Create an agent in orchestrate](#42-create-an-agent-in-orchestrate)
    - [4.3 Deploy Agent](#43-deploy-agent)
    - [4.4 Test Deployed Agent](#44-test-deployed-agent)


## 1. Introduction 
As part of this lab we will create an agent that can convert user Natural Language queries into SQL queries and use the presto engine to query the data and respond back to the user with the answer.  This lab uses the `customers_table` from the postgres_catalog and the `accounts_table` and `holdings table` from the iceberg_data catalog for the data sources.

## 2.  Prerequisites
- Completed  [Environment Setup](env-setup/wealth-mgr-env-setup.md) 
- Completed Labs 1 and 2
  
## 3. Create and Deploy NL2SQL Agent

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
   * Select Local File
   * Click Browse
   * Navigate to and select [NL2SQLAgent_wxai.ipynb](NL2SQLAgent_wxai.ipynb)
    * Append name with your initials: `-name-first3lettersSurname` and click `Create`
  ![add-jn](attachments/2025-07-11_17-31-34.png)

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

### 4.1 Get the endpoint of the agent
1. You should already be in watsonx.ai Studio.  If not:
   * Open `watsonx.ai Studio` from cloud resources:  https://cloud.ibm.com/resources
   * Launch in `IBM watsonx.ai`
2. From the hamburger menu, go to `Deployments`, `View all deployment spaces`
3. Open your deployment space
4. Go to `Assets` tab
5. Click on the AI Service `AI service nl2sql wxdata deploy xxxx` to open the asset.
6. Click on the deployment `AI service nl2sql wxdata deploy xxxx` to find the Endpoints for inferencing
7.  Under Public Endpoint, copy the Agent's endpoint that includes `ai_service_stream` in it as shown below and paste to your text based reference.  You will use this in the next step.
![Agent Endpoint](./attachments/watsonxAI-Agent-Endpoint.png)

### 4.2 Create an agent in orchestrate
1. Open `watsonx orchestrate` from cloud resources:  https://cloud.ibm.com/resources
2. From the hamburger menu, go to `Build`, `Agent Builder`
![alt text](./attachments/AgentBuilder.png)

3. Select `Create Agent +` button 
![alt text](./attachments/CreateAgent-1.png)
   * Select `Create from Scratch`
   * Name agent `NL2SQLAgent <Your Initials>`
   * Under Description enter `This agent helps to answer user's queries by converting natural language questions into SQL.`
   * Select `Create` button to create agent
   ![alt text](./attachments/CreateAgent-2.png)
4.  Configure the agent details.
    * Scroll down to the `Toolset` section on the left hand side
    * Click on `Add agent` under Agents
    ![alt text](./attachments/AddExternalAgent.png)
    * Select `Import` option from the add a new agent popup.
    ![alt text](./attachments/ImportButton.png)
    * Select `External agent` and click `Next`.
    ![alt text](./attachments/ExternalAgent-1.png)
5.  Configure import agent options 
    * Choose `watsonx.ai` as provider since our NL2SQL agent is deployed on the watsonx.ai platform
    * Add your `Cloud API Key` from your text based reference under `API Key`
    * Under `Service instance URL` paste the deployment endpoint you copied earlier
    * Under `Display Name` add `NL2SQLwx-aiAgent-<Your initials>`
    * Under `Description of agent capabilities` add:
    ```
    This agent has access to customer's investment related data.  It converts the user's natural language questions into sql queries to fetch the data from the database and respond to the user.
    ```
    * Select `Import Agent` to integrate the watsonx.ai agent.
  ![alt text](./attachments/ExternalAgent-Fillup.png)

  The imported should now be listed in the agents section.
  ![alt text](./attachments/ExAgent-Iisted.png)

### 4.3 Deploy Agent
1.  In the `Preview` section and enter a greeting to start a chat from the right side chat window.
2.  Enter the question:
```
Who are the clients who have invested in IBM and are holding more than 10000.  Give me just 5 such clients and their respective investment amounts.
```  
3. Click `Deploy` button from the top right corner, and `Deploy` to deploy the agent.

### 4.4 Test Deployed Agent
1. Under the hamburger menu, go to `Chat` and select your deployed agent from the `Agents` drop down 
2. Interact with the Agent by asking different variations of questions
  * `Who are the top 10 clients invested in Amazon and what their holdings are`
  * `Who are the top 3 clients invested in IBM`
  * `List the companies Kevin Wilcox has invested in`
  
  ![alt text](./attachments/Deployed-Agent.png)
1. Evaluate the responses, and reasoning.  
   * Click on `Show Reasoning`, then `Step 1` to see the logic and SQL queries created from natural language
   ![alt text](./attachments/2025-07-11_18-07-03.png)