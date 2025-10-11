
# Que lata trabajar oop en python,
# pero es lo que hay.
import random as rd
import numpy as np

class BRW:
    def __init__(self, p = 0.8):
        self._particulas = []
        self.p = p

    @property
    def particulas(self):
        return np.asarray(self._particulas.copy())
    @particulas.setter
    def particulas(self, value):
        self._particulas = [list(p) for p in value]
    
    #def lista(self):
   #     return self.particulas.copy()

    def crear_particula(self, x: int = 0, y: int = 0):
       self._particulas.append([x, y])

    def mover(self): # no hy realmente metodos privados en python pero este deberia serlo
        n = len(self._particulas)
        # elegir una particula al azar
        i = rd.randint(0, n-1)
        # elegir una direccion al azar
        dir = rd.choice([(-1, 0), (1, 0), (0, -1), (0, 1)])
        # mover la particula   
        
        self._particulas[i] = [x+y for x, y in zip(self._particulas[i], dir)]
   

    def aparear(self):
        n = len(self.particulas)
        # escoger particula al azar
        i = rd.randint(0, n-1)
        # duplicarla
        self._particulas.append(self.particulas[i].copy())

    def actualizar(self):
        u = rd.random()
        if u < self.p:
        # mover una particula
            self.mover()
        else:
        # aparear una particula
            self.aparear()