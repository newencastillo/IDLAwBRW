# Internal DLA with Branching Random Walk (IDLA-BRW)

Este proyecto implementa un modelo de **Internal Diffusion Limited Aggregation (IDLA)** combinado con **Branching Random Walk (BRW)**. El objetivo es simular la formación de clusters mediante caminatas aleatorias que pueden ramificarse, generando estructuras emergentes a partir de dinámicas locales.

## 🧠 Descripción General

$\int_a^b e^{\larrow \lambda \dot{newen}}$

En el modelo clásico de IDLA, partículas parten desde el origen y realizan un random walk hasta adherirse a un cluster. 
En esta versión extendida, se incorpora *branching*, permitiendo que ciertas partículas generen nuevas caminatas durante su evolución.

El objetivo del proyecto es:
- Explorar dinámicas de crecimiento en medios discretos.
- Analizar la estructura del cluster resultante.
- Experimentar con tasas de ramificación, tamaños de grilla y condiciones de ocupación.

## ✅ Estado Actual

### Primeros Resultados

A continuación se presenta una pequeña tabla-registro de la cantidad de particulas necesarias para alcanzar un estado "supercritico" aproximado (cuando la población de partículas se sostiene a si misma), junto con la "probabilidad de apareamiento" para algunas simulaciones realizadas.


| N | p |
|---|---|
| 19  | 0.90|
| 23  | 0.90|
| 14  | 0.85|
| 12  | 0.85|
| 14  | 0.85|
| 9  | 0.80|
| 9  | 0.80|
| 5 | 0.80|

**OJO** estos primeros resultados estan MALOS, la implementación no era correcta, ya que el branching no tenía implementada la probabilidad de "morir"


- Implementación base en **Python**.
- Simulación central de Random walk con posibilidad de branching.
- Clase de BRW con restricción de IDLA
- Simulación con animación

# Parte 2

Se implementará una *percolación* sobre la malla de $\mathbb{Z}^2$, esto es, quitar aristas para restringir el movimiento posible de las partículas.
La idea será eliminar aleatoriamente aristas en un campo finito (suficientemente grande para la simulación), con distintas probabilidades de eliminación para los "movimientos" verticales y los horizontales.

Es de esperar que de esta forma, el "cluster" que se formará asintóticamente será una elipse, y sus parámetros que lo definen estarán relacionados con la elección de las probabilidades para las aristas horizontales y verticales



### notas propias

*Cómo implementar la percolación??*

Nuestra malla de $\mathbb{Z}^2$ la interpretamos como un grafo, donde números son adyacentes si estan a una distancia de 1.
Al querer implementar la percolación surgen entonces un par de problemas:

Queremos almacenar una gran cantidad de aristas, y que estas sean capaces de restringir el movimiento de el movimiento aleatorio


*El problema fundamental*

Que debo hacer para implementar el brw realmente!!!, -> google
Ok, toca reimplementar el random wal, en CADA TIEMPO la particula se MUERE o se SEPARA ubicando a sus hijos en un lugar aleatorios
Puede que no haya que modificar muchas cosas

Este readme fue creado (en parte) con inteligencia artificiel

## TODO s

- Actualizar readme y borrar la copia
- organizar bien el proyecto (onda hacer un __main__)
- arreglar la wea del ovalo yaque chucha