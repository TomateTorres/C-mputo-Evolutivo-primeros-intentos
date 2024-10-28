En este boxplot observamos con más claridad aquello que notamos desde la tabla:

* El esquema de reemplazo generacional es el peor de todos porque presenta demasiada variabilidad en las soluciones encontradas (de hecho es el que provoca que nuestra escala en la vertical llegue hasta 800), presenta outliers en todas las funciones (con excepción de Rastrigin) y es muy poco robusto (pues todas las cajas son grandes).

* Elitismo y reemplazo de los peores quedan casi empatados pues los mejores valores alcanzados son prácticamente los mismos, presentan una cantidad similar de outliers y similar robustez.

El esquema de reemplazo de los peores pareciera ser la mejor opción porque la función Rosenbrock es la única en la que el esquema elitista presenta mayor robustez y menor dispersión en los outliers. 
