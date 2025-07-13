## Table of Contents
- [Table of Contents](#table-of-contents)
- [Environment Setup](#environment-setup)
- [Labs](#labs)
  - [Data Warehouse Optimization](#data-warehouse-optimization)
  - [Spark](#spark)
  - [Data Protection Rules (if we can get it to work in toronto)](#data-protection-rules-if-we-can-get-it-to-work-in-toronto)
  - [RAG Agent](#rag-agent)
  - [Natural Language to SQL Agent](#natural-language-to-sql-agent)

## Environment Setup
To run the steps in this hands-on lab portion of the bootcamp, you need access to **watsonx Orchestrate**, **watsonx.data**, and **watsonx.ai** which are provided for you as part of the preparation for this bootcamp.

- Check with your instructor to make sure **all systems** are up and running before you continue.
- Complete the [Environment Setup Guide](env-setup/student-env-setup.md)to setup your environment to run the (4) labs below.  

## Labs

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

