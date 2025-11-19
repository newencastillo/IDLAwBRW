'''Vamos a intentar estimar los parámetros a y b de la elipse
 generada por el crecimiento del cluster bajo percolaciones aleatorias'''

import BRW

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Ellipse

newen = BRW.BRW_IDLA_PERC(0.5)

# Fijar parametros pver y p hor
newen.crear_perc(100, 0.7, 0.4)

print(newen.validar_percolacion(100))
# Simular una cantidad grande