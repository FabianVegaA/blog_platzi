# Qué son los Greedy Algorithms

Respondamos la primera pregunta:

Un greedy algorithm o algoritmo voraz, es un paradigma para construir algoritmos que construyen una solucion poco a poco, buscando el siguiente paso que maximice el beneficio. Es decir, la eleccion local optima que conduce a una globlal. Esto a costa de nunca reconsiderar elecciones previas.


Un ejemplo interesante es el problema de asignación de tareas, que se puede resolver con greedy.

Supongamos que tenemos una lista de tareas, y que cada tarea tiene un inicio y una duración, y la condición que no deben solaparse.

Para resolver esto podemos partir con varias ideas:

- **Idea 1**: Elegir siempre la tarea más corta que no teng acpnflicto con las ya programadas.

Pero eso tiene algunos problemas, ejemplo:
<!-- ![]() TODO - Agregar imagen -->

<!-- Empezando con p 2 , efectuamos 1 tarea. Con p 1 completamos 2.Luego de comenzada la primera y antes que ésta termine, y a su vez comienza la tercera antes
que termine la segunda, pero luego del fin de la primera. Usando este criterio elegiríamos la
tarea p 2 , dejando fuera (por conflictos) a p 1 y p 3 . La solución óptima es elegir p 1 , p 3 . Por lo
tanto, esta sugerencia no siempre da un óptimo. -->

- **Idea 2**: Elegir la tarea con inicio más temprano que no tenga conflicto con las ya programadas.
  
<!-- Empezando con p 1 , completa 1 tarea. Con p 2 y p 3 hacemos 2.
que traslapa con varias tareas cortas independientes. elegiríamos la tarea p 1 , sin embargo, el
óptimo es p 2 , p 3 . Nuevamente, esta sugerencia no siempre da un óptimo. -->

- **Idea 3**: Marcar cada proyecto con el número de proyectos con que entra en conflicto, programar en orden creciente de conflictos.

