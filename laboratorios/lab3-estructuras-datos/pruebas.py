"""Pruebas de verificacion de la lista enlazada y la tabla hash."""

import random

from estructuras import ListaEnlazada, TablaHash

ESTADOS = ["en bodega", "en reparto", "entregado"]


def main() -> None:
    """Ejecuta los casos de prueba exigidos por el laboratorio."""
    # 1. Serie de ejemplo del enunciado: busqueda exitosa e infructuosa.
    serie = [
        (1000000010, "en bodega"),
        (1000000024, "en reparto"),
        (1000000017, "en bodega"),
        (1000000005, "entregado"),
    ]
    lista = ListaEnlazada()
    tabla = TablaHash(7)
    for guia, estado in serie:
        lista.insertar(guia, estado)
        tabla.insertar(guia, estado)

    assert lista.buscar(1000000024) == "en reparto"
    assert tabla.buscar(1000000024) == "en reparto"
    assert lista.buscar(1000000005) == "entregado"
    assert tabla.buscar(1000000005) == "entregado"
    assert lista.buscar(1000000099) is None
    assert tabla.buscar(1000000099) is None
    assert lista.tamano == 4
    assert tabla.tamano == 4

    # 2. Estructuras vacias: ninguna busqueda encuentra nada.
    assert ListaEnlazada().buscar(10) is None
    assert TablaHash(7).buscar(10) is None

    # 3. Colision forzada: con m = 7, las guias 10, 24 y 17 caen en la casilla 3.
    tabla = TablaHash(7)
    for guia in (10, 24, 17):
        assert tabla.hash(guia) == 3
        tabla.insertar(guia, "en bodega")

    assert tabla.buscar(10) == "en bodega"
    assert tabla.buscar(24) == "en bodega"
    assert tabla.buscar(17) == "en bodega"
    assert tabla.buscar(99) is None
    assert tabla.casillas[3].tamano == 3

    # 4. Factor de carga tras las tres inserciones.
    assert tabla.factor_carga() == 3 / 7

    # 5. Veinte colecciones aleatorias con semilla fija: lista y tabla coinciden.
    rng = random.Random(2026)
    for _ in range(20):
        n = rng.randint(1, 300)
        m = rng.randint(1, 50)
        guias = rng.sample(range(10**9, 10**10), n)
        lista = ListaEnlazada()
        tabla = TablaHash(m)
        for guia in guias:
            estado = rng.choice(ESTADOS)
            lista.insertar(guia, estado)
            tabla.insertar(guia, estado)

        for guia in guias:
            assert lista.buscar(guia) == tabla.buscar(guia)
            assert tabla.buscar(guia) is not None

        for _ in range(50):
            guia = rng.randint(10**9, 10**10 - 1)
            if guia not in guias:
                assert lista.buscar(guia) is None
                assert tabla.buscar(guia) is None

    print("Todas las pruebas pasaron.")


if __name__ == "__main__":
    main()
