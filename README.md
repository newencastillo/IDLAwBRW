# Internal DLA with Branching Random Walk (IDLA-BRW)

Este proyecto implementa un modelo de **Internal Diffusion Limited Aggregation (IDLA)** combinado con **Branching Random Walk (BRW)**. El objetivo es simular la formación de clusters mediante caminatas aleatorias que pueden ramificarse, generando estructuras emergentes a partir de dinámicas locales.

## 🧠 Descripción General

El concepto de DLA es el siguiente, particulas hacen caminata aleatoria hasta que "tocan" una estructura y luego se vuelven parte de ella, en el caso de Internal DLA, estas partículas se introducen al origen, caminan por un "cluster" hasta salir de él, momento en que "mueren" y pasan a ser parte del cluster.

Esto se puede interpretar como una grilla de "hoyos", donde vamos introduciendo pelotas que solo pueden caminar sobre los hoyos tapados, cuando se salen de esta "superficie tapada", tapan un hoyo.

Introducimos una partícula al origen hasta que esta muera, momento en el que añadimos la siguiente y así sucesivamente, la pregunta que manejamos primeramente es ¿cómo crece este clúster?, ¿tiene forma regular?

Esta pregunta fue respondida y demostrada en 1970~ por [REF] y la respuesta ( para cualquier dimensión) es LA bola! Resultados que se pueden observar:

## BRanching random Walk 

Nuestro primer objetivo fue replicar una cierta variación a este concepto propuesta por Silvestri etal [REF2]
Alteramos la caminata aleatoria normal de esta simulación por BRW (Branching random walk). Esto es que nuestras partículas, ahora deciden con prob. $p$,  entre morir o duplicarse, con sus "hijas" cada una haciendo el siguiente paso del RW.

El resultado que se expone y que pretendemos replicar, es que con esta dinámica, no se mantiene el comprotamiento asintótico sobre la forma de "la mancha", si no más bien que se forman "cototitos". lo que comprobamos rápidamente

![](./animacion.gif)

## Lo percolación (Parte 2)
![](https://github.com/newencastillo/IDLAwBRW/blob/main/newen.gif)

Cambiamos nuestro mundo, nuestro espacio donde esta ocurriendo esta recreación

Se implementa una *percolación* sobre la malla de $\mathbb{Z}^2$, esto es, quitar aristas para restringir el movimiento posible de las partículas.
La idea será eliminar aleatoriamente aristas en un campo finito (suficientemente grande para la simulación), con distintas probabilidades de eliminación para los "movimientos" verticales y los horizontales.

Es de esperar que de esta forma, el "cluster" que se formará asintóticamente será una elipse, y sus parámetros que lo definen estarán relacionados con la elección de las probabilidades para las aristas horizontales y verticales

El objetivo del proyecto es:
- Explorar dinámicas de crecimiento en medios discretos.
- Analizar la estructura del cluster resultante.
- Experimentar con tasas de ramificación, tamaños de grilla y condiciones de ocupación.

## ✅ Estado Actual

- Implementación base en **Python**.
- Simulación central de Random walk con posibilidad de branching.
- Clase de BRW 
- + restricción de IDLA
- + restricción de Percolationi
- Simulación con animación
- + Herramienta para fabricar gifs



### notas propias

*Cómo implementar la percolación??*

Nuestra malla de $\mathbb{Z}^2$ la interpretamos como un grafo, donde números son adyacentes si estan a una distancia de 1.
Al querer implementar la percolación surgen entonces un par de problemas:

Queremos almacenar una gran cantidad de aristas, y que estas sean capaces de restringir el movimiento de el movimiento aleatorio


*El problema fundamental*

Solucionado e Implementado correctamente 😺
solo falta quitarle flojera a la fn de crear percolacion y VALIDARLA

Este readme fue creado (en parte) con inteligencia artificiel

## TODO s

- Hacer la aprox montecarlo para los valores de a y b y ver como se comparan
- hacer la presentación 
- 
- organizar bien el proyecto () (onda hacer un __main__)
