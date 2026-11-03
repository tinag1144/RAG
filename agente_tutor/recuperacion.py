
from pathlib import Path

from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings


# Rutas del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent
RUTA_DB = BASE_DIR / "base_vectorial"


def buscar_documentos(pregunta: str, k: int = 3) -> dict:
    """
    Recupera fragmentos relacionados con una consulta.

    Args:
        pregunta: Texto de búsqueda.
        k: Cantidad máxima de resultados, entre 1 y 5.

    Returns:
        Estado, cantidad y fragmentos recuperados.
    """

    # Validación de la pregunta
    if not isinstance(pregunta, str) or not pregunta.strip():
        return {
            "estado": "error",
            "mensaje": "La consulta debe contener texto.",
            "fragmentos": []
        }

    # Validación de k
    if type(k) is not int or not 1 <= k <= 5:
        return {
            "estado": "error",
            "mensaje": "El valor de k debe ser un entero entre 1 y 5.",
            "fragmentos": []
        }

    # Validación de la carpeta de almacenamiento
    if not RUTA_DB.exists():
        return {
            "estado": "error",
            "mensaje": "No existe la base vectorial. Ejecutá indexar.py.",
            "fragmentos": []
        }

    try:
        # Modelo utilizado durante la indexación
        embeddings = OllamaEmbeddings(
            model="nomic-embed-text"
        )

        # Abrimos la colección de ChromaDB
        base_vectorial = Chroma(
            collection_name="apuntes_ia",
            embedding_function=embeddings,
            persist_directory=str(RUTA_DB)
        )

        # Comprobamos si la colección tiene documentos
        registros = base_vectorial.get(limit=1)

        if not registros["ids"]:
            return {
                "estado": "sin_resultados",
                "mensaje": "No hay documentos indexados en la colección.",
                "fragmentos": []
            }

        # Realizamos la búsqueda semántica
        resultados = base_vectorial.similarity_search(
            query=pregunta.strip(),
            k=k
        )

        if not resultados:
            return {
                "estado": "sin_resultados",
                "mensaje": "No se recuperaron fragmentos.",
                "fragmentos": []
            }

        # Preparamos los resultados
        fragmentos = []

        for documento in resultados:
            fragmentos.append({
                "texto": documento.page_content,
                "fuente": documento.metadata.get(
                    "source", "Desconocida"
                ),
                "pagina": documento.metadata.get("page")
            })

        return {
            "estado": "correcto",
            "cantidad": len(fragmentos),
            "fragmentos": fragmentos
        }

    except Exception as error:
        return {
            "estado": "error",
            "mensaje": f"Error durante la búsqueda: {error}",
            "fragmentos": []
        }
