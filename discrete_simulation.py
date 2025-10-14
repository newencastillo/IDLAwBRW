import BRW

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# SETUP
r_inicial = 12 # con 6 ya a veces no funca
""" Se usa para establecer una cantidad inicial de partículas antes de la animación
CONTROLARSE: ESTO NO REPRESENTA PARA NADA NINGUN TIPO DE RADIO DEL CLUSTER
ES LA CANTIDAD DE PARTICULAS CON LAS QUE SE INICIA LA SIMULACION (SE SUELTAN DE A UNA)
R GRANDE -> SE PUEDE ALCANZAR ESTADO SUPER-CRITICO Y LA ANIMACIÓN NUNCA PARTE"""

p = 0.9
""" Probabilidad de aparearse (de no aparearse?)
igual es como mitosis pero waterer"""


# Crear figura y ejes centrados en el origen
fig, ax = plt.subplots(figsize=(5, 5))
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal', 'box')
ax.axhline(0, color='gray', lw=1)
ax.axvline(0, color='gray', lw=1)

# Datos iniciales
newen = BRW.BRW_IDLA(p)
for i in range(r_inicial-1): # por el pi...

    newen.crear_particula()
    while not newen.vacio: # ACTUALIZAMOS HASTA QUEDAR si particula 
        newen.actualizar() # movemos 

# Creamos una más por motivos de animacion que si no se me rompe la webada de abajo
newen.crear_particula()

N = 100 # NADIE SABE PARA QUE ES ESTE N

cluster = ax.scatter(newen.mapa[:, 0], newen.mapa[:,1], s=20, color='red')

scat = ax.scatter(newen.particulas[:, 0], newen.particulas[:, 1], s=20, color='black', alpha=0.3)

"""
QUE se debe hacer, ? 😭

"""

# Función que actualiza el gráfico en cada frame
def update(frame): # falta trabajar bastante esta parte
    # TO DOS: 
    # parar simulacion (caso sub critico) (averiguar intervencion del usuario para recontinuar(?))
    # simulacion GRANDE
    # ver cuna
    global newen
    # Movimiento aleatorio pequeño
    newen.actualizar()
    if len(newen.particulas) == 0:
        # sos un boludo, si mueree la simulacion el siguiente update pide actualizar particulas vacias tenes que hacer un break
        print("⚠️  Evento detectado, simulación pausada.")
        input("Presiona Enter para continuar...")
        print("Reanudando...")
        newen.crear_particula()
        return cluster, scat

    x, y = zip(*newen.particulas)
    cluster.set_offsets(np.c_[newen.mapa[:,0], newen.mapa[:,1]])
    scat.set_offsets(np.c_[x, y])

    return cluster, scat

# Crear la animación
ani = FuncAnimation(fig, update, interval=1, blit=True)

plt.show()






