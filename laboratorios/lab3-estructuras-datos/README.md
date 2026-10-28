# Laboratorio 3 — Estructuras de datos: lista enlazada vs. tabla hash

Autor: Alvaro de Jesús Sotelo Galvis — Análisis de Algoritmos, ITM.

## Instrucciones de reproducción

1. Crear (solo la primera vez) y activar el entorno virtual desde la raíz del repositorio:
   - Windows: python -m venv venv, luego venv\Scripts\activate
   - macOS / Linux: python3 -m venv venv, luego source venv/bin/activate

2. Instalar las dependencias con pip install -r requirements.txt.

3. Desde esta carpeta (laboratorios/lab3-estructuras-datos/), ejecutar:
   - python pruebas.py, que verifica la lista enlazada y la tabla hash.
   - python medicion.py, que corre los dos experimentos, imprime las tablas de tiempos y genera
     las dos gráficas en graficas/.

---

## Parte 1 — Implementar y verificar las dos estructuras

Código: [estructuras.py](estructuras.py) · [pruebas.py](pruebas.py)

En esta primera parte implementé una lista enlazada en la que cada nodo almacena la guía, su estado y la referencia al siguiente nodo. La inserción se realiza al inicio, haciendo que el nuevo nodo apunte a la cabeza anterior y pase a ser la nueva cabeza, por lo que esta operación tiene una complejidad Θ(1). Para la búsqueda utilicé un ciclo while que recorre los nodos hasta encontrar la guía o llegar al final, retornando None cuando no existe; preferí hacerlo de forma iterativa para evitar problemas con el límite de recursión de Python al manejar una gran cantidad de nodos. También implementé una tabla hash mediante encadenamiento, donde cada posición contiene una lista enlazada y la casilla correspondiente se calcula utilizando el método de división h(k) = k mod m. Tanto al insertar como al buscar, la tabla trabaja únicamente sobre la lista enlazada de la casilla calculada, sin tener que recorrer las demás. Para comprobar el funcionamiento realicé pruebas con búsquedas exitosas y fallidas, estructuras vacías y una colisión forzada con m = 7, donde las guías 10, 24 y 17 quedan en la casilla 3; posteriormente verifiqué que las tres pudieran encontrarse, que dicha casilla tuviera una longitud de 3 y que el factor de carga fuera 3/7. Además, realicé pruebas con 20 colecciones aleatorias usando una semilla fija de 2026, comprobando que para las guías existentes ambas estructuras devolvieran el mismo estado y que para las guías inexistentes ambas devolvieran None. Toda la implementación se realizó sin utilizar dict, set ni la función hash() de Python.

## Parte 2 — Medir y graficar

Código: [medicion.py](medicion.py)

En la segunda parte realicé diferentes mediciones para comparar el rendimiento de la lista enlazada y la tabla hash. Para esto generé guías distintas de 10 dígitos utilizando una semilla fija de 2026, asegurando que ambas estructuras trabajaran con los mismos datos. También generé 200 guías inexistentes utilizando una semilla 7, con el fin de medir el comportamiento de las búsquedas cuando el elemento no se encuentra. En el experimento A trabajé con valores de n de 100, 500, 1.000, 5.000, 20.000 y 50.000, mientras que el tamaño m de la tabla se definió como el número primo más cercano a n/2, manteniendo un factor de carga cercano a 2. Para el experimento B mantuve fijo n = 20.000 y varié el factor de carga con valores de 0,25, 0,5, 1, 2, 4 y 10, calculando m como el primo más cercano a n/α. Los tiempos se midieron con time.perf_counter(), teniendo en cuenta únicamente las búsquedas y dejando por fuera la construcción de las estructuras y la generación de los datos. El tiempo promedio por búsqueda se obtuvo dividiendo el tiempo total entre las 200 búsquedas realizadas. Para disminuir el efecto del ruido en las mediciones, repetí cada prueba 3 veces para la lista enlazada y 51 veces para la tabla hash, tomando como resultado el menor tiempo obtenido. Antes de cada medición también verifiqué con 100 guías existentes que ambas estructuras devolvieran correctamente el estado esperado. Finalmente, los resultados del experimento A se expresaron en segundos y los del experimento B en microsegundos.

### Experimento A — Lista enlazada frente a tabla hash

![Tiempo medio por búsqueda vs. número de guías](graficas/lista_vs_tabla.png)

| n | m | α | Lista (s) | Tabla (s) |
|---|---|---|---|---|
| 100 | 53 | 1.89 | 3.364e-06 | 2.440e-07 |
| 500 | 251 | 1.99 | 1.817e-05 | 2.280e-07 |
| 1000 | 499 | 2.00 | 4.573e-05 | 3.130e-07 |
| 5000 | 2503 | 2.00 | 2.416e-04 | 2.835e-07 |
| 20000 | 10007 | 2.00 | 1.063e-03 | 2.700e-07 |
| 50000 | 24989 | 2.00 | 2.834e-03 | 2.765e-07 |

### Experimento B — Efecto del factor de carga (n = 20000)

![Tiempo medio por búsqueda vs. factor de carga](graficas/tiempo_vs_alfa.png)

| α | m | Tabla (µs) |
|---|---|---|
| 0.25 | 79999 | 0.224 |
| 0.50 | 40009 | 0.217 |
| 1.00 | 19997 | 0.229 |
| 2.00 | 10007 | 0.306 |
| 4.00 | 4999 | 0.430 |
| 10.01 | 1999 | 1.105 |

---

## Parte 3 — Análisis

### 1. Costo teórico

En una lista enlazada, buscar una guía que no existe obliga a recorrer los `n` nodos porque solo al llegar al final se puede confirmar que no está, por lo que se realizan `n` comparaciones y su costo es Θ(n). En la tabla hash primero se calcula la casilla, con costo Θ(1), y después se recorre únicamente la lista de esa posición, que en promedio contiene `α = n/m` elementos. Por esto, el costo esperado es Θ(1 + α), suponiendo un hash uniforme simple, donde cada guía tiene la misma probabilidad de caer en cualquier casilla. En el peor caso, si todas las guías cayeran en una sola casilla, habría que recorrer `n` elementos y la tabla terminaría teniendo un comportamiento Θ(n).

### 2. Lo medido contra lo esperado

Los resultados obtenidos se acercan a lo esperado teóricamente. En la lista, al pasar de 20.000 a 50.000 guías, `n` aumentó 2,5 veces y el tiempo pasó de `1,063e-03` a `2,834e-03` segundos, es decir, aumentó aproximadamente 2,67 veces. Esto muestra un crecimiento cercano al lineal esperado de Θ(n). Para la tabla hash, en el mismo tramo el tiempo pasó de `2,700e-07` a `2,765e-07` segundos, apenas 1,02 veces, lo que concuerda con Θ(1) en este experimento porque `α` se mantuvo cercano a 2. Al variar el factor de carga también se observa su efecto: desde `α = 1` hasta `α = 10`, el tiempo aumenta de `0,229` a `1,105 µs`, unas 4,8 veces, mientras que Θ(1 + α) permite esperar una relación de `(1+10)/(1+1) = 5,5`. Entre `α = 0,25` y `α = 1`, en cambio, el tiempo casi no cambia, pasando de `0,224` a `0,229 µs`. Esto muestra que existe un costo mínimo aunque haya pocas colisiones, principalmente por calcular el hash y acceder a la casilla.

### 3. Las colisiones

Una colisión ocurre cuando dos guías diferentes terminan en la misma casilla. Aunque `m` sea mayor que `n`, estas siguen siendo posibles porque existen muchas más guías de 10 dígitos que casillas disponibles y, de forma similar a la paradoja del cumpleaños, pueden aparecer coincidencias incluso sin llenar la tabla. En mi implementación utilicé encadenamiento, donde cada casilla contiene una lista enlazada. Esto permite trabajar incluso con `α > 1`, aunque requiere memoria adicional y recorrer la cadena cuando existen varias colisiones. Otra alternativa es el direccionamiento abierto, que busca otra casilla disponible, aunque necesita mantener `α < 1` y pierde rendimiento cuando se acerca a ese límite. Por ejemplo, con `m = 7`, las guías `10`, `24` y `17` tienen residuo 3. Con encadenamiento quedan juntas en la lista de la casilla 3, mientras que con sondeo lineal podrían ocupar las posiciones 3, 4 y 5.

### 4. Tabla hash o árbol de búsqueda

La tabla hash es adecuada para consultar una guía específica, pero no para búsquedas por rangos porque distribuye los datos sin conservar su orden. Para encontrar las guías entre dos valores sería necesario revisar los `n` elementos, con costo Θ(n). Un árbol de búsqueda sí conserva el orden, permitiendo llegar al valor inicial y recorrer únicamente hasta el final del rango, con costo aproximado `O(h + k)`, donde `h` es la altura y `k` la cantidad de elementos encontrados. El problema aparece si llegan 400.000 guías ordenadas a un árbol no balanceado: cada nueva guía podría quedar a la derecha de la anterior, formando prácticamente una cadena. En ese caso, buscar un valor inexistente mayor que todos podría requerir cerca de 400.000 comparaciones. En un árbol balanceado, `log₂(400.000) ≈ 18,6`, por lo que serían aproximadamente 19 niveles y alrededor de 19 comparaciones, una diferencia considerable frente al caso degenerado.

### 5. Concepto para la jefa de operaciones

Para el caso de Rutas del Caribe utilizaría una combinación de estructuras: una tabla hash para consultar rápidamente una guía específica y un árbol balanceado para el monitoreo y las búsquedas por rangos. El costo de esta solución es utilizar más memoria y realizar cada inserción en las dos estructuras. Si el sistema llegara a 5.000.000 de guías, puedo hacer una estimación a partir de los resultados obtenidos. La lista tardó `2,834e-03 s` con 50.000 elementos y las pruebas mostraron un crecimiento cercano al lineal, ya que al aumentar 2,5 veces los datos el tiempo aumentó 2,67 veces. Como 5.000.000 representa 100 veces más elementos que 50.000, estimo un tiempo cercano a `0,28 s` por búsqueda en la lista. Para la tabla, si se aumenta `m` para mantener `α ≈ 2`, estimo que la búsqueda permanecería alrededor de `0,28 µs`, similar a lo medido. Las dos cifras son estimaciones y en un escenario con millones de registros pueden variar por factores como memoria y caché. Aun así, la diferencia permite ver por qué una lista podría generar esperas cuando se realizan muchas consultas, mientras que la tabla hash resulta más apropiada para consultas puntuales.