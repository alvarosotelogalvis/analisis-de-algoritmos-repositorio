# Retroalimentación — Lab 03 Estructuras de datos

**Estudiante:** Alvaro Sotelo Galvis · **Laboratorio:** Laboratorio evaluativo 03 — Estructuras de datos
**Fecha límite:** 2026-11-01 23:59 · **Versión revisada:** commit `e0bfa1b`

Excelente trabajo: entregó un laboratorio completo, ordenado y que funciona.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 19 / 20 |
| Calidad de la explicación teórica | 20 / 20 |
| Corrección de la implementación | 25 / 25 |
| Calidad del análisis de las gráficas | 25 / 25 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **99 / 100** |
| **Nota (0–5)** | **4.95** |

## 1. Corrección conceptual (19 / 20)
**Lo que hizo bien:**
- Explica bien qué es una colisión y por qué ocurre aunque sobren casillas, y usa el ejemplo de `10`, `24` y `17` con `m = 7`.
- Compara encadenamiento y direccionamiento abierto con su ventaja y su costo.
- Explica con claridad por qué la tabla hash no sirve para rangos y qué ofrece el árbol.
- Recomienda una combinación (tabla hash más árbol balanceado) y declara sus cifras a 5.000.000 como estimación.

**Lo que puede mejorar (y cómo corregirlo):**
- En la pregunta 4 no dice cuál sería la altura del árbol degenerado y solo da las comparaciones de una búsqueda, no las de insertar todas las guías.
  → *Cómo corregirlo:* diga cuántos niveles tendría el árbol si cada guía va a la derecha de la anterior, y piense cuántas comparaciones cuesta cada inserción a medida que el árbol crece, para estimar el total y compararlo con el árbol equilibrado.
- En la pregunta 5 la estimación de la tabla repite lo medido sin explicar la forma de la curva.
  → *Cómo corregirlo:* justifique por qué con `α` fijo el tiempo de la tabla no depende de `n`, apoyándose en sus datos de la primera gráfica.

## 2. Calidad de la explicación teórica (20 / 20)
**Lo que hizo bien:**
- Justifica el `Θ(n)` de la lista y el `Θ(1 + α)` de la tabla.
- Nombra el supuesto de hash uniforme simple y explica qué pasa si todas las guías caen en una casilla.

## 3. Corrección de la implementación (25 / 25)
**Lo que hizo bien:**
- Ambas estructuras devuelven el estado correcto en búsquedas exitosas e infructuosas.
- La colisión forzada con `m = 7` funciona y `factor_carga` da `3/7`.
- Las pruebas cubren veinte colecciones aleatorias con semilla fija y la tabla reutiliza la lista sin `dict`, `set` ni `hash()`.
- Hay *type hints*, *docstrings* con `Args` y `Returns` y la búsqueda es iterativa.

## 4. Calidad del análisis de las gráficas (25 / 25)
**Lo que hizo bien:**
- Ambas gráficas existen, con título, ejes rotulados y leyenda; la primera tiene seis valores de `n` y la segunda seis valores de `α`.
- Calcula los factores de crecimiento (2,5 veces en `n` contra unas 2,67 en la lista; 1,02 en la tabla; unas 4,8 de `α = 1` a `α = 10`) y los contrasta con `Θ(n)`, `Θ(1)` y `Θ(1 + α)`.
- Sus cifras coinciden con lo que muestran las gráficas publicadas.

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- La carpeta está en `laboratorios/lab3-estructuras-datos/`, ubicación válida, con todos los archivos pedidos.
- El informe sigue el orden pedido, tiene su nombre, instrucciones de reproducción, enlaces al código y las gráficas visibles.
- Hay seis commits con mensajes descriptivos.

## ¿El código funciona?
Sí. Las pruebas pasan sin errores y `medicion.py` corre completo, mide ambas estructuras y genera las dos gráficas.
