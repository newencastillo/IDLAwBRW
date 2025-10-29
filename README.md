# Internal DLA with Branching Random Walk (IDLA-BRW)

Este proyecto implementa un modelo de **Internal Diffusion Limited Aggregation (IDLA)** combinado con **Branching Random Walk (BRW)**. El objetivo es simular la formación de clusters mediante caminatas aleatorias que pueden ramificarse, generando estructuras emergentes a partir de dinámicas locales.

## 🧠 Descripción General

En el modelo clásico de IDLA, partículas parten desde el origen (u otra fuente) y realizan un random walk hasta adherirse a un cluster.  
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


- Implementación base en **Python**.
- Simulación central de Random walk con posibilidad de branching.
- Clase de BRW con restricción de IDLA
- Simulación con animación

# Parte 2

Se implementará una *percolación* sobre la malla de $\mathbb{Z}^2$, esto es, quitar aristas para restringir el movimiento posible de las partículas.
La idea será eliminar aleatoriamente aristas en un campo finito (suficientemente grande para la simulación), con distintas probabilidades de eliminación para los "movimientos" verticales y los horizontales.

Es de esperar que de esta forma, el "cluster" que se formará asintóticamente será una elipse, y sus parámetros que lo definen estarán relacionados con la elección de las probabilidades para las aristas horizontales y verticales


Este readme fue creado (en parte) con inteligencia artificiel
