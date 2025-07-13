## Table of Contents
- [Table of Contents](#table-of-contents)
- [Environment Setup](#environment-setup)
- [1.  RAG Agent](#1--rag-agent)
- [2.  Web Tools Agent](#2--web-tools-agent)
- [3.  NL2SQL Agent](#3--nl2sql-agent)
- [4.  Supervisor Agent](#4--supervisor-agent)

## Environment Setup
To run the steps in this hands-on lab portion of the bootcamp, you need access to **watsonx Orchestrate**, **watsonx.data**, and **watsonx.ai** which are provided for you as part of the preparation for this bootcamp.

- Check with your instructor to make sure **all systems** are up and running before you continue.
- Complete the [Environment Setup Guide](env-setup/wealth-mgr-env-setup.md) to setup your environment to run the (4) labs below.  

## 1.  RAG Agent
This lab implements an Agentic RAG pipeline using watsonx.data Milvus vector database, and watsonx Orchestrate as the user interface for interacting with the agent. 

Follow the steps in the [Agentic RAG Guide](1_Agentic_RAG/Agentic_RAG_Guide.md) to create the RAG agent.

## 2.  Web Tools Agent
This lab implements a Web search tool using watsonx.ai.  Follow instructions in the [Web Tools Guide](2_Web_Tools/Web_Tools_Guide.md) to create the Web tools agent.

## 3.  NL2SQL Agent

This lab creates an agent that can convert user Natural Language queries into SQL queries and leveraging the presto engine in watsonx.data, query the data and respond back to the user with the answer.  

Follow instructions in the [NL2SQL Agent Guide](3_NL2SQL/NL2SQL_Guide.md) to create the NL2SQL Agent.

## 4.  Supervisor Agent

Help needed to create a functioning Supervisor agent that ties all of this together.