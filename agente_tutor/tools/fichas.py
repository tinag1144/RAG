
from agente_tutor.recuperacion import buscar_documentos


def preparar_fichas(tema: str, cantidad: int = 3) -> dict:
    """
    Recupera información para preparar fichas de estudio.

    Args:
        tema: Tema sobre el que se crearán las fichas.
        cantidad: Número de fichas, entre 1 y 5.

    Returns:
        Diccionario con el contexto recuperado o un error.
    """

    # Validamos que el tema sea un texto
    if not isinstance(tema, str):
        return {
            "estado": "error",
            "mensaje": "El tema debe ser un texto."
        }

    # Eliminamos espacios innecesarios
    tema = tema.strip()

    # Comprobamos que el tema no esté vacío
    if not tema:
        return {
            "estado": "error",
            "mensaje": "Debés indicar un tema de estudio."
        }

    # Validamos la cantidad solicitada
    if type(cantidad) is not int or cantidad < 1 or cantidad > 5:
        return {
            "estado": "error",
            "mensaje": "La cantidad de fichas debe estar entre 1 y 5."
        }

    # Recuperamos información sobre el tema
    resultado = buscar_documentos(
        pregunta=tema,
        k=5
    )

    # Controlamos errores o ausencia de información
    if resultado["estado"] != "correcto":
        return resultado

    # Devolvemos el contenido al agente
    return {
        "estado": "correcto",
        "tema": tema,
        "cantidad_fichas": cantidad,
        "fragmentos": resultado["fragmentos"],
        "mensaje": (
            "Prepará las fichas usando los fragmentos. "
            "Cada ficha debe contener una pregunta y su respuesta. "
            "No inventes información que no esté en las fuentes. "
            "Si no hay contenido suficiente, indicalo."
        )
    }
