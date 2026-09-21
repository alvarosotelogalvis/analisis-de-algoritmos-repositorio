"""Experimento de la Parte 4.2: tiempo de merge_sort vs insertion_sort.

Mide con time.perf_counter el tiempo de ambos algoritmos sobre el
escenario A de Tamiza y produce la grafica parte4_tiempo.png.
"""

import statistics
import time
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio

TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]
REPETICIONES = 3
CARPETA_GRAFICAS = Path(__file__).parent / "graficas"

ALGORITMOS = [
    ("Insertion sort", insertion_sort),
    ("Merge sort", merge_sort),
]


def medir(funcion, n):
    """Ejecuta funcion sobre un lote aleatorio y devuelve el tiempo en s."""
    datos = generar_aleatorio(n)
    inicio = time.perf_counter()
    funcion(datos)
    return time.perf_counter() - inicio


def medir_tiempos(funcion, tamanos, repeticiones):
    """Devuelve la mediana del tiempo por tamano."""
    tiempos = []
    for n in tamanos:
        muestras = [medir(funcion, n) for _ in range(repeticiones)]
        tiempos.append(statistics.median(muestras))
    return tiempos


def graficar(tamanos, tiempos_por_algoritmo):
    """Dibuja una curva por algoritmo en los mismos ejes."""
    plt.figure(figsize=(8, 5))
    for nombre, tiempos in tiempos_por_algoritmo:
        plt.plot(tamanos, tiempos, marker="o", label=nombre)
    plt.xlabel("Tamano de entrada (n)")
    plt.ylabel("Tiempo (s)")
    plt.title("Tiempo de ejecucion sobre el escenario A de Tamiza")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(CARPETA_GRAFICAS / "parte4_tiempo.png")
    plt.close()


def main() -> None:
    if not CARPETA_GRAFICAS.is_dir():
        CARPETA_GRAFICAS.mkdir(parents=True)
    tiempos_por_algoritmo = []
    for nombre, funcion in ALGORITMOS:
        tiempos = medir_tiempos(funcion, TAMANOS, REPETICIONES)
        tiempos_por_algoritmo.append((nombre, tiempos))
        print(nombre)
        for n, t in zip(TAMANOS, tiempos):
            print(f"  n={n:>5}  tiempo={t:.6f} s")
    graficar(TAMANOS, tiempos_por_algoritmo)


if __name__ == "__main__":
    main()
    