"""Experimentos de la Parte 2: busqueda en lista enlazada y en tabla hash.

Experimento A: mide con time.perf_counter el tiempo medio por busqueda de
guias inexistentes en la lista y en la tabla (con alfa cercano a 2) para
varios valores de n, verifica que ambas coinciden y produce
graficas/lista_vs_tabla.png.

Experimento B: con n fijo, construye tablas con distinto m para variar el
factor de carga alfa, mide el tiempo medio por busqueda de guias
inexistentes en cada una y produce graficas/tiempo_vs_alfa.png.
"""

import random
import time
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from estructuras import ListaEnlazada, TablaHash

TAMANOS = [100, 500, 1000, 5000, 20000, 50000]
N_FIJO = 20000
ALFAS = [0.25, 0.5, 1, 2, 4, 10]
BUSQUEDAS = 200
REPETICIONES = 3
REPETICIONES_TABLA = 51
MUESTRA_VERIFICACION = 100
SEMILLA = 2026
ESTADOS = ["en bodega", "en reparto", "entregado"]

CARPETA_GRAFICAS = Path(__file__).parent / "graficas"


def generar_guias_inexistentes(
    existentes: set[int], cantidad: int, semilla: int = 7
) -> list[int]:
    """Genera guias de diez digitos que no estan en la coleccion.

    Args:
        existentes: guias almacenadas en las estructuras.
        cantidad: cuantas guias inexistentes generar.
        semilla: semilla del generador, para reproducir la medicion.

    Returns:
        Una lista con `cantidad` guias que no pertenecen a `existentes`.
    """
    azar = random.Random(semilla)
    inexistentes: list[int] = []
    while len(inexistentes) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in existentes:
            inexistentes.append(guia)
    return inexistentes


def generar_envios(n: int, semilla: int = SEMILLA) -> list[tuple[int, str]]:
    """Genera n envios con guias distintas de diez digitos.

    Args:
        n: numero de guias a generar.
        semilla: semilla del generador aleatorio.

    Returns:
        Lista de n tuplas (guia, estado), con guias sin repetir.
    """
    rng = random.Random(semilla)
    guias = rng.sample(range(10**9, 10**10), n)
    return [(guia, rng.choice(ESTADOS)) for guia in guias]


def es_primo(numero: int) -> bool:
    """Indica si un numero es primo, probando divisores hasta su raiz.

    Args:
        numero: entero a revisar.

    Returns:
        True si el numero es primo, False en otro caso.
    """
    if numero < 2:
        return False
    divisor = 2
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False
        divisor += 1
    return True


def primo_cercano(objetivo: int) -> int:
    """Busca el primo mas cercano a un valor, empezando por los mayores.

    Args:
        objetivo: valor alrededor del cual se busca el primo.

    Returns:
        El primo mas cercano a objetivo (si hay empate, el mayor).
    """
    distancia = 0
    while True:
        if es_primo(objetivo + distancia):
            return objetivo + distancia
        if es_primo(objetivo - distancia):
            return objetivo - distancia
        distancia += 1


def construir_estructuras(
    envios: list[tuple[int, str]], m: int
) -> tuple[ListaEnlazada, TablaHash]:
    """Inserta los mismos envios en una lista y en una tabla de m casillas.

    Args:
        envios: tuplas (guia, estado) a insertar.
        m: numero de casillas de la tabla hash.

    Returns:
        La lista enlazada y la tabla hash ya llenas.
    """
    lista = ListaEnlazada()
    tabla = TablaHash(m)
    for guia, estado in envios:
        lista.insertar(guia, estado)
        tabla.insertar(guia, estado)
    return lista, tabla


def verificar_coincidencia(
    lista: ListaEnlazada, tabla: TablaHash, envios: list[tuple[int, str]]
) -> None:
    """Comprueba que lista y tabla devuelven el estado correcto.

    Args:
        lista: lista enlazada con los envios.
        tabla: tabla hash con los mismos envios.
        envios: tuplas (guia, estado) insertadas en ambas.
    """
    rng = random.Random(SEMILLA)
    muestra = rng.sample(envios, min(MUESTRA_VERIFICACION, len(envios)))
    for guia, estado in muestra:
        assert lista.buscar(guia) == estado, f"La lista falla en {guia}"
        assert tabla.buscar(guia) == estado, f"La tabla falla en {guia}"


def medir_busquedas(
    estructura: ListaEnlazada | TablaHash, guias: list[int], repeticiones: int
) -> float:
    """Mide el tiempo medio por busqueda sobre una estructura.

    Cronometra solo el ciclo de busquedas, repite la medicion y toma el
    minimo, que es la repeticion menos afectada por el ruido del sistema
    operativo.

    Args:
        estructura: lista enlazada o tabla hash donde se busca.
        guias: guias a buscar.
        repeticiones: cuantas veces se repite la medicion completa.

    Returns:
        El menor tiempo medio por busqueda entre las repeticiones, en
        segundos.
    """
    muestras = []
    for _ in range(repeticiones):
        inicio = time.perf_counter()
        for guia in guias:
            estructura.buscar(guia)
        muestras.append((time.perf_counter() - inicio) / len(guias))
    return min(muestras)


def graficar_lista_vs_tabla(
    tamanos: list[int], tiempos_lista: list[float], tiempos_tabla: list[float]
) -> None:
    """Dibuja el tiempo medio por busqueda de ambas estructuras frente a n.

    Args:
        tamanos: valores de n medidos.
        tiempos_lista: tiempo medio por busqueda en la lista (s).
        tiempos_tabla: tiempo medio por busqueda en la tabla (s).
    """
    plt.figure(figsize=(8, 5))
    plt.plot(tamanos, tiempos_lista, marker="o", label="Lista enlazada")
    plt.plot(tamanos, tiempos_tabla, marker="s", label="Tabla hash (alfa ~ 2)")
    plt.xlabel("Numero de guias n (guias)")
    plt.ylabel("Tiempo medio por busqueda (s)")
    plt.title("Busqueda de guias inexistentes: lista enlazada vs. tabla hash")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(CARPETA_GRAFICAS / "lista_vs_tabla.png")
    plt.close()


def experimento_a() -> None:
    """Mide lista y tabla para cada n, imprime la tabla y guarda la grafica."""
    tiempos_lista = []
    tiempos_tabla = []
    print("Experimento A: lista enlazada vs. tabla hash")
    print(f"{'n':>6} {'m':>6} {'alfa':>5} {'lista (s)':>12} {'tabla (s)':>12}")
    for n in TAMANOS:
        envios = generar_envios(n)
        m = primo_cercano(n // 2)
        lista, tabla = construir_estructuras(envios, m)
        verificar_coincidencia(lista, tabla, envios)

        existentes = {guia for guia, _ in envios}
        inexistentes = generar_guias_inexistentes(existentes, BUSQUEDAS)

        t_lista = medir_busquedas(lista, inexistentes, REPETICIONES)
        t_tabla = medir_busquedas(tabla, inexistentes, REPETICIONES_TABLA)
        tiempos_lista.append(t_lista)
        tiempos_tabla.append(t_tabla)
        print(
            f"{n:>6} {m:>6} {tabla.factor_carga():>5.2f}"
            f" {t_lista:>12.3e} {t_tabla:>12.3e}"
        )

    graficar_lista_vs_tabla(TAMANOS, tiempos_lista, tiempos_tabla)
    print(f"Grafica guardada en {CARPETA_GRAFICAS / 'lista_vs_tabla.png'}")


def graficar_tiempo_vs_alfa(alfas: list[float], tiempos: list[float]) -> None:
    """Dibuja el tiempo medio por busqueda de la tabla frente a alfa.

    Args:
        alfas: factores de carga medidos.
        tiempos: tiempo medio por busqueda en cada tabla (s).
    """
    microsegundos = [t * 1e6 for t in tiempos]
    plt.figure(figsize=(8, 5))
    plt.plot(
        alfas, microsegundos, marker="s", color="tab:orange",
        label=f"Tabla hash (n = {N_FIJO})",
    )
    plt.xlabel("Factor de carga alfa = n / m (guias por casilla)")
    plt.ylabel("Tiempo medio por busqueda (microsegundos)")
    plt.title("Tabla hash: tiempo de busqueda de guias inexistentes vs. alfa")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(CARPETA_GRAFICAS / "tiempo_vs_alfa.png")
    plt.close()


def experimento_b() -> None:
    """Mide la tabla con n fijo y varios alfa, imprime y guarda la grafica."""
    envios = generar_envios(N_FIJO)
    existentes = {guia for guia, _ in envios}
    inexistentes = generar_guias_inexistentes(existentes, BUSQUEDAS)

    alfas_reales = []
    tiempos = []
    print(f"\nExperimento B: efecto del factor de carga (n = {N_FIJO})")
    print(f"{'alfa obj.':>9} {'m':>6} {'alfa':>6} {'tabla (us)':>12}")
    for alfa in ALFAS:
        m = primo_cercano(round(N_FIJO / alfa))
        lista, tabla = construir_estructuras(envios, m)
        verificar_coincidencia(lista, tabla, envios)

        t_tabla = medir_busquedas(tabla, inexistentes, REPETICIONES_TABLA)
        alfas_reales.append(tabla.factor_carga())
        tiempos.append(t_tabla)
        print(
            f"{alfa:>9} {m:>6} {tabla.factor_carga():>6.2f}"
            f" {t_tabla * 1e6:>12.3f}"
        )

    graficar_tiempo_vs_alfa(alfas_reales, tiempos)
    print(f"Grafica guardada en {CARPETA_GRAFICAS / 'tiempo_vs_alfa.png'}")


def main() -> None:
    """Ejecuta los experimentos de la Parte 2."""
    if not CARPETA_GRAFICAS.is_dir():
        CARPETA_GRAFICAS.mkdir(parents=True)
    experimento_a()
    experimento_b()


if __name__ == "__main__":
    main()
