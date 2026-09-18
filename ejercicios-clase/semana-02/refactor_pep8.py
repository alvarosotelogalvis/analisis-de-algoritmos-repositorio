"""Script refactorizado: calculo del promedio de una lista siguiendo PEP 8."""


def calcular_promedio(lista: list[float]) -> float:
    """Calcula el promedio aritmetico de los valores de una lista.

    Args:
        lista: secuencia de numeros a promediar.

    Returns:
        El promedio de los valores de la lista.
    """
    suma = 0
    for valor in lista:
        suma += valor
    return suma / len(lista)


def main() -> None:
    """Punto de entrada: calcula y muestra el promedio de un ejemplo."""
    valores = [1, 2, 3, 4, 5]
    promedio = calcular_promedio(valores)
    print(promedio)


if __name__ == "__main__":
    main()