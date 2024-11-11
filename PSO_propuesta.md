**Torres Ochoa María Adelina**

# PSO en funciones continuas uni-objetivo

### Introducción

Propuesto en 1995 por James Kennedy y Russell Eberhart, el PSO (Optimización por Enjambre de Partículas, en inglés *Particle Swarm Optimization*) es un algoritmo de optimización inspirado en el comportamiento social de grupos de animales como bandadas de aves o bancos de peces. Kennedy y Eberhart observaron cómo estos grupos de organismos podían encontrar soluciones colectivas a problemas complejos, como la búsqueda de alimento, sin una jerarquía centralizada.

Al igual que otras técnicas de cómputo evolutivo, el PSO es un algoritmo de búsqueda basado en poblaciones y se inicializa con una población de soluciones aleatorias, llamadas partículas. La diferencia es que cada partícula en el PSO también está asociada con una velocidad: Las partículas vuelan a través del espacio de búsqueda velocidades que son ajustadas dinámicamente según su comportamiento histórico. Por lo tanto, las partículas tienen tendencia a volar hacia áreas de búsqueda cada vez mejores a lo largo del proceso de búsqueda.

### Alcance del proyecto

La meta es implementar en Python el PSO para implementar las funciones a minimizar Rastrigin, Rosenbrock, Griewank, Ackley y Sphere utilizando como criterio de paro un número de iteraciones máximas para poder posteriormente hacer una comparación lo más justa posible con las versiones Algoritmos Genéticos implementados en la Tarea 5 que dieron los mejores resultados para estas funciones de prueba (Reemplazo Elitista y Reemplazo de los Peores).

Las comparaciones se harán mediante gráficas de evolución de aptitud, tablas de datos estadísticos y boxplots para medir la robustez de los algoritmos.

Previa a la comparación de resultados se explicará qué es el PSO y algunas características que lo diferencian del AG que vimos en clase.

### Fuentes:

1. La implementación del PSO estará fuertemente basada en: https://github.com/alexxxroz/Medium/blob/main/PSO_explained.ipynb
2. También en: https://induraj2020.medium.com/implementing-particle-swarm-optimization-in-python-c59278bc5846
3. Inspiró la elección del tema (es el dueño del repositorio de **1.**): https://towardsdatascience.com/what-the-hell-is-particle-swarm-optimization-pso-simplest-explanation-in-python-be296fc3b1ab
4. Describe qué es el PSO, aplicaciones y parámetros: https://www.marksmannet.com/RobertMarks/Classes/ENGR5358/Papers/pso_bySHI.pdf
