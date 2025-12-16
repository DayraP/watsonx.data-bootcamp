## Tabla de contenido
- [🥇 Caso de Uso de Wealth Manager](#-caso-de-uso-de-wealth-manager)
  - [🤔 El Problema](#-el-problema)
  - [🎯 Objetivo](#-objetivo)
  - [🏛 Arquitectura](#-arquitectura)
  - [📝 Laboratorios prácticos paso a paso](#-laboratorios-prácticos-paso-a-paso)
    - [Configuración del entorno](#configuración-del-entorno)
    - [Labs](#labs)
      - [1. Data Warehouse Lab](#1-data-warehouse-lab)
      - [2. Data Lakehouse Lab](#2-data-lakehouse-lab)
      - [3. Agentic RAG Lab](#4-agentic-rag-lab)
      - [4. Natural Language to SQL Lab](#5-natural-language-to-sql-lab)


# 🥇 Caso de Uso de Wealth Manager

FinWin Bank es un líder establecido en servicios financieros en EE. UU. con más de 50 años de experiencia ofreciendo un conjunto integral de soluciones, que incluye banca tradicional y en línea, corretaje y wealth management, a través de una amplia red de ubicaciones en todo el país.

Sin embargo, su infraestructura de IT ha crecido de forma orgánica, lo que resultó en un entorno híbrido que abarca data centers on-premises y múltiples proveedores de cloud.

FinWin Bank busca la experiencia en la industria y el liderazgo tecnológico de IBM para proporcionar una solución rentable, fácil de administrar y que minimice las interrupciones a sus sistemas de IT existentes.

## 🤔 El Problema

Los asesores financieros enfrentan desafíos abrumadores cada día: gestionar relaciones con clientes, tomar decisiones complejas, hacer crecer su patrimonio y ofrecer planes personalizados para objetivos futuros, todo mientras navegan manualmente procesos internos y sistemas empresariales. Iniciar sesión manualmente en varias plataformas consume tiempo y es ineficiente.


## 🎯 Objetivo

* Unificar y aprovechar activos de datos empresariales curados, permitiendo que los empleados accedan a los datos correctos en el momento adecuado.
* Facilitar un descubrimiento de datos sencillo, empoderando a los empleados para encontrar información relevante rápidamente.
* Implementar herramientas de IA intuitivas para automatizar tareas repetitivas y mejorar la eficiencia de los asesores financieros.

Al automatizar estas tareas, la empresa busca impulsar la productividad para que sus wealth managers se enfoquen en desarrollar estrategias personalizadas y efectivas que fortalezcan las relaciones con los clientes.


## 🏛 Arquitectura

Para agilizar el proceso de investigación, FinWin se asoció con IBM para diseñar una solución Multi-Agent Wealth Manager que impulsa la productividad de los asesores financieros ayudándolos a priorizar mejor, investigar y prepararse para reuniones con clientes.

Esta solución recibe consultas en lenguaje natural y no requiere que el usuario sea experto en SQL. Los asesores pueden hacer preguntas variadas sobre clientes y mercado y tomar decisiones informadas con acceso sencillo a los datos necesarios de fuentes internas y externas.

Este sistema aprovecha [watsonx Orchestrate](https://www.ibm.com/products/watsonx-orchestrate), el producto no-code/low-code/pro-code de IBM para desarrollar soluciones de IA agentic, [watsonx.data](https://www.ibm.com/products/watsonx-data), el data lakehouse híbrido y abierto de IBM para IA y analítica empresarial, y [watsonx.ai](https://www.ibm.com/products/watsonx-ai), la plataforma de IBM para alojar foundation models como Large Language Models (LLMs).

![Solution Architecture](../attachments/Slide6.png)
 
## 📝 Laboratorios prácticos paso a paso

### Configuración del entorno
Para ejecutar los pasos de esta parte práctica del bootcamp, necesitas acceso a **watsonx Orchestrate**, **watsonx.data** y **watsonx.ai**, los cuales se te proporcionan como parte de la preparación de este bootcamp.

- Consulta con tu instructor para asegurarte de que **todos los sistemas** estén en funcionamiento antes de continuar.
- Completa la [guía de configuración de entorno](../env-setup/README.md) para preparar tu entorno y ejecutar los 4 labs a continuación.  

### Labs
#### 1. [Data Warehouse Lab](Lab1_Data_Warehouse_Optimization/Lab_1_Data_Offload_Guide.md)
#### 2. [Data Lakehouse Lab](Lab2_Data_Lakehouse/Lab2_Data_Lakehouse_Guide.md) 
#### 3. [Agentic RAG Lab](Lab4_Agentic_RAG/Agentic_RAG_Guide.md)
#### 4. [Natural Language to SQL Lab](Lab5_NL2SQL/NL2SQL_Guide.md)
