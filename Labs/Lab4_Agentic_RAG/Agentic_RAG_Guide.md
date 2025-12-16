# Agentic RAG Application

- [Agentic RAG Application](#agentic-rag-application)
  - [1. Introducción](#1-introducción)
  - [2.  Prerrequisitos](#2--prerrequisitos)
  - [3. Ingestar datos en Milvus](#3-ingestar-datos-en-milvus)
    - [3.1. Abrir el proyecto watsonx.ai](#31-abrir-el-proyecto-watsonxai)
    - [3.2 Importar el Jupyter Notebook con el script desde la carpeta local](#32-importar-el-jupyter-notebook-con-el-script-desde-la-carpeta-local)
    - [3.3 Abrir y ejecutar el Jupyter Notebook](#33-abrir-y-ejecutar-el-jupyter-notebook)
  - [4. Integrar el agente en watsonx Orchestrate](#4-integrar-el-agente-en-watsonx-orchestrate)
  - [5. Conversar con el agente desplegado](#5-conversar-con-el-agente-desplegado)



## 1. Introducción
Este lab implementa un pipeline de Agentic RAG usando la base de datos vectorial Milvus de watsonx.data y watsonx Orchestrate como la interfaz de usuario para interactuar con el agente. 

La aplicación usa:
- **watsonx.data Milvus**: Para almacenamiento en base de datos vectorial y búsqueda por similitud
- **LangChain**: Para construir el pipeline de RAG
- **LangGraph**: Para orquestar el flujo de trabajo de RAG
 
La aplicación aprovecha datos que el instructor subió al <INPUT_BUCKET> en Cloud Object Storage.

## 2.  Prerrequisitos
- Haber completado la [configuración de ambiente](/env-setup/README.md)
  
  
## 3. Ingestar datos en Milvus

La ingesta se realizará usando la librería de python `langchain` con parámetros personalizables para la carga y división de documentos. 
En la base de datos predeterminada de Milvus crearás una nueva colección correspondiente al `MV_COLLECTION_NAME` predefinido; el esquema de la colección está definido en el código:
![milvus-schema](attachments/2025-07-07-11-43-10-pasted-vscode.png)
Contiene cinco campos:
* `id` que se generará automáticamente;
* `text_embedding` contendrá los vectores de los chunks embebidos;
* `title` del documento;
* `page` donde se ubica el chunk de texto correspondiente;
* `text` chunk completo de texto a embeber.

El modelo de embedding se especifica en la variable de entorno `SENTENCE_TRANSFORMER` y estará disponible desde HuggingFace usando `HuggingFaceEmbeddings` de langchain.

Después de realizar los embeddings de texto, insertamos datos en la colección y creamos el índice para hacer búsquedas vectoriales. Actualmente, los parámetros de la búsqueda vectorial están predefinidos en el código:
![vector-index](attachments/2025-07-07-11-50-27-pasted-vscode.png)

Luego cargamos los vectores en memoria y probamos la búsqueda semántica localmente.
  
### 3.1. Abrir el proyecto watsonx.ai
1. Abre el servicio de watsonx.ai Studio: en la [Cloud Resource list](https://cloud.ibm.com/resources) selecciona los recursos de `AI / Machine Learning` -> servicio `watsonx.ai Studio` -> abrir en `IBM watsonx`
<img src="./attachments/2025-06-15-21-03-23-pasted-vscode.png" alt="alt text" width="75%"><br>
2. Inicia sesión y desde la página de acceso rápido -> `Recent work` selecciona el proyecto que creaste durante la [configuración de ambiente](..//env-setup/README.md).
![get-project-wx-studio](attachments/2025-06-15-21-05-27-pasted-vscode.png)
3. Verifica que puedas ver el archivo env.txt en la lista de todos los assets en la pestaña `Assets`
![view-env.txt](attachments/2025-06-15-12-39-24-pasted-vscode.png)
4. Verifica que las conexiones estén disponibles; las usaremos en el lab
![](attachments/2025-06-16-16-07-01-pasted-vscode.png)

### 3.2 Importar el Jupyter Notebook con el script desde la carpeta local

1. Ve a los Assets del proyecto y selecciona `New asset +`:
  [new-asset](attachments/2025-06-11-13-32-03-pasted-vscode.png)

2. Selecciona el tipo de asset `Work with data and models in Python or R notebooks`
![select-asset](attachments/2025-06-11-13-44-23-pasted-vscode.png)

3. Importa el Jupyter Notebook desde un archivo local:
![browse-jn](attachments/2025-06-11-13-50-39-pasted-vscode.png)

4. Selecciona [1_add_data_milvus_collection_wxai.ipynb](1_add_data_milvus_collection_wxai.ipynb)

5. Agrega al nombre tus iniciales: `-name-first3lettersSurname` y haz clic en `Create`
  ![add-jn](attachments/2025-06-11-17-07-04-pasted-vscode.png)

### 3.3 Abrir y ejecutar el Jupyter Notebook

1. Debería abrirse automáticamente justo después de crearlo; si no, ve a `Your Project` -> `Assets`:
    * haz clic en el Jupyter Notebook
    * y luego haz clic en el lápiz para editar; se abrirá el Jupyter Notebook en modo edición
    ![edit-notebook](attachments/2025-06-15-23-41-37-pasted-vscode.png) 

2. Márcalo como confiable en la esquina superior derecha:
  ![trust-jn](attachments/2025-06-11-14-04-09-pasted-vscode.png)
3. Agrega un Project Token para acceder a los assets del proyecto

     * Haz clic en la segunda celda con imports para activarla
     * Inserta una celda debajo haciendo clic en el signo `+`
    ![](attachments/2025-06-12-16-50-45-pasted-vscode.png)
     * En el menú superior selecciona los 3 puntos para insertar el snippet de project token:
    ![insert-project-token](attachments/2025-06-16-16-17-01-pasted-vscode.png)
     * Ahora debería verse así (el orden es importante):
    ![](attachments/2025-06-16-16-18-26-pasted-vscode.png)
4. Ejecuta todas las celdas consecutivamente comenzando por la instalación de paquetes en la primera celda y revisa las salidas

## 4. Integrar el agente en watsonx Orchestrate

1. Inicia `watsonx Orchestrate` desde cloud resources: https://cloud.ibm.com/resources

   <img width="750" alt="proj_id" src="./attachments/Launch_Orchestrate.png">

2. Desde el menú Hamburguesa en la esquina superior izquierda ve a `Build`, `Agent Builder` 
3. En la pantalla de administración de agentes haz clic en `Create Agent`
   * Elige `Create from Scratch`
   * Nombra el agente, `Equity Research -{your name}`
   * En `Profile`, `Description`, pega el texto siguiente.  
     ```
     An agent to help researching the Equity market based on the past, and current market performance.  This agent will also provide insights into the emerging trends.   By analyzing market research documents details, the agent answers questions about equity market trends.  If the answer to the question is not contained in your knowledge base, instead of responding you should initiate a transfer to the supervisor agent, copying the users query verbatim.
     ```
   * Haz clic en `Create`
   * Selecciona `Choose Knowledge`, `Milvus`, `Next`
   * Add
add host, port, ibmlhapi key and backend cloud api key, next


   * Proporciona las credenciales de conexión a Milvus

     * Para GRPC Host - usa `MILVUS_HOST` de milvus.json
     * Para GRPC Port - usa `MILVUS_PORT` de milvus.json
     * Para Authentication Type - elige `Basic Authentication`
     * Para `Username`, ingresa `ibmlhapikey`
     * Para `Password`, usa la `watsonx.data Cloud API Key` proporcionada por el instructor. (No uses tu propia Cloud API Key)
     * Haz clic en `Next`

   * Proporciona los detalles de configuración de Milvus

     * En `Database`, ingresa `default`
     * En `Collection or Alias`, elige `Collection`
     * En `Collection`, ingresa tu `MV_COLLECTION_NAME` de env.txt, por ejemplo, `equity_research_YourName_First3LettersOfSurname`
     * En `Index` ingresa `text_embedding`
     * En `embedding_model_id`, selecciona `all-minilm-l6-v2`
     * En `Title`, ingresa `title`
     * En `Body`, ingresa `body`
     * Haz clic en `Save`

    * En `Knowledge`, `Description`, pega el texto siguiente.  

     ```
     These  knowledge file had the details of the Equity market and can be used to answer questions to users.   Contains information about market trends and insights for the past and current performance.  If the answer to the question is not contained in your knowledge base, instead of responding you should initiate a transfer to the supervisor agent, copying the users query verbatim.
     ```

     * En la sección `Behavior`, **asegúrate** de que Chat with Documents esté habilitado .<br>
      

1. Despliega el agente haciendo clic en el botón `Deploy` en la esquina superior derecha 
<img width="750" alt="proj_id" src="./attachments/Deploy_Agent.png"><br>

## 5. Conversar con el agente desplegado

  1. Haz clic en el menú Hamburguesa en la esquina superior izquierda y elige Chat
  2. Selecciona el agente con el que quieras conversar, por ejemplo, Equity Research
   <img width="750" alt="proj_id" src="./attachments/Chat_with_Agent.png">

  3. Prueba el agente haciendo preguntas relacionadas con los documentos de Equity Research. Aquí tienes algunas preguntas de ejemplo:<br>

      ```What are the main insights from the equity market in 2024?```<br>
      ```Which commodity has the highest percentage change in 2024?```<br>
      ```What is an ETF?```<br>

  4. Evalúa las respuestas, el razonamiento y las fuentes de los documentos 

      <img width="750" alt="proj_id" src="./attachments/reasoning.png">
      <img width="750" alt="proj_id" src="./attachments/view_sources.png">
