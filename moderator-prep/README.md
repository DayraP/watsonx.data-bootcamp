
# watsonx.data Client bootcamp

- [watsonx.data Client bootcamp](#watsonxdata-client-bootcamp)
  - [1. Prerequisities](#1-prerequisities)
  - [bootcamp parep](#bootcamp-parep)
  - [Overview of the available labs](#overview-of-the-available-labs)
    - [Data Warehouse Optimization](#data-warehouse-optimization)
    - [Spark](#spark)
    - [Data Protection Rules (if we can get it to work in toronto)](#data-protection-rules-if-we-can-get-it-to-work-in-toronto)
    - [RAG Agent](#rag-agent)
    - [Natural Language to SQL Agent](#natural-language-to-sql-agent)
  - [2. Setup Overview](#2-setup-overview)
  - [Optional Pre-work](#optional-pre-work)


The bootcamp will use a shared Techzone environment for all students, to be created by the instructor. 

## 1. Prerequisities
1. TechZone [bundle](https://techzone.ibm.com/my/reservations/create/67e6c2a9bc768d343f1c08ea), which has all the components needed for the hands-on labs, including:

   * watsonx.data
   * Cloud Object Storage (COS)
   * watsonx.data Intelligence (Formerly IKC)
   * watsonx.ai Studio & Runtime
   * watsonx Orchestrate

2. Data Sources and credentials needed for labs -->box link to creds
   1. Netezza 
   2. PostGres SQL

## bootcamp parep

understand the labs, presentations, murals
customize agenda for audience
Share prework if client is new to watsonx.data

## Overview of the available labs

### Data Warehouse Optimization 

Follow instructions in the [Data Warehouse Optimization Guide](Labs/Lab1_Data_Warehouse_Optimization/Lab_1_Data_Offload_Guide.md) to....

### Spark

Follow instructions in the [Data Lakehouse Guide](Labs/Lab2_Data_Lakehouse/Lab2_Data_Lakehouse_Guide.md) to ...

### Data Protection Rules (if we can get it to work in toronto)

Follow instructions in the [Data Governance Guide](<Labs/Lab3_Data_Governance/Lab 3 wdi Data Protection Guide v2.md>) to ...

### RAG Agent

This lab implements an Agentic RAG pipeline using watsonx.data Milvus vector database, and watsonx Orchestrate as the user interface for interacting with the agent. 

Follow the steps in the [Agentic RAG Guide](Labs/Lab4_Agentic_RAG/Agentic_RAG_Guide.md) to create the RAG agent.

### Natural Language to SQL Agent

This lab creates an agent that can convert user Natural Language queries into SQL queries and leveraging the presto engine in watsonx.data, query the data and respond back to the user with the answer.  

Follow instructions in the [Natural Language to SQL Guide](Labs/Lab5_NL2SQL/NL2SQL_Guide.md)to create the NL2SQL Agent.




## 2. Setup Overview

1. [Provision and setup watsonx.data bootcamp Environment](<provision-techzone/1. watsonx-environment-setup.md>)
2. Invite students to Techzone Env (need instructions)
3. Set wxd access control to allow student acccess to storage, engines, catalogs, etc. (need instructions
4. Anything else?)
 
## Optional Pre-work 
In order to maximize the benefits of attending the bootcamp, the attendees should plan to complete the [IBM watsonx.data Technical Essentials Course](https://learn.ibm.com/course/view.php?id=16226) (3 hours).

For users who are new to databases, it is recommended that you complete the following **optional** learning activities as well: 