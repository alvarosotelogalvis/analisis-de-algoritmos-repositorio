"""Experimento de la Parte 2: subarreglo maximo por las dos soluciones.

Mide con time.perf_counter el tiempo de la fuerza bruta y de divide y
venceras sobre la misma serie para cada tamano, verifica que ambas
coinciden y produce graficas/tiempo_vs_n.png.
"""

import random
import statistics
import time
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo

TAMANOS = [10, 50, 100, 500, 1000, 4000]
REPETICIONES = 3
SEMILLA = 2026

CARPETA_GRAFICAS = Path(__file__).parent / "graficas"


def generar_serie(n: int, semilla: int = SEMILLA) -> list[int]:
    """Genera n variaciones diarias enteras reproducibles.

    Args:
        n: tamano de entrada (cantidad de dias).
        semilla: semilla del generador aleatorio.

    Returns:
        Lista de n enteros entre -100 y 100, en el orden generado.
    """
    rng = random.Random(semilla)
    return [rng.randint(-100, 100) for _ in range(n)]


def medir_fuerza_bruta(serie: list[int], repeticiones: int) -> float:
    """Devuelve la mediana del tiempo (s) de la fuerza bruta sobre serie."""
    muestras = []
    for _ in range(repeticiones):
        inicio = time.perf_counter()
        subarreglo_fuerza_bruta(serie)
        muestras.append(time.perf_counter() - inicio)
    return statistics.median(muestras)


def medir_divide_y_venceras(serie: list[int], repeticiones: int) -> float:
    """Devuelve la mediana del tiempo (s) de divide y venceras sobre serie."""
    fin = len(serie) - 1
    muestras = []
    for _ in range(repeticiones):
        inicio = time.perf_counter()
        subarreglo_maximo(serie, 0, fin)
        muestras.append(time.perf_counter() - inicio)
    return statistics.median(muestras)


def graficar(
    tamanos: list[int], tiempos_fuerza: list[float], tiempos_dyv: list[float]
) -> None:
    """Dibuja las dos curvas de tiempo en los mismos ejes."""
    plt.figure(figsize=(8, 5))
    plt.plot(tamanos, tiempos_fuerza, marker="o", label="Fuerza bruta (n^2)")
    plt.plot(tamanos, tiempos_dyv, marker="s", label="Divide y venceras (n log n)")
    plt.xlabel("Tamano de entrada n (elementos)")
    plt.ylabel("Tiempo de ejecucion (s)")
    plt.title("Subarreglo maximo: tiempo de ejecucion vs. tamano de entrada")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(CARPETA_GRAFICAS / "tiempo_vs_n.png")
    plt.close()


def main() -> None:
    """Verifica coincidencias, mide los tiempos y guarda la grafica."""
    if not CARPETA_GRAFICAS.is_dir():
        CARPETA_GRAFICAS.mkdir(parents=True)

    tiempos_fuerza = []
    tiempos_dyv = []
    for n in TAMANOS:
        serie = generar_serie(n)

        suma_fuerza = subarreglo_fuerza_bruta(serie)[2]
        suma_dyv = subarreglo_maximo(serie, 0, n - 1)[2]
        assert suma_fuerza == suma_dyv, f"Discrepancia en n={n}"

        t_fuerza = medir_fuerza_bruta(serie, REPETICIONES)
        t_dyv = medir_divide_y_venceras(serie, REPETICIONES)
        tiempos_fuerza.append(t_fuerza)
        tiempos_dyv.append(t_dyv)
        print(
            f"n={n:>5}  fuerza bruta={t_fuerza:.6f} s"
            f"  divide y venceras={t_dyv:.6f} s"
        )

    graficar(TAMANOS, tiempos_fuerza, tiempos_dyv)
    print(f"Grafica guardada en {CARPETA_GRAFICAS / 'tiempo_vs_n.png'}")


if __name__ == "__main__":
    main()
