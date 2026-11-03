
from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma


# Definimos las rutas del proyecto
BASE_DIR = Path(__file__).resolve().parent
RUTA_PDF = BASE_DIR / "documentos" / "RAG (Retrieval Augmented Generation)-2(1).pdf"
RUTA_DB = BASE_DIR / "base_vectorial"


# 1. Comprobamos que exista el PDF
if not RUTA_PDF.exists():
    print("Error: no se encontró el archivo PDF.")

else:
    # 2. Cargamos el contenido del PDF
    loader = PyPDFLoader(str(RUTA_PDF))
    documentos = loader.load()

    print("Páginas cargadas:", len(documentos))

    # 3. Dividimos el texto en fragmentos
    divisor = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    fragmentos = divisor.split_documents(documentos)

    print("Fragmentos generados:", len(fragmentos))

    # 4. Configuramos el modelo de embeddings
    embeddings = OllamaEmbeddings(
        model="nomic-embed-text"
    )

    # 5. Creamos la base de datos vectorial
    base_vectorial = Chroma(
        collection_name="apuntes_ia",
        embedding_function=embeddings,
        persist_directory=str(RUTA_DB)
    )

    # 6. Guardamos los fragmentos en ChromaDB
    base_vectorial.add_documents(fragmentos)

    print("Documento indexado correctamente.")
