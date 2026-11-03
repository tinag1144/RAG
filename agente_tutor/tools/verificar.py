
from agente_tutor.recuperacion import buscar_documentos


def verificar_afirmacion(afirmacion: str) -> dict:
    """
    Recupera evidencia para evaluar una afirmación.

    Args:
        afirmacion: Texto que el usuario desea verificar.

    Returns:
        Diccionario con evidencia o un error.
    """

    if not isinstance(afirmacion, str):
        return {
            "estado": "error",
            "mensaje": "La afirmación debe ser un texto."
        }

    afirmacion = afirmacion.strip()

    if not afirmacion:
        return {
            "estado": "error",
            "mensaje": "Debés ingresar una afirmación."
        }

    resultado = buscar_documentos(
        pregunta=afirmacion,
        k=4
    )

    if resultado["estado"] != "correcto":
        return resultado

    return {
        "estado": "correcto",
        "afirmacion": afirmacion,
        "cantidad": resultado["cantidad"],
        "evidencia": resultado["fragmentos"],
        "mensaje": (
            "Analizá la evidencia recuperada. "
            "Determiná si la afirmación está respaldada, "
            "contradicha o si no hay información suficiente. "
            "Justificá la conclusión con los documentos."
        )
    }
