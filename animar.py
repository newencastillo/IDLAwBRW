import BRW

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Ellipse




def pedir_float(msg):
    while True:
        try:
            x = float(input(msg))
            if x < 0 or x > 1:
                raise ValueError("Input debe estar entre 0 y 1")
            return x
        except ValueError:
            print("Entrada inválida, intenta nuevamente.")
def pedir_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Entrada inválida, intenta nuevamente.")
# SETUP

N_inicial = pedir_int("Ingresa tamaño inicial del cluster: ") # NO ES UN RADIO
""" Se usa para establecer una cantidad inicial de partículas antes de la animación

"""
p = pedir_float("Ingresa prob. de apareamiento: ")
""" Probabilidad de aparearse 
"""

p_hor = pedir_float("Ingresa prob. descarte horizontal: ")


p_ver = pedir_float("Ingresa prob. descarte vertical: ")

""" Probabilidades de descartar un camino horizontal o vertical en la percolacion"""

#a, b =  (1-p_ver), (1-p_hor)


# esto no a, b =  1/(1-p_hor) , 1/(1-p_ver)
#a, b = (1-p_ver)/( p_ver+ p_hor), (1-p_hor)/( p_ver+ p_hor) # esto un poco para valores bajos de ps
C = 1
if p_ver + p_hor == 0:
    a, b= 1, 1
else:
    a, b = C*(1-p_ver)/( p_ver+ p_hor), C*(1-p_hor)/( p_ver+ p_hor) 
'''Conjetura sobre como se comporta el crecimiento del cluster como una ellipse,'''

# Datos iniciales
newen = BRW.BRW_IDLA_PERC(p)
newen.crear_perc(500, p_ver, p_hor)

print("Iniciando simulacion inicial!")
while newen.N < N_inicial:
    # creamos una particula y esperamos a q muera
    if newen.N % 1000 == 0:
        print(newen.N, "particulas en el cluster")
    newen.crear_particula()
    while not newen.vacio and newen.N < N_inicial: 
        newen.actualizar()



# Creamos una más por motivos de animacion que si no se me rompe la webada de abajo
if newen.vacio:
    newen.crear_particula()

#N = 100 # NADIE SABE PARA QUE ES ESTE N


# Crear figura y ejes centrados en el origen
fig, ax = plt.subplots(figsize=(5, 5))
ax.set_xlim(-100,100)
ax.set_ylim(-100, 100)
ax.set_aspect('equal', 'box')
ax.axhline(0, color='gray', lw=1)
ax.axvline(0, color='gray', lw=1)

# Preparar visual
ellipse = Ellipse((0, 0), width=2*a, height=2*b, fill=False, color='blue')
ax.add_patch(ellipse)
cluster = ax.scatter(newen.mapa[:, 0], newen.mapa[:,1], s=20, color='red')
scat = ax.scatter(newen.particulas[:, 0], newen.particulas[:, 1], s=20, color='black', alpha=0.3)
texto = ax.text(0.02, 0.98, '', transform=ax.transAxes, verticalalignment='top')

"""
QUE se debe hacer, ? 😭
TODO
 - IMPLEMENTAR VALIDAR PERCOLACION
"""

# Función que actualiza el gráfico en cada frame
def update(frame):

    global newen # nuestra simulacion
    
    # Tamaño del cluster "|A(n)|"
    N = newen.N
    # Movemos hasta actualizar el cluster
    while newen.N == N and not newen.vacio:
        newen.actualizar() #ATENCION ESTO SE ROMPE CON P =! DE PYCLE 0

    if newen.vacio:
        newen.crear_particula()

    # Calcular tamaño del     
    scale =  (np.pi/0.69)**0.5 * (newen.N / (np.pi* a*b))**0.5 


    # Actualizar ovalo
    ellipse.width = a*scale
    ellipse.height = b*scale



    x, y = zip(*newen.particulas)
    cluster.set_offsets(np.c_[newen.mapa[:,0], newen.mapa[:,1]])
    scat.set_offsets(np.c_[x, y])
    texto.set_text(f'Tamaño cluster: {N}\n $p$ branch = {p}\n($p_h$,  $p_v$) : ({p_ver}, {p_hor})\nPartículas activas: {len(newen.particulas)}')

    return cluster, scat, texto, ellipse

# Crear la animación
ani = FuncAnimation(fig, update, interval=1, blit=True)

plt.show()






