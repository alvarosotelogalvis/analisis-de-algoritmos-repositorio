"""Pruebas de verificacion de las soluciones del subarreglo maximo."""

import random

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo


def main() -> None:
    """Ejecuta los casos de prueba exigidos por el laboratorio."""
    # 1. Serie de ocho dias (suma 17).
    serie = [-3, 5, -2, 8, -6, 3, 9, -4]
    assert subarreglo_fuerza_bruta(serie)[2] == 17
    assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == 17

    # 2. Un solo elemento.
    assert subarreglo_fuerza_bruta([42.0])[2] == 42.0
    assert subarreglo_maximo([42.0], 0, 0)[2] == 42.0
    assert subarreglo_fuerza_bruta([-7.0])[2] == -7.0
    assert subarreglo_maximo([-7.0], 0, 0)[2] == -7.0

    # 3. Todos los valores negativos.
    negativos = [-8.0, -3.0, -6.0, -1.0, -9.0]
    assert subarreglo_fuerza_bruta(negativos)[2] == -1.0
    assert subarreglo_maximo(negativos, 0, len(negativos) - 1)[2] == -1.0

    # 4. Todos los valores positivos.
    positivos = [4.0, 1.0, 7.0, 2.0]
    assert subarreglo_fuerza_bruta(positivos)[2] == 14.0
    assert subarreglo_maximo(positivos, 0, len(positivos) - 1)[2] == 14.0

    # 5. Tramo que cruza el punto medio (indices 2..5, suma 8).
    cruzado = [2.0, -5.0, 3.0, 4.0, -1.0, 2.0]
    assert subarreglo_fuerza_bruta(cruzado)[2] == 8.0
    assert subarreglo_maximo(cruzado, 0, len(cruzado) - 1)[2] == 8.0

    # 6. Veinte listas aleatorias con semilla fija: ambas soluciones coinciden.
    rng = random.Random(2026)
    for _ in range(20):
        n = rng.randint(1, 40)
        lista = [rng.randint(-100, 100) for _ in range(n)]
        assert subarreglo_fuerza_bruta(lista)[2] == subarreglo_maximo(
            lista, 0, n - 1
        )[2]

    # 7. Ninguna funcion modifica la lista recibida.
    original = [1.0, -2.0, 3.0]
    copia = list(original)
    subarreglo_fuerza_bruta(original)
    subarreglo_maximo(original, 0, len(original) - 1)
    assert original == copia

    print("Todas las pruebas pasaron.")


if __name__ == "__main__":
    main()
