
from pathlib import Path

from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings


# 1. Ubicamos la base vectorial del proyecto
BASE_DIR = Path(__file__).resolve().parent
RUTA_DB = BASE_DIR / "base_vectorial"


# 2. Configuramos el mismo modelo de embeddings
embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)


# 3. Nos conectamos a la colección existente
base_vectorial = Chroma(
    collection_name="apuntes_ia",
    embedding_function=embeddings,
    persist_directory=str(RUTA_DB)
)


# 4. Definimos la pregunta
pregunta = "¿Qué es RAG?"


# 5. Buscamos los fragmentos más relevantes
resultados = base_vectorial.similarity_search(
    query=pregunta,
    k=3
)


# 6. Mostramos los resultados
print("Pregunta:", pregunta)
print("Fragmentos encontrados:", len(resultados))

for numero, documento in enumerate(resultados, start=1):
    print(f"\n--- FRAGMENTO {numero} ---")
    print(documento.page_content)
    print("Fuente:", documento.metadata.get("source"))
    print("Página:", documento.metadata.get("page"))
