Para los Algoritmos Genéticos (con excepción del parámetro de reemplazo, que solamente aparece en el de reemplazo de los peores), se usaron los mismos parámetros para que la comparación fuera justa.

1. **Poblaciones (AG) = 70:** Se eligió una población de 70 individuos porque después de varios experimentos, concluimos que poblaciones de aproximadamente este tamaño permitían el suficiente número de individuos para tener (al menos de manera inicial) poblaciones diversas. Poblaciones más grandes no sólo aumentaban innecesariamente el costo de cómputo (pues no solían llegar a valores mejores), sino que además solían estancarse en soluciones peores.

2. **Dimensión 10:** Es la requerida.

3. **Bits en codificaciones binarias = 20 (por dimensión):** Para tener una representación binaria precisa (sobre todo en dimensiones grandes) 15-20 bits para cada entrada de los vectores nos pareció un número adecuado. Con 20 bits, cada dimensión puede representar $2^{20}$ valores distintos, lo que otorga una granularidad suficiente para que no haya pérdida de información significativa en los procesos de codificación en binario.

4. **Cortes en el operador de cruza (AG) = 15:** Mientras más cortes son considerados en el operador de reproducción de cruza, mayor es la probabilidad de que bits en posiciones alejadas puedan heredarse juntos. Dado que la idea es que los hijos que se generen después de la reproducción, sean parecidos a ambos padres, decidimos dar un número "grande" de cortes al operador para que ambos hijos reciban una cantidad más o menos equitativa de cada padre.

5. **Probabilidad de mutación (AG) = 0.1:** Las probabilidades de mutación dentro de los algoritmos genéticos suelen estar en [0.01, 0.1]. Dado que la idea de la mutación es permitir más variedad en la población y en consecuencia retrasar la convergencia, decidimos dar el mayor valor permitido.

6. **Fracción de reemplazo (en AG reemplazo de los peores) = 0.5:** Después de varios experimentos a priori, notamos que este esquema es más propenso a la convergencia prematura pero también permite llegar a mejores valores. Así que, decidimos permitir que sólo la mitad de los individuos (los peores) sean reemplazados cada generación para deshacernos rápidamente de valores muy malos, pero conservando los suficientes "valores buenos" con la esperanza de que al hacer la ruleta de la selección de padres, tuviéramos una distribución de pedazos un poco más equitativa de la que se tiene con el esquema de reemplazo elitista (donde rápidamente hay un sólo individuo al que se le es asignado un pedazo muy grande).

7. **Iteraciones (AG) = 1000:** De manera usual, la convergencia se ve alrededor de la iteración ~800, pero como llegamos a tener experimentos donde aún en generaciones avanzadas (arriba de 900) hubo mejora, decidimos dejar 1000 generaciones.

8. **Criterio de término (AG) = Generación máxima (1000):** Dado que nuestra implementación no permite manejo del tiempo de ejecución, decidimos dar como criterio de término un número máximo de 1000 generaciones (iteraciones).
