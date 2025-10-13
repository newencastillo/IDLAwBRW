
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

    @property  
    def vacio(self):
        ''' Retorna verdadero si no quedan partículas haciendo RW'''
        return len(self.particulas) == 0
    

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

    
## Vamos a crear otra clase copia de la anterior pero que implemente idla
# no vamos a usar herencia porque es demasiado engorroso en python
# ojala saber rust
# ojala pasr esto a julia

class BRW_IDLA:

    def __init__(self, p = 0.8):
        self._particulas = []
        self.p = p
        # Añadimos el conjunto de sitios ocupados uwu donde se puede mover
        self._mapa = []
        self._mapa.append([0, 0]) # Empezamos con el origen ocupado
        

    @property
    def mapa(self):
        return np.asarray(self._mapa.copy()) # 
    @mapa.setter
    def mapa(self, value):
        self._mapa = value

    @property  # FALTA IMPLEMENTAR EN LA CLASE PADRE
    def vacio(self):
        ''' Retorna verdadero si no quedan partículas haciendo RW'''
        return len(self.particulas) == 0

    
    @property
    def particulas(self):
        return np.asarray(self._particulas.copy())
    @particulas.setter
    def particulas(self, value):
        self._particulas = [list(p) for p in value]
    
    #def lista(self):
   #     return self.particulas.copy()

    def crear_particula(self): 
       ''' Crea una particula en el origen '''
       self._particulas.append([0, 0])

        
    def mover(self): 
        ''' Mueve una particula al azar en una direccion al azar.
        Si la particula sale del conjunto de sitios ocupados, se elimina
        y se actualiza el cluster
        '''
        # Eleccion aleatoria
        n = len(self._particulas)
        i = rd.randint(0, n-1)
        dir = rd.choice([(-1, 0), (1, 0), (0, -1), (0, 1)])

        # Mover la particula   

        x_new = self._particulas[i][0] + dir[0] 
        y_new = self._particulas[i][1] + dir[1]

        # chequeamos si nos salimos
        if [x_new, y_new] not in self._mapa: 
            self._mapa.append([x_new, y_new])
            self._particulas.pop(i)
        else: 
            # si no nos salimos, actualizamos la posicion
            self._particulas[i] = [x_new, y_new]


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

   