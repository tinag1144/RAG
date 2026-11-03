
from agente_tutor.recuperacion import buscar_documentos


def comparar_conceptos(concepto1: str, concepto2: str) -> dict:
    """
    Busca información en los documentos para comparar dos conceptos.

    Args:
        concepto1: Primer concepto.
        concepto2: Segundo concepto.

    Returns:
        Diccionario con la información recuperada.
    """

    # Verificamos que ambos conceptos sean textos
    if not isinstance(concepto1, str) or not isinstance(concepto2, str):
        return {
            "estado": "error",
            "mensaje": "Los conceptos deben ser textos."
        }

    # Quitamos espacios innecesarios
    concepto1 = concepto1.strip()
    concepto2 = concepto2.strip()

    # Comprobamos que no estén vacíos
    if not concepto1 or not concepto2:
        return {
            "estado": "error",
            "mensaje": "Debés indicar dos conceptos válidos."
        }

    # Comprobamos que sean diferentes
    if concepto1.lower() == concepto2.lower():
        return {
            "estado": "error",
            "mensaje": "Los conceptos deben ser diferentes."
        }

    # Buscamos información de cada concepto
    resultado1 = buscar_documentos(concepto1, k=3)
    resultado2 = buscar_documentos(concepto2, k=3)

    # Comprobamos si alguna búsqueda falló
    if resultado1["estado"] != "correcto":
        return resultado1

    if resultado2["estado"] != "correcto":
        return resultado2

    # Devolvemos los resultados de ambas búsquedas
    return {
        "estado": "correcto",
        "concepto1": concepto1,
        "concepto2": concepto2,
        "informacion_concepto1": resultado1,
        "informacion_concepto2": resultado2,
        "mensaje": "Comparar utilizando los fragmentos recuperados."
    }
