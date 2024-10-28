**Nota:** Para nosotros, aptitud=evaluación. De aquí que (ya que nuestras funciones son a minimizar) se busque minimizar las aptitudes.

## Comparaciones de aptitud AG:

En todas las funciones de prueba vemos un patrón similar:

1. **En el esquema de reemplazo elitista:** 

Las evaluaciones promedio mantienen valores relativamente altos y varían bastante generación a generación, lo que provoca que la gráfica de estos tenga un patrón caótico. La razón por la que tenemos este comportamiento es que, generación a generación conservamos solamente una solución (el que da el menor valor en la función de prueba) y reemplazamos a todos los demás individuos, permitiendo que en nuestras poblaciones haya valores altos. Esto es especialmente notorio en funciones que tienen intervalos de búsqueda grades (como Griewank) o más complicadas de minimizar (como Rosenbrock).

La mejor evaluación, por otro lado, baja rápidamente hacia valores bajos y no es tan frecuente la convergencia prematura (aunque cuando esta se da, ocurre desde iteraciones muy tempranas y nos quedamos atorados en valores malos).

2. **En el esquema de reemplazo generacional:** 

En este esquema, generación a generación estamos haciendo prácticamente búsqueda aleatoria. Esto porque aunque los hijos al final de cada generación provienen, en su gran mayoría, de padres con los valores que más minimizan a la función, como no permitimos que ningún individuo sobreviva más de una generación, difícilmente (de hecho esto nunca pasa) aparecerá un individuo que domine a la ruleta en la selección de padres. 

Así que, en la población se mantienen tanto individuos con valores bajos como altos en las funciones a minimizar. Lo que provoca que las gráficas de las evaluaciones promedio y las de la mejor evaluación presenten patrones caóticos y en ninguna haya una tendencia al decrecimiento.

3. **En el esquema de reemplazo de los peores:**

Generación a generación, conservamos a la mejor mitad de los individuos. Esto provoca que tanto las evaluaciones promedio, como las mejores evaluaciones decrezcan rápidamente.

A diferencia del esquema de reemplazo elitista, aquí las evaluaciones promedio también decrecen y siempre tenemos convergencia prematura. Lo anterior es porque a diferencia del reemplazo elitista, como conservamos generación a generación una proporción más grande de la población (la mitad, en vez de un solo individuo) en las primeras iteraciones podemos bajar mucho más rápido y usualmente hacia valores mejores (pues en principio, la ruleta de selección de padres tiene una partición un poco más equitativa y no sesgada hacia un solo individuo); pero una vez que se encuentra uno o más óptimos locales (en los casos donde no se llega al óptimo global), es muy difícil seguir bajando porque generación a generación sólo podemos mejorar a la mitad de los individuos.

## Comparaciones de diversidad y entropía AG:

**Tanto para el esquema de reemplazo elitista como el generacional**, las gráficas de diversidad y entropía presentan patrones similares en las distintas funciones de prueba: 

* La diversidad promedio baja rápidamente en las primeras iteraciones y se queda "oscilando" en un rango pequeño. Esto nos dice que desde las primeras iteraciones, nuestra población llega a un estado donde los individuos son parecidos, pero no llegamos a tener clones (pues seguimos teniendo valores positivos en la escala de diversidad).

* La diversidad mínima refleja lo anterior porque, aunque la curva llega a valores menores que la del promedio (lo cual tiene sentido, porque diversidad mínima mide la distancia de cada individuo a su vecino más cercano), igual ésta se queda "oscilando" en un valor distinto del cero.

* La gráfica de la entropía es prácticamente la misma que la de la diversidad promedio (salvo un re-escalamiento). Esto tiene sentido porque la entropía mide "el promedio del desorden" en cada uno de los genes (las entradas de los individuos en su codificación binaria) a nivel poblacional; así que a mayor diversidad promedio en nuestra población, mayor es la entropía (pues hay más variabilidad en los genes) y a menor diversidad promedio en nuestra población, menor es la entropía (pues hay más repetición en los genes).

Así, que aunque en el reemplazo elitista llegamos a valores mucho mejores que en el generacional, terminamos con poblaciones que a grandes rasgos tienen la misma variabilidad.

En el caso del **esquema de reemplazo de los peores**:

* Por la razón ya expuesta arriba, las gráficas de entropía y diversidad promedio, son en esencia las mismas (salvo un re-escalamiento).

* Las gráficas de diversidad promedio y mínima muestran un muy rápido decrecimiento hacia el 0 y prácticamente se estancan en un valor muy cercano a él. Esto es porque en este esquema de reemplazo llegamos muy rápidamente a óptimos locales (o al global en ocasiones) y una vez que esto pasa ya es muy difícil modificar a nuestra población.
