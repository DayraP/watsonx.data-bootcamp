#  Configuración del Ambiente

- [Configuración del Ambiente](#configuracion-del-ambiente)
  - [1. Primeros Pasos](#1-primeros-pasos)
    - [1.1 Descargar el repositorio del Bootcamp](#11-descargar-el-repositorio-del-bootcamp)
    - [1.2 Acceder al ambiente del bootcamp](#12-acceder-al-ambiente-del-bootcamp)
    - [1.3 Verificar que estás en la instancia correcta](#13-verificar-que-estás-en-la-instancia-correcta)
    - [1.4 Abrir un editor de texto de tu preferencia](#14-abrir-un-editor-de-texto-de-tu-preferencia)
  - [2. Configuración del Ambiente](#2-configuración-del-ambiente)
    - [2.1 Crear una clave de API](#21-crear-una-clave-de-api)
    - [2.2 Crear un nuevo proyecto](#22-crear-un-nuevo-proyecto)
    - [2.3 Asociar una instancia de watsonx.ai Runtime](#23-asociar-una-instancia-de-watsonxai-runtime)
    - [2.4 Crear un token del proyecto](#24-crear-un-token-del-proyecto)
    - [2.5 Crear una clave de API de usuario](#25-crear-una-clave-de-api-de-usuario)
    - [2.6 Crear un espacio de despliegue](#26-crear-un-espacio-de-despliegue)
    - [2.7 Preparar el archivo env.txt](#27-preparar-el-archivo-envtxt)
    - [2.8 Cargar el archivo env.txt en el proyecto de watsonx.ai Studio](#28-cargar-el-archivo-envtxt-en-el-proyecto-de-watsonxai-studio)
  - [3. Crear conexiones a fuentes de datos en el proyecto de watsonx.ai Studio](#3-crear-conexiones-a-fuentes-de-datos-en-el-proyecto-de-watsonxai-studio)
    - [3.1 Agregar conexión Presto](#31-agregar-conexión-presto)
    - [3.2 Agregar conexión Milvus](#32-agregar-conexión-milvus)
    - [3.3 Agregar conexión a COS](#33-agregar-conexión-a-cos)
    - [3.4 Revisar las conexiones en el proyecto](#34-revisar-las-conexiones-en-el-proyecto)



## 1. Primeros Pasos

### 1.1 Descargar los archivos compartidos

- El instructor proporcionará a los estudiantes un archivo ZIP, que incluye los archivos necesarios para el Bootcamp.


### 1.2 Acceder al ambiente del bootcamp

Para completar este bootcamp, necesitarás acceso a los siguientes servicios:

* watsonx.data (Ambiente back-end compartido)
* Cloud Object Storage (COS)
* watsonx.data Intelligence
* watsonx.ai Studio & Runtime
* watsonx Orchestrate
  
Para los laboratorios se requieren dos ambientes de Techzone:  
un ambiente back-end compartido de watsonx.data, utilizado por todos los estudiantes, y un ambiente individual de laboratorios donde realizarás el trabajo práctico.

Para acceder a los ambientes, busca los correos electrónicos enviados por IBM Cloud <no-reply@cloud.ibm.com>, en los que se te invita a unirte a las cuentas donde se encuentran tus ambientes.

En cada correo, haz clic en el enlace `Join` para aceptar la invitación  
(resaltado en la captura de pantalla a continuación).

**Opción:** Si no ves el correo o no lo recibes por algún motivo, puedes encontrar la invitación directamente en tu cuenta de IBM Cloud:  
<https://cloud.ibm.com/notifications?type=account>

<img src="./attachments/image5.png"
style="width:4.96851in;height:2.75537in"
alt="Captura de pantalla de una computadora. El contenido generado por IA puede ser incorrecto." />

*Es posible que hayas trabajado anteriormente con la misma cuenta de Techzone o que ya tengas acceso a ella y puedas verla en la lista de tus cuentas en IBM Cloud. En ese caso, selecciónala y revisa la lista de servicios disponibles para la reserva actual (según el Group ID y el Environment ID en Techzone).*


### 1.3 Verificar que estás en la instancia correcta

Verifica en la esquina superior derecha que te encuentras en la instancia correcta:  
**itz-watsonx-event-xxx**

Si no aparece el nombre correcto de la instancia, puedes seleccionarla desde el menú desplegable.

<font color="red">**PRECAUCIÓN:**</font>  
La instancia que aparece en la esquina superior derecha suele cambiar a tu cuenta personal predeterminada cada vez que navegas o regresas a una nueva página. Por ello, es recomendable verificar la esquina superior derecha **cada vez** que cambies de página.


### 1.4 Abrir un editor de texto de tu preferencia

Abre un editor de texto para usarlo como referencia durante el laboratorio.  
En los laboratorios se indicará cuándo copiar información que será necesaria para pasos posteriores de configuración.

Ejemplos: Bloc de notas en Windows, TextEdit en Mac o un archivo `.txt` en VS Code.
 

## 2. Configuración del Ambiente

### 2.1 Crear una clave de API

Desde la interfaz de IBM Cloud, utiliza el menú superior:

![Manage Access](./attachments/2025-04-23-11-24-04-pasted-vscode.png)

* Manage -> Access IAM  
* En la navegación izquierda, haz clic en **Manage Identities -> API Keys**  
* Haz clic en el botón **Create**  
* Asigna el nombre **lab-api-key** y haz clic en **Create** utilizando los valores predeterminados  
* Copia la clave en tu archivo de referencia de texto (la utilizarás en un paso posterior)  
* Descarga el archivo en tu laptop o computadora de escritorio  

<img src="./attachments/image8.png"
style="width:4.58333in;height:2.125in"
alt="Captura de pantalla de una computadora. El contenido generado por IA puede ser incorrecto." />


### 1. Iniciar sesión en watsonx <a name="log-in-to-watsonx"></a>
---
Ve a `IBM Cloud` -> `Resource list` -> en los recursos de `AI / Machine Learning`, busca la instancia de `watsonx.ai Studio` y haz clic sobre ella -> **Launch in IBM watsonx**

![](./attachments/2025-04-23-17-33-42-pasted-vscode.png)


### 2. Verificar que estás en la cuenta y ubicación correctas <a name="check-instance"></a>
---
Ahora deberías ver la pantalla principal de watsonx. Verifica en la esquina superior derecha que te encuentras en la cuenta y ubicación correctas (especificadas para tu cuenta de laboratorios).  
Si no aparece el nombre correcto de la cuenta, puedes seleccionarlo desde el menú desplegable.

**Nota:**  
La cuenta que aparece en la esquina superior derecha suele cambiar a tu cuenta personal predeterminada cada vez que navegas o regresas a una nueva página. Por ello, es recomendable verificar la esquina superior derecha **cada vez** que cambies de página.

![check-right-instance](./attachments/check-right-instance.png)



### 2.2 Crear un nuevo proyecto<a name="new-project"></a>

1. En la página principal, copia la `URL de watsonx.ai` y guárdala en tu archivo de referencia de texto; la necesitarás para el archivo `env.txt`.

2. Ve a la sección **Projects** en la parte inferior y haz clic en el símbolo **“+”** que aparece junto a ella para crear un nuevo proyecto.

    ![create-new-project](./attachments/2025-07-13_08-30-16.png)

3. Ingresa un **nombre único** para tu proyecto. Incluye tu nombre y apellido, así como cualquier otra información que desees agregar.

    ![unique-name](./attachments/unique-name.png)

    **Cloud Object Storage (COS)**  
    Es probable que ya tengas seleccionada una instancia de Cloud Object Storage, con un nombre que comienza con **“itzcos-...”**.  
    Si es así, **no necesitas realizar ninguna acción adicional**.

    En caso contrario, es posible que se te solicite seleccionar una instancia entre varias opciones.  
    Por favor, consulta con el responsable del bootcamp cuál instancia de COS debes seleccionar.

    ![select-instance](./attachments/select-instance.png)

4. Haz clic en **Create** para crear el proyecto. El proceso puede tardar algunos segundos en completarse.

5. Copia el `Project ID` y guárdalo en tu archivo de referencia de texto; lo necesitarás para tu archivo `env`.

    ![](./attachments/projectid.png)

6. Regresa a la página principal de watsonx.ai Studio.


### 2.3 Asociar una instancia de watsonx.ai Runtime<a name="wml-instance"></a>
---
1. Ve a la pestaña `Manage`.
2. En el panel lateral izquierdo, haz clic en `Services and Integrations`.
3. Haz clic en `Associate service`.

![manage-tab](./attachments/manage-tab.png)

4. Selecciona el servicio que tenga **"Type" = `watsonx.ai Runtime`** y haz clic en **Associate**.

![associate-wml](./attachments/2025-06-25-11-10-43-pasted-vscode.png)

**Nota:**  
Si no encuentras el servicio, elimina todos los filtros de los menús desplegables **“Locations”** y **“Resource Groups”**.  
Si aparecen dos o más servicios de watsonx.ai Runtime, selecciona aquel cuyo **“Group”** coincida con el nombre del *ambiente* de la instancia.  

El nombre del *ambiente* puede encontrarse en:  
https://techzone.ibm.com/my/reservations  

![techzone](./attachments/techzone.png)


### 2.4 Crear un token del proyecto

El token del proyecto será utilizado por el notebook para acceder de forma programática a los activos del proyecto.

1. Ve a la pestaña `Manage`.
2. En la sección `Access Control`, haz clic en la pestaña `Access tokens`.
3. Si no tienes un token, crea uno seleccionando `New access token`.

   ![project_token](./attachments/project_token.png)

4. Asigna un nombre, selecciona `Editor` como `Access Role` y haz clic en `Create`.

   ![project_token](./attachments/access_token.png)


### 2.5 Crear una clave de API de usuario

La clave de API de usuario es un prerrequisito para realizar despliegues remotos exitosos y para acceder a despliegues desde otros servicios (por ejemplo, watsonx Orchestrate).  
Esta clave es diferente de la clave de API de Cloud que creaste previamente.  

Si ya cuentas con una, no necesitas realizar ninguna acción adicional.  
Si no la tienes, sigue los pasos a continuación:

1. Ve a `Profile and settings` del usuario (esquina superior derecha con las iniciales del usuario) y selecciona la pestaña `User API Key`.

   ![profile-settings](./attachments/2025-06-25-11-33-52-pasted-vscode.png)

2. Haz clic en `Create a key +` si aún no tienes una.

### 2.6 Crear un espacio de despliegue
---
1. En el menú hamburguesa de watsonx.ai Studio, ve a `Deployments` -> `New deployment space +`.

   ![Deployment space](./attachments/2025-04-25-16-06-17-pasted-vscode.png)

2. Completa el campo `Name`, selecciona `Development` como **Deployment Stage**, elige el servicio de almacenamiento desde el menú desplegable, así como la instancia de `watsonx.ai Runtime`, y luego haz clic en **Create**.

   ![Create deployment space](./attachments/2025-04-25-16-10-19-pasted-vscode.png)

3. Espera a que el espacio sea creado y luego haz clic en `View new space`.

   ![View new space](./attachments/2025-04-25-16-12-02-pasted-vscode.png)

4. Desde la pestaña `Manage`, copia el `Space GUID` y guárdalo en tu nota de referencia como **Deployment Space ID**.

   ![Deployment space id](./attachments/2025-04-25-16-15-12-pasted-vscode.png)


### 2.7 Preparar el archivo env.txt

1. Actualiza el archivo `env.txt` de la siguiente manera:

    ```
    # Spark Engine ID -> Actualizar con el Engine ID proporcionado por el instructor
    SPARK_ENGINE_ID="spark256"

    # ID de usuario de Cloud -> Actualizar con tu IBMID, normalmente tu correo electrónico
    CLOUD_USER_ID=""

    # Buckets de COS -> Actualizar con los buckets de COS proporcionados por el instructor
    HIVE_BUCKET="hive-1765401354499711144"
    WXD_BUCKET="wxd-1765401354499711842"
    MILVUS_BUCKET="milvus-1765401354499711473"
    INPUT_BUCKET="input-data-1765401354499711902"

    # Catálogos de watsonx.data -> No debería ser necesario cambiarlo, salvo indicación del instructor
    HIVE_CATALOG="hive_catalog"
    ICEBERG_CATALOG="iceberg_data"

    # Esquemas de watsonx.data -> Actualiza los nombres de los esquemas agregando tu nombre
    # y las primeras 3 letras de tu apellido
    SCHEMA_DWH_OFFLOAD="netezza_offload_TuNombre_3PrimerasLetrasDeApellido"
    SCHEMA_DATA_H="input_data_hive_TuNombre_3PrimerasLetrasDeApellido"
    SCHEMA_DATA_I="clients_schema_TuNombre_3PrimerasLetrasDeApellido"

    # Desde watsonx.ai Studio -> Copiar desde tu nota de referencia
    WATSONX_URL="watsonx.ai URL"
    WATSONX_PROJECT_ID="watsonx.ai Project ID"
    WATSONX_DEPLOYMENT_SPACE_ID="Deployment space GUID"

    # Parámetros de ingesta en Milvus -> Actualiza el nombre de la colección agregando
    # tu nombre y las primeras 3 letras de tu apellido
    MV_COLLECTION_NAME="equity_research_TuNombre_3PrimerasLetrasDeApellido"
  
    # Carpeta en COS con archivos PDF de entrada para la ingesta en Milvus
    # No debería ser necesario cambiarla, salvo indicación del instructor
    COS_FOLDER="pdfs"

    # Parámetros para la ingesta en Milvus -> No deberían requerir cambios,
    # salvo indicación del instructor
    SIMILARITY_METRIC="L2"
    SENTENCE_TRANSFORMER="sentence-transformers/all-minilm-l6-v2"
    TEXT_SPLITTER_CHUNK_SIZE=1000
    TEXT_SPLITTER_CHUNK_OVERLAP=200
    TEXT_SPLITTER_SEPARATORS='[" \n", "\n"]'
    TEXT_REPLACEMENTS='{"✔": "ok"}'
    TEXT_SPLITTER_TYPE="RecursiveCharacterTextSplitter" 

### 2.8 Cargar el archivo env.txt en el proyecto de watsonx.ai Studio
:warning: Asegúrate de haber completado **todos** los valores en `env.txt` antes de cargarlo en tu proyecto.

> Este archivo contiene toda la configuración necesaria que se cargará en tu kernel como variables de entorno.

* Ve a tu proyecto en watsonx.ai desde el menú hamburguesa -> `Projects` -> `TuProyecto`
* Ve a la pestaña `Assets`
* Haz clic en el ícono de carga en la esquina superior derecha para subir archivos de datos  
  ![](./attachments/add-asset.png)

* Arrastra y suelta el archivo `env.txt` en el área designada
* Verifica que el archivo aparezca en la lista de activos dentro de la pestaña `Assets`  
  ![view-env.txt](./attachments/2025-06-15-12-39-24-pasted-vscode.png)


## 3. Crear conexiones a fuentes de datos en el proyecto de watsonx.ai Studio

### 3.1 Agregar conexión Presto

Desde el proyecto de watsonx.ai Studio:  
`Assets` -> `New asset +` -> `Connect to a data source` -> buscar `IBM watsonx.data` -> seleccionar `Presto` -> `Next`

![ws-studio-assets](./attachments/2025-06-16-13-36-42-pasted-vscode.png)  
![add-wxdata-connection](./attachments/2025-06-16-13-38-17-pasted-vscode.png)

**Completa los detalles de la conexión:**  
La forma más sencilla es completar los datos de conexión utilizando el fragmento JSON proporcionado por el instructor.

* Selecciona `Enter JSON Snippet`
* Selecciona `Upload File`
* Busca el archivo `presto.json` proporcionado por el instructor y haz clic en `Enter`
 
Deberías ver todos los detalles de la conexión completados, excepto la clave de API, que deberás ingresar manualmente:

* Cambia el nombre de la conexión a (obligatorio): `presto_connection`
* Pega la **Cloud API Key de watsonx.data** proporcionada por el instructor en el campo `API Key`  
  *(no utilices la Cloud API Key del estudiante)*
* Haz clic en `Test connection` (esquina superior derecha) y, una vez que sea exitosa, selecciona `Create` para crear la conexión.
  
**IMPORTANTE:**  
Utiliza la Cloud API Key proporcionada por el instructor, **no** tu propia Cloud API Key, para la conexión Presto.

![test-create-connection](./attachments/2025-06-16-13-55-33-pasted-vscode.png)


### 3.2 Agregar conexión Milvus

Repite los pasos anteriores para crear la conexión a Milvus.

Desde el proyecto de watsonx.ai Studio:  
`Assets` -> `New asset +` -> `Connect to a data source` -> buscar `IBM watsonx.data` -> seleccionar `Milvus`

![ws-studio-assets](./attachments/2025-06-16-13-36-42-pasted-vscode.png)  
![add-wxdata-connection-milvus](./attachments/2025-06-16-13-59-15-pasted-vscode.png)

**Completa los detalles de la conexión:**  
La forma más sencilla es completar los datos de conexión utilizando el fragmento JSON proporcionado por el instructor.

* Selecciona `Enter JSON Snippet`
* Selecciona `Upload File`
* Busca el archivo `milvus.json` proporcionado por el instructor y haz clic en `Enter`

Deberías ver todos los detalles de la conexión completados, excepto el **Username** y el **Password**:

* Cambia el nombre de la conexión a (obligatorio): `milvus_connection`
* Ingresa el **Username** como: `ibmlhapikey_dayra.perez@ibm.com`
* Pega la **Cloud API Key de watsonx.data** proporcionada por el instructor como **Password**  
  *(no utilices la Cloud API Key del estudiante)*
* Haz clic en `Test connection` (esquina superior derecha) y, una vez que sea exitosa, selecciona `Create` para crear la conexión.
  
**IMPORTANTE:**  
Utiliza la Cloud API Key proporcionada por el instructor, **no** tu propia Cloud API Key, para la conexión Milvus.

![test-create-connection-milvus](./attachments/2025-06-16-14-05-31-pasted-vscode.png)

### 3.3 Agregar conexión a COS

Desde el proyecto de watsonx.ai Studio:  
`Assets` -> `New asset +` -> `Connect to a data source` -> buscar `IBM Cloud Object Storage` -> seleccionar `IBM Cloud Object Storage`

![ws-studio-assets](./attachments/2025-06-16-13-36-42-pasted-vscode.png)  
![add-cos-connection](./attachments/2025-06-16-14-34-56-pasted-vscode.png)

Completa los detalles de la conexión:

* Nombre: `cos_connection`
* Deja el campo **Bucket** vacío
* En **Login URL**, utiliza el `COS Bucket Public Endpoint` proporcionado por el instructor **sin** `https://`
* En **Credentials**, selecciona `Resource Instance ID and API Key`
* En **Resource instance ID**, ingresa el `COS CRN` proporcionado por el instructor
* En **API key**, ingresa la `COS API Key` proporcionada por el instructor  
  *(no utilices Cloud API Key)*

  ![](../env-setup/attachments/2025-07-03-20-20-17-pasted-vscode.png)

* Haz clic en `Test connection` (esquina superior derecha) y, una vez que sea exitosa, selecciona `Create` para crear la conexión.

![](../env-setup/attachments/2025-06-26-12-50-46-pasted-vscode.png)


### 3.4 Revisar las conexiones en el proyecto

1. Verifica que tengas **3 conexiones** creadas usando las convenciones de nombres recomendadas  
   (esto es necesario para poder utilizarlas en el código):

   * `cos_connection`
   * `milvus_connection`
   * `presto_connection`

![connections-overview](./attachments/connections-overview.png)

**¡Felicitaciones! Ya estás listo para comenzar con los laboratorios.**

Regresa a [Labs/README.md](../Labs/README.md)
