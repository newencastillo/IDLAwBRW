import BRW

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation




# SETUP
r_inicial = 5# NO ES UN RADIO
""" Se usa para establecer una cantidad inicial de partículas antes de la animación

"""
p_hor = 0.2
p_ver = 0.6
""" Probabilidades de descartar un camino horizontal o vertical en la percolacion"""

p = 0.5
""" Probabilidad de aparearse 
(no nos interesa esta parte en esta generación de momento)
"""


# Crear figura y ejes centrados en el origen
fig, ax = plt.subplots(figsize=(5, 5))
ax.set_xlim(-100,100)
ax.set_ylim(-100, 100)
ax.set_aspect('equal', 'box')
ax.axhline(0, color='gray', lw=1)
ax.axvline(0, color='gray', lw=1)

# Datos iniciales
newen = BRW.BRW_IDLA_PERC(p)
newen.crear_perc(500, p_ver, p_hor)
print("iniciando simulacion inicial!")
for i in range(r_inicial-1): # por el pi...
    if i % 100 == 0:
        print(f"{i} particulians introducidas al origen ")
    
    # creamos una particula y esperamos a q muera
    newen.crear_particula()
    while not newen.vacio: 
        newen.actualizar() 

# Creamos una más por motivos de animacion que si no se me rompe la webada de abajo
newen.crear_particula()

N = 100 # NADIE SABE PARA QUE ES ESTE N

# Preparar visual
cluster = ax.scatter(newen.mapa[:, 0], newen.mapa[:,1], s=20, color='red')
scat = ax.scatter(newen.particulas[:, 0], newen.particulas[:, 1], s=20, color='black', alpha=0.3)
texto = ax.text(0.02, 0.98, '', transform=ax.transAxes, verticalalignment='top')

"""
QUE se debe hacer, ? 😭
TODO
 - dibujars un ovalo del tamaño de acuerdo al N y phor y pvert :]
 - buscar diferencia entre ovalo y elipse
 -optimizacion facil: no revisar percolacion cuando se esta dentro del cluster?
 - esto cambia resultados?
 - puede que si pe

"""

# Función que actualiza el gráfico en cada frame
def update(frame):

    global newen # nuestra simulacion
    
    # Tamaño del cluster "|A(n)|"
    N = newen.N
    while newen.N == N and not newen.vacio:
        newen.actualizar() #ATENCION ESTO SE ROMPE CON P =! DE PYCLE 0

    newen.crear_particula()
    if newen.vacio: # no va a entrsar aqui nunka

        print("⚠️ Evento detectado, simulación pausada.")
        #input("Presiona Enter para continuar...")
        print("Reanudando...")
        newen.crear_particula()
        return cluster, scat

    x, y = zip(*newen.particulas)
    cluster.set_offsets(np.c_[newen.mapa[:,0], newen.mapa[:,1]])
    scat.set_offsets(np.c_[x, y])
    texto.set_text(f'Tamaño cluster: {N}\nDescarte vertical: {p_ver}\nDescarte horizontal:{p_hor}')

    return cluster, scat, texto

# Crear la animación
ani = FuncAnimation(fig, update, interval=1, blit=True)

plt.show()






