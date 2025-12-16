
# watsonx.data intelligence 

- [watsonx.data intelligence](#watsonxdata-intelligence)
  - [1. Introducción](#1-introducción)
  - [2. Prerrequisitos:](#2-prerrequisitos)
  - [3. Configurar la integración servicio a servicio](#3-configurar-la-integración-servicio-a-servicio)
  - [4. Crear catálogo en watsonx.data Intelligence](#4-crear-catálogo-en-watsonxdata-intelligence)
  - [5. Curación de datos](#5-curación-de-datos)
    - [5.1 Abrir el servicio watsonx.data Intelligence](#51-abrir-el-servicio-watsonxdata-intelligence)
    - [5.2. Crear un proyecto](#52-crear-un-proyecto)
  - [6. Agregar una conexión a la fuente de datos de watsonx.data](#6-agregar-una-conexión-a-la-fuente-de-datos-de-watsonxdata)
    - [6.1 Copiar información de conexión de watsonx.data](#61-copiar-información-de-conexión-de-watsonxdata)
    - [6.2 Abrir el Bootcamp Catalog](#62-abrir-el-bootcamp-catalog)
    - [6.3 Agregar una conexión a tu instancia de watsonx.data](#63-agregar-una-conexión-a-tu-instancia-de-watsonxdata)
  - [7. Agregar el asset conectado de watsonx.data al catálogo de watsonx.data Intelligence](#7-agregar-el-asset-conectado-de-watsonxdata-al-catálogo-de-watsonxdata-intelligence)
  - [8. Navegar el asset importado](#8-navegar-el-asset-importado)
  - [9. Generar perfil de datos para el asset importado](#9-generar-perfil-de-datos-para-el-asset-importado)
  - [10. Enriquecer datos para el asset importado](#10-enriquecer-datos-para-el-asset-importado)
    - [10.1 Configurar opciones de enriquecimiento](#101-configurar-opciones-de-enriquecimiento)
    - [10.2 Crear un job de Metadata Enrichment](#102-crear-un-job-de-metadata-enrichment)
    - [10.3  Revisar resultados de enriquecimiento](#103--revisar-resultados-de-enriquecimiento)
    - [10.4  Agregar los datos enriquecidos de vuelta al catálogo](#104--agregar-los-datos-enriquecidos-de-vuelta-al-catálogo)
  - [11. Crear regla de protección de datos en Cloud Pak for Data](#11-crear-regla-de-protección-de-datos-en-cloud-pak-for-data)
  - [12. Agregar integración de servicio en watsonx.data hacia watsonx.data Intelligence](#12-agregar-integración-de-servicio-en-watsonxdata-hacia-watsonxdata-intelligence)
  - [13. Agregar acceso restringido de usuario a watsonx.data](#13-agregar-acceso-restringido-de-usuario-a-watsonxdata)
    - [13.1 Agregar acceso a componentes de infraestructura](#131-agregar-acceso-a-componentes-de-infraestructura)
    - [13.2 Agregar política a datos iceberg](#132-agregar-política-a-datos-iceberg)
  - [14 Verificar que la regla de protección de datos se está aplicando (demostración)](#14-verificar-que-la-regla-de-protección-de-datos-se-está-aplicando-demostración)

## 1. Introducción

Lab 3 te guiará por los pasos de alto nivel a continuación para demostrar cómo implementar la aplicación de reglas de protección de datos en watsonx.data.

Como estamos trabajando en un entorno compartido de watsonx.data intelligence (wxi), algunos pasos se completaron de antemano (los pasos en azul oscuro).  

<img src="./attachments/image1.png" alt="alt text" width="75%">


## 2. Prerrequisitos:
- Haber completado la [configuración de ambiente](/env-setup/README.md)
- El instructor preparó el Bootcamp Catalog, importó el glosario de negocio y creó las reglas de protección de datos.
 
 
## 3. Configurar la integración servicio a servicio

[Documentation link](https://dataplatform.cloud.ibm.com/docs/content/wsj/governance/wkc-wxd-integration.html?context=cpdaas&locale=en&audience=wdp)


Antes de comenzar a trabajar con reglas de protección de datos en los assets de watsonx.data, debes autorizar a los servicios `watsonx.data` y `watsonx.data intelligence` para que se accedan entre sí. Para facilitar el uso, estas autorizaciones para el bootcamp ya están preconfiguradas.

* Para verificar, en IBM Cloud ve a `Manage` -> `Access IAM`, luego en el menú izquierdo `Authorizations`.
![](./attachments/2025-04-24-12-09-12-pasted-vscode.png)

  Deberías encontrar autorizaciones similares a las siguientes con tu instancia de techzone

  <img src="./attachments/image4.png" alt="alt text" width="100%">

  <img src="./attachments/image5.png" alt="alt text" width="100%">


## 4. Crear catálogo en watsonx.data Intelligence

El catálogo es el lugar donde pondremos las conexiones de watsonx.data y los assets de datos a disposición de los usuarios de negocio.  

Al crear un catálogo es necesario habilitar la opción `Enforce data protection and data location rules` si se usarán reglas de protección de datos entre los dos servicios 

<img src="./attachments/image6.png" alt="alt text" width="100%"><br>


Para el bootcamp, el catálogo ya fue creado para ti y será compartido por todos los estudiantes. Por esta razón, es importante que las conexiones y los assets que agreguemos en el lab tengan nombres únicos.  

Lo haremos anteponiendo `FirstInitial+Lastname` para el contenido que agreguemos al catálogo.

## 5. Curación de datos

Nota: el proceso de curación de datos también usará un proyecto como en el Lab 2; sin embargo, este proyecto se creará dentro del servicio watsonx.data Intelligence en lugar de watsonx.ai Studio para aprovechar las capacidades de data fabric del servicio.

### 5.1 Abrir el servicio watsonx.data Intelligence

* Desde IBM Cloud `Resource List` <https://cloud.ibm.com/resources>

* Selecciona watsonx.data Intelligence para tu región (en AI/ Machine Learning) en `IBM Cloud Pak for Data`
  
  <img src="./attachments/ikc-resources.png" alt="alt text" width="75%">

* Inicia el servicio
  
  <img src="./attachments/intelligence.png" alt="alt text" width="75%">

* Haz clic en `Cancel` si aparece la ventana de inicio


### 5.2. Crear un proyecto 

* Desde el menú Hamburguesa, selecciona `Projects`, `View all Projects`

* Selecciona `New Project`
* Nombre:  `Lab 3 Data Protection`
* Selecciona tu Cloud Object Storage de la lista
* Selecciona `Create`


## 6. Agregar una conexión a la fuente de datos de watsonx.data
### 6.1 Copiar información de conexión de watsonx.data 

* Desde IBM Cloud `Resource list` <https://cloud.ibm.com/resources>

* Inicia `watsonx.data` (en `Databases`) en una nueva ventana

* Desde el menú Hamburguesa, selecciona `Configurations`, `Connection information`

  <img src="./attachments/image2.png" alt="alt text" width="25%">

* En Engine and service connection details

* Selecciona tu motor presto

* `Copy JSON snippet` (al portapapeles)

  <img src="./attachments/image3.png" alt="alt text" width="75%"> <br>

* Pega en tu nota de referencia (lo usarás en el siguiente paso)

### 6.2 Abrir el Bootcamp Catalog

* Regresa al servicio `watsonx.data Intelligence`.  
  
* Desde el menú Hamburguesa, selecciona `Catalogs`, `View all Catalogs`
  
* Selecciona el `Bootcamp Catalog`
  
### 6.3 Agregar una conexión a tu instancia de watsonx.data
  
* Selecciona `Add to Catalog`, `Connection` en la esquina derecha

* Busca y selecciona `IBM watsonx.data` en el conjunto de conectores de la izquierda

* Selecciona `IBM watsonx.data Presto` y haz clic en Next

  <img src="./attachments/image8.png" alt="alt text" width="60%"> 

* Selecciona `Enter JSON snippet`

* Pega la información de conexión de watsonx.data desde tu nota de referencia (que copiaste antes desde watsonx.data Presto) y selecciona `Enter`

  <img src="./attachments/image9.png" alt="alt text" width="75%">

* En Name, antepone tu **FirstInitialLastName**, por ejemplo `Jwales Presto`
* Desplázate hacia abajo y pega tu `cloud-api-key` (creada durante la configuración del ambiente)

* Haz clic en `Test connection` (esquina superior derecha)

* Cuando la prueba sea exitosa, selecciona Create

  <img src="./attachments/image10.png" alt="alt text" width="75%">

##  7. Agregar el asset conectado de watsonx.data al catálogo de watsonx.data Intelligence

* Desde la esquina izquierda selecciona `Add to catalog`, `Connected Asset`

  <img src="./attachments/image11.png" alt="alt text" width="25%">

* Haz clic en `Select Source`

  <img src="./attachments/image12.png" alt="alt text" width="50%">

* En las `Connections` disponibles, selecciona [tu conexión Presto], selecciona `postgres_catalog`, selecciona el esquema `bankdemo` y finalmente la `customers_table` y haz clic en `Select`

  <img src="./attachments/customertable.png" alt="alt text" width="75%"><br>

* En la ventana `Add asset from connection`, antepone tu nombre al nombre de la tabla, por ejemplo: **jwales-customers-table**.  
* Deja el resto de los campos con los valores predeterminados y haz clic en `Add`
  <img src="./attachments/addasset.png" alt="alt text" width="75%"><br>


* Deberías ver tu conexión y asset de datos en `Recently added` Assets

  <img src="./attachments/image14.png" alt="alt text" width="25%"><br>

##  8. Navegar el asset importado

* Selecciona el Data Asset que acabas de importar
  
* Observa que la tabla no tiene calidad de datos, términos de negocio ni clasificaciones.
  <img src="./attachments/nometadata.png" alt="alt text" width="75%"><br>

* Selecciona la pestaña `Assets` y previsualiza la información de las columnas
* Aquí vemos SSN y direcciones de correo electrónico que queremos proteger.
   <img src="./attachments/protectcolumns.png" alt="alt text" width="75%"><br>


##  9. Generar perfil de datos para el asset importado

El profiling en watsonx.data intelligence consiste en analizar las columnas de los assets de datos para entender su estructura y contenido. Este análisis incluye calcular estadísticas sobre los datos, determinar tipos y formatos, clasificar los datos y capturar distribuciones de frecuencia. 

* Selecciona la pestaña `Profile` para iniciar el profiling (toma de 5 a 10 minutos)

  <img src="./attachments/image16.png" alt="alt text" width="75%"><br>

* Al finalizar, selecciona la opción `Add to project` 

  <img src="./attachments/addtoproject.png" alt="alt text" width="75%"><br>

* En la ventana `Add to project`, selecciona `I Understand`, 
* Selecciona el proyecto que creaste en el paso 3  
* `Next` y luego `Add`

  <img src="./attachments/addtoproject1.png" alt="alt text" width="75%"><br>

**Nota**: el método preferido para enriquecer un asset de datos sería trabajar directamente en el proyecto, realizando un Metadata Import (MDI) seguido de un Metadata Enrichment (MDE), y luego agregarlo al catálogo. Debido a un bug con el profiling después de importar con MDI, estamos tomando el paso adicional de perfilar primero en el catálogo. Esto es una solución temporal hasta que se resuelva el problema. 


##  10. Enriquecer datos para el asset importado

Este paso usa la herramienta automatizada de Metadata Enrichment para enriquecer el asset de watsonx.data que acabas de importar a través del catálogo.

El metadata enrichment utiliza data classes definidas y términos de negocio para asignar o sugerir automáticamente durante el proceso de enriquecimiento. Esto ahorra a las organizaciones una gran cantidad de tiempo y recursos al reducir el esfuerzo manual necesario para lograr el mismo resultado.

### 10.1 Configurar opciones de enriquecimiento

* Ve a tu proyecto seleccionando el menú Hamburguesa, `Projects`, `View all Projects`, `Lab 3 Data Protection` 

  Deberías ver 2 assets importados: tu conexión a watsonx.data y la tabla importada.

  <img src="./attachments/importedtoproject.png" alt="alt text" width="75%"><br>
  
* Configura las opciones de enriquecimiento seleccionando `Manage`, `Metadata enrichment`, y desplázate hacia abajo hasta los métodos de asignación de términos y selecciona: 
  
  * Machine learning (se usa un modelo de machine learning para asignar términos).
  * Data-class-based assignments (los términos se asignan según la data class de la columna).
  * Name matching (los términos se asignan según la similitud entre un término y el nombre del asset o columna).
  
  <img src="./attachments/enrichmentoptions.png" alt="alt text" width="75%"><br>

    La asignación de términos basada en Gen AI (Semantic Enrichment) es una opción disponible en un servicio SaaS con licencia de prueba o Premium. Con esta opción, se asignan y sugieren términos de negocio específicos del dominio usando el modelo slate.30m.semantic-automation.c2c. El modelo toma en cuenta nombres y descripciones de assets y columnas, y hace coincidir semánticamente términos con ese metadata, asignándolos incluso si no son coincidencias exactas.  

    Para el lab estamos usando una licencia essentials, por lo que Gen AI no se utilizará. 

### 10.2 Crear un job de Metadata Enrichment

* Cambia a la pestaña `Assets`
* Selecciona `New Asset`
* Selecciona `Enrich data assets with metadata`
* Ingresa el nombre:  `MDE` y selecciona `Next`
* Selecciona `Select data from project` 
* En Asset types, selecciona `Data asset`, y `Your Table Name` y `Select`
   <img src="./attachments/selectdataasset.png" alt="alt text" width="75%"><br>
* Tu asset debería estar seleccionado. Selecciona `Next`
* Configura los objetivos de enriquecimiento habilitando las siguientes opciones:
  * Profile Data
  * Assign terms and classifications
  * Run basic quality analysis  
  <img src="./attachments/objectives.png" alt="alt text" width="75%"><br>
  * Desplázate hacia abajo, selecciona `Select categories + `
  * Selecciona [uncategorized] y `Customer` y `Select`
  <img src="./attachments/selectcategories.png" alt="alt text" width="75%"><br>
* Mantén los valores predeterminados para Sampling y Schedule enrichment Job y haz clic en `Next`
  <img src="./attachments/sampling.png" alt="alt text" width="75%"><br>
* Mantén los valores predeterminados para ejecutar el job ahora y haz clic en `Next`
 <img src="./attachments/schedulejob.png" alt="alt text" width="75%"><br>
* Se mostrarán las opciones de enriquecimiento. Selecciona `Create` para iniciar el job
  <img src="./attachments/confirmenrich.png" alt="alt text" width="75%"><br>


El Data Scope analizará un asset de datos importado desde watsonx.data con el objetivo de perfilar los datos, analizar su calidad y asignar términos en 2 categorías usando el método de muestreo Basic.

El proceso de enriquecimiento tomará aproximadamente 2-3 minutos. <br>El estado cambiará de `Not analyzed` a `In progress` y luego a `Finished`.

### 10.3  Revisar resultados de enriquecimiento  

Según el alcance y los objetivos, la herramienta de Metadata Enrichment perfiló automáticamente los datos, analizó y evaluó la calidad, asignó y sugirió términos de negocio, y asignó data classes a todas las columnas para los assets incluidos en el job.

Como data steward, ahora revisarás el enriquecimiento propuesto antes de publicarlo en el catálogo para que otros lo consuman.


* Selecciona el botón `Refresh` para mostrar el metadata enrichment o navega hasta él: selecciona el `Project-Name`, selecciona la pestaña `Assets` y selecciona `MDE`

* Ve a la pestaña Columns
  
  <img src="./attachments/refresh.png" alt="alt text" width="75%"><br>


¡La tabla ahora tiene metadata! <br>
<img src="./attachments/metadata.png" alt="alt text" width="75%"><br>

Cuando watsonx.data intelligence alcanzó los umbrales de confianza, asignó automáticamente términos de negocio, data classes y clasificaciones.   

Cuando el modelo no cumple el umbral de enriquecimiento definido, hará una sugerencia (en morado). Veamos:

 <img src="./attachments/suggestion.png" alt="alt text" width="75%"><br>


* Haz clic en la burbuja morada `1 suggested` junto a `risk_score`, luego selecciona la pestaña `Governance` en el lado derecho y revisa la sugerencia.
* Selecciona el botón `Assign` para aceptar la sugerencia.
<img src="./attachments/risk-score.png" alt="alt text" width="75%"><br>

En el caso de que haya ambigüedad en el término de negocio, el modelo puede no hacer una sugerencia. 

* Pasa el cursor sobre la columna de business term para `Address` y selecciona `View more`  
* Selecciona la pestaña `Governance` en el lado derecho y selecciona el botón `+`
<img src="./attachments/address.png" alt="alt text" width="75%"><br>
* En la barra de búsqueda, escribe `address`
* Selecciona `Work Address` y `Assign`
<img src="./attachments/assignworkaddr.png" alt="alt text" width="75%"><br>

Tómate un momento para explorar los atributos de metadata `Data Class` y `Classifications` que se asignaron o sugirieron. 

Un data steward continuaría asignando valores para todas las columnas, pero en aras del tiempo nos concentraremos en lo necesario para proteger los datos en las columnas `SSN` y `Email Address`.

**Verificar Data Classes** 

Las reglas de protección de datos requieren criterios para que la regla se active y pueden incluir atributos de usuario y propiedades del asset de datos.  <br>
Para nuestro lab, usaremos el atributo `Data class` para clasificar el contenido en las columnas a proteger. 

* En la fila `SSN`, revisa la `Data Class` asignada y establécela en `US Social Security Number` si no se asignó automáticamente. 
* Opcionalmente revisa las `Classifications` y configúralas en `Sensitive Personal Information`.

<img src="./attachments/dataclasses.png" alt="alt text" width="100%"><br>
  
* En la fila `email`, revisa la `Data Class` asignada y establécela en `Email Address` si no se asignó automáticamente. 
* Opcionalmente revisa las `Classifications` y configúralas en `Personally Identifiable Information`.  

Cuando estés satisfecho con que tus datos estén correctamente identificados y listos para ser gobernados, puedes agregar la versión enriquecida de vuelta al catálogo.

### 10.4  Agregar los datos enriquecidos de vuelta al catálogo

* Navega de regreso a la vista del asset haciendo clic en la pestaña Asset

  <img src="./attachments/returntoasset.png" alt="alt text" width="25%"><br>
* Selecciona la casilla junto al Data asset y haz clic en `Publish` en la barra azul
  <img src="./attachments/publish.png" alt="alt text" width="75%"><br>
* Selecciona el `Bootcamp Catalog` y selecciona `Next`
  <img src="./attachments/publish2.png" alt="alt text" width="75%"><br>
* En la página Review Assets, selecciona `Publish`  
* Esto tomará unos minutos y, al finalizar, verás un mensaje `Request to publish assets completed`
  
Antes

   <img src="./attachments/nometadata.png" alt="alt text" width="75%"><br>

Después
  
  <img src="./attachments/after2.png" alt="alt text" width="75%"><br>

## 11. Crear regla de protección de datos en Cloud Pak for Data 

Ahora que los datos han sido curados, es momento de aplicar reglas de protección. Para nuestro caso de uso, queremos proteger los números de Social Security y las direcciones de correo electrónico para que no sean visibles en el catálogo.  

Como trabajamos en un entorno compartido de watsonx.data Intelligence, este paso ya se realizó por ti. Veamos las reglas configuradas.

* Ve a tu instancia de `watsonx.data Intelligence`

* Desde el menú Hamburguesa, selecciona `Governance`, `Rules`

  1. Previsualiza las reglas Protect US SSN y Email

      Para el lab, elegimos enmascarar el SSN con el carácter X, y para el Email sustituiremos datos, aunque también podríamos haber optado por ofuscar o denegar el acceso.

      <img src="./attachments/protectssn.png" alt="alt text" width="75%"><br>
       
     <img src="./attachments/protect-email.png" alt="alt text" width="75%"><br>


##  12. Agregar integración de servicio en watsonx.data hacia watsonx.data Intelligence

* Ve a la instancia del servicio `watsonx.data`

* Desde el menú Hamburguesa, selecciona `Access Control`

* Selecciona la pestaña `Integrations`<br>
  <img src="./attachments/integrations.png" alt="alt text" width="75%"><br>

* Haz clic en el botón `Integrate service +`

* Selecciona `IBM Knowledge Catalog`

* En `Storage catalogs`, selecciona todos los catálogos

* Agrega el endpoint de watsonx.data Intelligence para tu catálogo anteponiendo api a tu host: <br>
    https://api.dataplatform.cloud.ibm.com (para SaaS Dallas)<br>
    https://api.eu-gb.dataplatform.cloud.ibm.com (para London)

* Haz clic en `Integrate`

* :exclamation:Nota: el servicio no se activará de forma predeterminada.


* Haz clic en los 3 puntos a la derecha de la integración de servicio y selecciona `Activate`

  <img src="./attachments/integrate.png" alt="alt text" width="75%"><br>

* Haz clic en `Confirm` cuando se solicite

* La integración reiniciará el motor presto.

  <img src="./attachments/integratecomplete.png" alt="alt text" width="75%"><br>

## 13. Agregar acceso restringido de usuario a watsonx.data

Las reglas de protección de datos se aplican a usuarios que no son administradores del recurso de datos. Para el lab, nuestros usuarios de negocio pertenecerán al grupo de usuarios `Data_Scientist`.  

  
### 13.1 Agregar acceso a componentes de infraestructura

* Desde el menú Hamburguesa, selecciona `Access control` en `watsonx.data` 

* En la pestaña `Infrastructure`, haz clic en `Add Access +`

* Selecciona la casilla junto a `Items` para seleccionar todo y haz clic en Next

  <img src="./attachments/image19.png" alt="alt text" width="75%"><br>

* Agrega data\_scientist, haz clic en Next

  <img src="./attachments/image20.png" alt="alt text" width="75%"><br>

* Selecciona el menú desplegable y desplázate a la derecha para seleccionar los roles apropiados para el grupo de usuarios restringidos.
  * Selecciona el rol `User` para `Engines`
  * Selecciona el rol `Reader` para `storage` 
  * Selecciona el rol `User` para `catalogs`; puede que debas desplazarte a la derecha para encontrarlos todos
* Haz clic en Save

  <img src="./attachments/assignroles.png" alt="alt text" width="75%"><br>

### 13.2 Agregar política a datos iceberg

* Cambia a la pestaña `Policies`

  <img src="./attachments/image21.png" alt="alt text" width="50%"><br>

* Haz clic en `Add Policy +`

* Nombra la política `postgres_allow`, y selecciona `Policy status after creation` en `Active`, haz clic en Next

* En Choose a resource to get started, selecciona todo `postgres_catalog` 

* En Search tables habilita la casilla `all`

* Haz clic en Next

* Haz clic en `Add rule +`

* En Details selecciona Allow -> selecciona todas las acciones

* A la derecha, en Choose users or groups, haz clic en `Add +`

* Selecciona el grupo `Data_Scientist` y selecciona Add

* Haz clic en `Add`, `Add`, `Review` y `Create`


## 14 Verificar que la regla de protección de datos se está aplicando (demostración)

* Para demostrar que la regla de protección de datos se está aplicando, debemos iniciar sesión en el entorno con un usuario que no sea propietario de los datos.

* Para el bootcamp, esto corresponde a cualquier usuario que haya sido agregado al grupo Data\_Scientist.

* :teacher para demostrar:

  * Inicia sesión como usuario restringido

  * Ve a la instancia de `watsonx.data Intelligence`

  * Abre el `Bootcamp Catalog`

  * Abre el Data Asset de watsonx.data

  * Haz clic en la pestaña `Asset`

    <img src="./attachments/image23.png" alt="alt text" width="75%"><br>

  * En otra ventana, ve a la instancia de `watsonx.data`

  * Ve a `Query Workspace`

  * Navega hasta la tabla iceberg y genera un Select Statement y selecciona ejecutar en el motor Presto

    <img src="./attachments/image24.png" alt="alt text" width="75%"><br>

  * Desplázate hasta la columna SSN para ver el enmascaramiento aplicado:

    <img src="./attachments/image25a.png" alt="alt text" width="75%"><br>


En este lab has demostrado que watsonx.data permite a los data stewards enriquecer y catalogar datos como cualquier otro dato en su empresa.


¡Terminado!
