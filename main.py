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
newen = BRW.BRW(p = 0.5)
newen.crear_particula()
newen.crear_particula()

N = 100
for _ in range(5):
    newen.actualizar()

print(newen.particulas)

scat = ax.scatter(newen.particulas[:][0], newen.particulas[:][1], s=20, color='black', alpha=0.3)


# Función que actualiza el gráfico en cada frame
def update(frame):
    global newen
    # Movimiento aleatorio pequeño
    newen.actualizar()
    x, y = zip(*newen.particulas)
    scat.set_offsets(np.c_[x, y])
    return scat,

# Crear la animación
ani = FuncAnimation(fig, update, frames=200, interval=30, blit=True)

plt.show()



