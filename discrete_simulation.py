import BRW

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Crear figura y ejes centrados en el origen
fig, ax = plt.subplots(figsize=(5, 5))
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal', 'box')
ax.axhline(0, color='gray', lw=1)
ax.axvline(0, color='gray', lw=1)

# Datos iniciales
newen = BRW.BRW_IDLA(p = 0.4)
newen.crear_particula()

N = 2
cluster = ax.scatter(newen.mapa[:, 0], newen.mapa[:,1], s=20, color='red')

scat = ax.scatter(newen.particulas[:, 0], newen.particulas[:, 1], s=20, color='black', alpha=0.3)



# Función que actualiza el gráfico en cada frame
def update(frame): # falta trabajar bastante esta parte
    # TO DOS: 
    # parar simulacion (caso sub critico) (averiguar intervencion del usuario para recontinuar(?))
    # simulacion GRANDE
    # ver cuna
    global newen
    # Movimiento aleatorio pequeño
    for _ in range(N):
        if len(newen.particulas) == 0:
            return cluster, scat
        newen.actualizar()
    x, y = zip(*newen.particulas)
    cluster.set_offsets(np.c_[newen.mapa[:,0], newen.mapa[:,1]])
    scat.set_offsets(np.c_[x, y])

    return cluster, scat

# Crear la animación
ani = FuncAnimation(fig, update, frames=1000, interval=1, blit=True)

plt.show()






