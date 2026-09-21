"""Experimento de la Parte 3: los tres casos de insertion_sort.

Mide tiempo (time.perf_counter) y numero de comparaciones de
insertion_sort sobre los tres escenarios de Tamiza para tamanos
crecientes, y produce dos graficas en graficas/.
"""

import statistics
import time
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from algoritmos import insertion_sort
from datos import generar_aleatorio, generar_casi_ordenado, generar_inverso

TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]
REPETICIONES = 3
CARPETA_GRAFICAS = Path(__file__).parent / "graficas"

ESCENARIOS = [
    ("A", "Aleatorio", generar_aleatorio),
    ("B", "Casi ordenado", generar_casi_ordenado),
    ("C", "Inverso", generar_inverso),
]


def medir(generador, n):
    """Ejecuta insertion_sort una vez y devuelve (tiempo_s, comparaciones)."""
    datos = generador(n)
    inicio = time.perf_counter()
    _, comparaciones = insertion_sort(datos)
    duracion = time.perf_counter() - inicio
    return duracion, comparaciones


def medir_escenario(generador, tamanos, repeticiones):
    """Devuelve tiempos y comparaciones de cada tamano (promediados)."""
    tiempos = []
    comparaciones = []
    for n in tamanos:
        muestras = [medir(generador, n) for _ in range(repeticiones)]
        tiempos.append(statistics.median(t for t, _ in muestras))
        comparaciones.append(muestras[0][1])
    return tiempos, comparaciones


def graficar(tamanos, resultados, archivo, titulo, tipo):
    """Genera una grafica con una curva por escenario."""
    plt.figure(figsize=(8, 5))
    for letra, nombre, _ in ESCENARIOS:
        tiempos, comparaciones = resultados[letra]
        valores = tiempos if tipo == "tiempo" else comparaciones
        plt.plot(tamanos, valores, marker="o", label=f"Escenario {letra} - {nombre}")
    plt.xlabel("Tamano de entrada (n)")
    if tipo == "tiempo":
        plt.ylabel("Tiempo (s)")
    else:
        plt.ylabel("Comparaciones entre elementos")
    plt.title(titulo)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(CARPETA_GRAFICAS / archivo)
    plt.close()


def main() -> None:
    if not CARPETA_GRAFICAS.is_dir():
        CARPETA_GRAFICAS.mkdir(parents=True)
    resultados = {}
    for letra, nombre, generador in ESCENARIOS:
        tiempos, comparaciones = medir_escenario(generador, TAMANOS, REPETICIONES)
        resultados[letra] = (tiempos, comparaciones)
        print(f"Escenario {letra} ({nombre})")
        for n, t, c in zip(TAMANOS, tiempos, comparaciones):
            print(f"  n={n:>5}  tiempo={t:.6f} s  comparaciones={c}")
    graficar(TAMANOS, resultados, "parte3_comparaciones.png", "comparaciones",
             "Insertion sort: comparaciones por escenario de Tamiza")
    graficar(TAMANOS, resultados, "parte3_tiempo.png", "tiempo",
             "Insertion sort: tiempo de ejecucion por escenario de Tamiza")


if __name__ == "__main__":
    main()
