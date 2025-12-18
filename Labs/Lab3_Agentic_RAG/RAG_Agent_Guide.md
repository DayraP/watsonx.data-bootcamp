## Integrar el agente en watsonx Orchestrate

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

  4. Evalúa las respuestas, el razonamiento y las fuentes de los documentos 

      <img width="750" alt="proj_id" src="./attachments/reasoning.png">
      <img width="750" alt="proj_id" src="./attachments/view_sources.png">
