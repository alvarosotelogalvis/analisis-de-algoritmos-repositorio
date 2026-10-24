# Retroalimentación — Laboratorio 2: Dividir y vencer

**Estudiante:** Alvaro Sotelo Galvis · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `b371cbe`

Muy buen trabajo: sus soluciones son correctas y el informe es claro.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 17 / 20 |
| Calidad de la explicación teórica | 19 / 20 |
| Corrección de la implementación | 25 / 25 |
| Calidad del análisis de las gráficas | 22 / 25 |
| Documentación y organización del informe | 9 / 10 |
| **Total** | **92 / 100** |
| **Nota (0–5)** | **4.60** |

## 1. Corrección conceptual (17 / 20)
**Lo que hizo bien:**
- Compara con el máximo de un arreglo y explica bien que combinar cuesta una sola comparación, así que dividir no mejora el tiempo.
- Recomienda divide y vencerás y estima el tiempo para 1.000.000 de registros, declarando que es una estimación y sin usar regla de tres lineal.

**Lo que puede mejorar:**
- Dice que a partir de n = 100 gana divide y vencerás y que en n = 10 y 50 gana la fuerza bruta. Eso no se puede comprobar con lo publicado: ni en su gráfica ni en una tabla del informe. Incluya una tabla con los tiempos medidos.

## 2. Calidad de la explicación teórica (19 / 20)
**Lo que hizo bien:**
- Plantea `T(n) = 2T(n/2) + Θ(n)`, explica de dónde sale cada término y la resuelve con el método maestro, verificando el caso 2.
- Justifica bien por qué la fuerza bruta es `Θ(n²)`.

**Lo que puede mejorar:**
- Al explicar el caso 2 conviene mencionar también que la condición se cumple con constantes concretas, no solo "tiene el mismo orden".

## 3. Corrección de la implementación (25 / 25)
**Lo que hizo bien:**
- Las tres funciones dan la suma correcta en todos los casos pedidos, resuelven los tres casos y no modifican la lista.
- Tienen `type hints` y `docstrings`; las pruebas cubren todo lo exigido, con 20 listas aleatorias.

## 4. Calidad del análisis de las gráficas (22 / 25)
**Lo que hizo bien:**
- La gráfica tiene título, ejes rotulados, leyenda, ambas curvas en los mismos ejes y seis tamaños.
- Calcula el factor al duplicar n (500 a 1000) y lo compara con `Θ(n²)` y `Θ(n log n)`; lo que dice de la fuerza bruta coincide con la gráfica (cerca de 0.018 s en 500, 0.075 s en 1000 y 1.03 s en 4000).

**Lo que puede mejorar:**
- Los factores que reporta (4.04 y 1.76) no se pueden verificar con lo publicado.

## 5. Documentación y organización del informe (9 / 10)
**Lo que hizo bien:**
- Carpeta en la ubicación acordada, archivos con los nombres pedidos, gráfica visible, enlaces al código y 4 commits descriptivos.

**Lo que puede mejorar:**
- Las instrucciones para activar el entorno solo sirven en Windows (`venv\Scripts\activate`); añada el comando para macOS/Linux.

## ¿El código funciona?
Sí. Las pruebas pasan y la medición corre sin errores y genera la gráfica. Ambas soluciones coinciden con una referencia en listas aleatorias.

## Para el próximo laboratorio
- Incluya una tabla con los tiempos medidos para poder sustentar cada cifra que cite.
- Verifique que todas las funciones tengan *type hints*, *docstring* con `Args` y `Returns`, y dos líneas en blanco entre ellas.
- Indique cómo reproducir el experimento en distintos sistemas operativos.
