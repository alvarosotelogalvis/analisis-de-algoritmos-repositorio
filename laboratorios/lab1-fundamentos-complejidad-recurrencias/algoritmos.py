"""Algoritmos de ordenamiento instrumentados para el Laboratorio 1."""


def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de insercion.

    No modifica la lista recibida: trabaja sobre una copia.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    resultado = datos.copy()
    comparaciones = 0
    for j in range(1, len(resultado)):
        clave = resultado[j]
        i = j - 1
        while i >= 0:
            comparaciones += 1
            if resultado[i] < clave:
                resultado[i + 1] = resultado[i]
                i -= 1
            else:
                break
        resultado[i + 1] = clave
    return resultado, comparaciones

def merge_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de mezcla.

    No modifica la lista recibida: trabaja sobre una copia.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    resultado, comparaciones = _merge_sort_recursivo(datos.copy())
    return resultado, comparaciones


def _merge_sort_recursivo(parte: list[int]) -> tuple[list[int], int]:
    """Ordena una sublista por mezcla y devuelve (ordenada, comparaciones)."""
    n = len(parte)
    if n <= 1:
        return parte, 0
    medio = n // 2
    izquierda, ci = _merge_sort_recursivo(parte[:medio])
    derecha, cd = _merge_sort_recursivo(parte[medio:])
    mezclada, cm = _mezclar(izquierda, derecha)
    return mezclada, ci + cd + cm


def _mezclar(izquierda: list[int], derecha: list[int]) -> tuple[list[int], int]:
    """Combina dos sublistas ordenadas en una sola, contando comparaciones."""
    resultado = []
    i = j = 0
    comparaciones = 0
    while i < len(izquierda) and j < len(derecha):
        comparaciones += 1
        if izquierda[i] >= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado, comparaciones
