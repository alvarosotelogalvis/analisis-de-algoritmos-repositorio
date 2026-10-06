# Retroalimentación — Laboratorio evaluativo 01: Fundamentos, complejidad y recurrencias

**Estudiante:** Alvaro Sotelo · **Laboratorio:** Fundamentos, complejidad y recurrencias (Tamiza)
**Fecha límite:** 2026-10-04 23:59 · **Versión revisada:** commit `2a2cb45`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 17 / 25 |
| Calidad de la explicación teórica | 19 / 25 |
| Corrección de la implementación | 16 / 20 |
| Calidad del análisis de las gráficas | 11 / 20 |
| Documentación y organización del informe | 8 / 10 |
| **Total** | **71 / 100** |
| **Nota (0–5)** | **3.55** |

## 1. Corrección conceptual (17 / 25)
**Lo que hizo bien:**
- Explica que duplicar la velocidad solo cambia una constante y que el crecimiento cuadrático sigue igual, con un ejemplo numérico (60 veces más datos, 3600 veces más comparaciones).
- Nombra la ventana de 4 horas como la restricción que se incumple.
- Identifica perjuicios para el paciente y para el operador del centro de contacto, y dice quién paga cada uno.

**Lo que puede mejorar:**
- Distinga de forma explícita entre "da el resultado correcto" y "lo entrega a tiempo": hoy ambas ideas se confunden.
- El ejemplo del Excel no dice cuántos datos ni qué límite de tiempo se incumple. Sea concreto.
- En la Parte 2 faltan cifras o razonamiento sobre la energía (por ejemplo, horas de CPU por noche por año).
- Sobre la obligación de que el orden decida a quién se llama primero, falta decir que el orden debe ser siempre correcto, no solo rápido.

## 2. Calidad de la explicación teórica (19 / 25)
**Lo que hizo bien:**
- La recurrencia de merge sort está bien planteada y cada término se explica.
- La resolución por sustitución es completa: hipótesis, paso, constante y cota final `Θ(n log n)`.
- El análisis línea a línea de insertion sort y la tabla de complejidades son correctos.
- Escribió la predicción antes del experimento y la contrastó.

**Lo que puede mejorar:**
- En 3.1 los tres casos se definen de forma muy general. Diga sobre qué conjunto de entradas de tamaño n se toma el máximo, el mínimo y el promedio.
- La justificación de usar el peor caso es muy corta; explique qué pasaría con la ventana si solo se mirara el promedio.
- En el análisis línea a línea falta sumar los costos de cada línea para llegar al resultado.

## 3. Corrección de la implementación (16 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien (de mayor a menor), no cambian la lista original y cuentan solo comparaciones entre elementos. No usan `sorted()` ni `sort()`.
- Merge sort tiene su propia mezcla recursiva. Los generadores devuelven números distintos y usan semilla.

**Lo que puede mejorar:**
- Las funciones de `parte3_casos.py` y `parte4_complejidad.py` no tienen *type hints* completos y `main` no tiene *docstring*.
- Hay detalles de estilo (PEP 8): falta una línea en blanco entre funciones en `algoritmos.py`, e importaciones después de código.

## 4. Calidad del análisis de las gráficas (11 / 20)
**Lo que hizo bien:**
- La gráfica de la Parte 4 está completa (título, ejes, leyenda) y muestra bien la diferencia entre los dos algoritmos.
- Concluye con razón que merge sort conviene y lo relaciona con las complejidades calculadas.
- La estimación para 1.200.000 registros está bien razonada y declarada como estimación.
- Responde a la propuesta del servidor con datos de n=6400.

**Lo que puede mejorar:**
- Las gráficas `parte3_tiempo.png` y `parte3_comparaciones.png` salieron iguales: ambas muestran comparaciones. La de tiempo no muestra tiempo, y sus títulos solo dicen "tiempo" y "comparaciones". Hubo un error al llamar la función que dibuja (los argumentos van en otro orden). Revíselo.
- Por eso el análisis de 3.2 se apoya solo en comparaciones y no se ve el comportamiento del tiempo.
- La gráfica de tiempo no indica las unidades de forma completa en todos los casos; revise siempre rótulos y unidades.
- Falta discutir al menos una consideración distinta del tiempo en 4.3 (memoria extra de merge sort, estabilidad, mantenimiento). También falta explicar por qué merge sort no gana para tamaños muy pequeños.

## 5. Documentación y organización del informe (8 / 10)
**Lo que hizo bien:**
- El laboratorio está en la carpeta acordada (`laboratorios/lab1-fundamentos-complejidad-recurrencias/`) con todos los archivos pedidos.
- El informe sigue el orden de las partes, enlaza el código y muestra las gráficas con rutas que funcionan.
- Hay más de cinco commits descriptivos.

**Lo que puede mejorar:**
- Escriba su nombre completo, no solo "Alvaro Sotelo".
- Las instrucciones de activación del entorno solo sirven para Windows; indique también la forma para otros sistemas.

## ¿El código funciona?
Sí. Los dos algoritmos ordenan correctamente y los scripts corren sin errores. Sin embargo, la gráfica de tiempo de la Parte 3 sale con datos equivocados (comparaciones).

## Para el próximo laboratorio
- Después de generar una gráfica, ábrala y revise que muestre lo que dice el título.
- Defina cada concepto con precisión: sobre qué entradas y qué tamaño se toma cada caso.
- Dé números y límites concretos en los ejemplos y en el consumo de energía.
- Agregue *type hints* y *docstring* a todas las funciones, incluidas las de los scripts, y revise el estilo.
- Discuta siempre una consideración más allá del tiempo (memoria, estabilidad, mantenimiento).
