
# Agente Tutor RAG

## Descripción

Agente de inteligencia artificial desarrollado con Python y Google ADK
que utiliza RAG (Retrieval-Augmented Generation) para ayudar a estudiantes
a consultar material académico.

El sistema permite recuperar información de documentos PDF y utilizarla
para comparar conceptos, verificar afirmaciones y preparar fichas de
estudio.

El agente utiliza Ollama para ejecutar el modelo de lenguaje y ChromaDB
para almacenar y recuperar la información de los documentos.

## Objetivo

Desarrollar un agente RAG capaz de seleccionar diferentes herramientas
según la solicitud del usuario, utilizando información documental para
generar respuestas fundamentadas.

## Tecnologías

- Python 3.12: lenguaje de programación.
- Google ADK: desarrollo y ejecución del agente.
- LiteLLM: integración del agente con Ollama.
- Ollama: ejecución de modelos de inteligencia artificial.
- Qwen 2.5 7B: modelo de lenguaje utilizado por el agente.
- nomic-embed-text: generación de embeddings.
- LangChain: procesamiento y recuperación de documentos.
- ChromaDB: almacenamiento vectorial persistente.
- PyPDFLoader: extracción del contenido de archivos PDF.
- RecursiveCharacterTextSplitter: división del texto en fragmentos.
- uv: gestión del entorno virtual y dependencias.

## Funcionamiento general

El sistema RAG se divide en dos procesos:

### 1. Indexación

1. Se carga un documento PDF.
2. Se extrae su contenido textual.
3. Se divide el texto en fragmentos.
4. Se generan embeddings mediante Ollama.
5. Se almacenan los fragmentos y sus embeddings en ChromaDB.

La indexación se realiza mediante indexar.py.

### 2. Consulta y generación

1. El usuario escribe una solicitud en ADK Web.
2. El agente identifica qué herramienta necesita.
3. La herramienta consulta la base vectorial.
4. Se recuperan fragmentos relacionados con la solicitud.
5. El agente utiliza el contexto recuperado para generar una respuesta.

## Herramientas personalizadas

### comparar_conceptos

Archivo: agente_tutor/tools/comparar.py

Recibe dos conceptos, valida los argumentos y recupera información
documental relacionada con ambos.

El agente utiliza los fragmentos para elaborar una comparación.

Ejemplo:
"Compará RAG y Fine-Tuning".

### verificar_afirmacion

Archivo: agente_tutor/tools/verificar.py

Recibe una afirmación y recupera fragmentos relacionados para que el
agente evalúe si está respaldada o contradicha por los documentos.

Si no existe evidencia suficiente, debe indicar esa limitación.

Ejemplo:
"Verificá si RAG necesita reentrenar el modelo".

### preparar_fichas

Archivo: agente_tutor/tools/fichas.py

Recibe un tema y una cantidad de fichas entre 1 y 5.

Recupera información documental para que el agente genere preguntas
y respuestas de repaso.

Ejemplo:
"Prepará 3 fichas sobre embeddings".

## Estructura del proyecto

agente_rag/
  agente_tutor/
    __init__.py
    agent.py
    recuperacion.py
    tools/
      comparar.py
      verificar.py
      fichas.py
  documentos/
    rag_teoria.pdf
  base_vectorial/
  indexar.py
  buscar.py
  requirements.txt
  .gitignore
  README.md

## Instalación

Requisitos:

- Python 3.12
- Ollama
- uv
- Git (para clonar el repositorio)

Crear el entorno virtual desde la raíz del proyecto:

    uv venv env --python 3.12

Instalar las dependencias:

    uv pip install --python .\env\Scripts\python.exe -r requirements.txt

Descargar los modelos necesarios:

    ollama pull qwen2.5:7b
    ollama pull nomic-embed-text

Comprobar los modelos:

    ollama list

## Preparación de los documentos

Colocar el PDF en la carpeta documentos/ con el nombre:

    rag_teoria.pdf

Ejecutar el indexador:

    .\env\Scripts\python.exe indexar.py

El programa extrae el contenido, genera embeddings y guarda la
información en la carpeta base_vectorial/.

No se debe ejecutar repetidamente sobre los mismos documentos sin
controlar los duplicados.

## Ejecución del agente

Desde PowerShell, configurar la conexión con Ollama:

    $env:OLLAMA_API_BASE="http://localhost:11434"

Iniciar ADK Web:

    .\env\Scripts\adk.exe web --port 8000

Abrir en el navegador:

http://localhost:8000

Seleccionar el agente_tutor para realizar consultas.

## Pruebas de herramientas

Las herramientas se prueban desde ADK Web mediante las siguientes
solicitudes:

1. "Compará RAG y Fine-Tuning".
   Herramienta esperada: comparar_conceptos.

2. "Verificá si RAG necesita reentrenamiento".
   Herramienta esperada: verificar_afirmacion.

3. "Prepará 3 fichas sobre embeddings".
   Herramienta esperada: preparar_fichas.

La ejecución de cada herramienta puede revisarse en los eventos
de ADK Web.

## Validaciones

Se contemplan:

- Argumentos vacíos.
- Tipos de datos inválidos.
- Conceptos iguales en una comparación.
- Cantidades de fichas fuera del rango permitido.
- Valores incorrectos del parámetro k.
- Ausencia de una base vectorial.
- Colecciones sin documentos.
- Excepciones durante la recuperación.

Cuando ocurre un problema, las funciones devuelven un diccionario
con un estado y un mensaje descriptivo.

## Limitaciones

- El indexador actual procesa un PDF configurado previamente.
- Volver a indexar el mismo archivo puede duplicar fragmentos.
- La recuperación por similitud no garantiza relevancia suficiente.
- El LLM puede interpretar incorrectamente los fragmentos recuperados.
- No existe todavía una verificación automática de la calidad
  de las respuestas.
- El sistema está pensado para una práctica educativa, no para
  un entorno de producción.

## Glosario

**Agente de IA:** sistema que utiliza un modelo de lenguaje y puede
seleccionar herramientas para realizar tareas.

**ADK:** framework de Google para desarrollar agentes de IA.

**RAG:** arquitectura que combina recuperación de información externa
con generación de respuestas mediante un modelo de lenguaje.

**LLM:** modelo de lenguaje grande capaz de comprender y generar texto.

**Ollama:** herramienta que permite ejecutar y utilizar modelos
de inteligencia artificial.

**LiteLLM:** biblioteca que facilita la integración con distintos
modelos y proveedores.

**Embedding:** representación numérica de un texto dentro de un
espacio vectorial.

**Chunk:** fragmento de texto obtenido durante la división de un
documento.

**Chunking:** proceso de dividir documentos en fragmentos más pequeños.

**Chunk overlap:** contenido compartido entre fragmentos consecutivos.

**ChromaDB:** base de datos vectorial utilizada para almacenar y
recuperar información.

**Búsqueda semántica:** búsqueda que utiliza representaciones del
significado del texto para recuperar información relacionada.

**Retriever:** componente encargado de recuperar fragmentos relevantes
para una consulta.

**Tool calling:** mecanismo mediante el cual un modelo puede solicitar
la ejecución de una herramienta o función.

**Prompt:** conjunto de instrucciones y contexto enviado al modelo.

**Metadatos:** información adicional que describe el origen de un
documento o fragmento, como su archivo y página.

**Indexación:** preparación de documentos para su almacenamiento
y recuperación posterior.

**FastAPI:** framework de Python para desarrollar APIs. Fue utilizado
en el material de clase, pero no es necesario para ejecutar este
agente mediante ADK Web.

## Conclusión

El proyecto implementa un agente tutor basado en RAG que incorpora
tres herramientas personalizadas con responsabilidades diferentes.

Google ADK permite seleccionar y ejecutar las herramientas, mientras
que LangChain, Ollama y ChromaDB permiten recuperar información de
documentos para elaborar respuestas.

El proyecto contempla validaciones básicas y utiliza ADK Web como
interfaz de prueba.
