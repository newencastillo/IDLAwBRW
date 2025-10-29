import random as rd
import numpy as np

class BaseBRW:
    def __init__(self, p=0.8):
        self._particulas = []
        self.p = p

    @property
    def particulas(self):
        return np.asarray(self._particulas.copy())

    @particulas.setter
    def particulas(self, value):
        self._particulas = [list(p) for p in value]

    @property
    def vacio(self):
        return len(self._particulas) == 0

    def crear_particula(self, x=0, y=0):
        self._particulas.append([x, y])

    def mover(self):
        n = len(self._particulas)
        i = rd.randint(0, n-1)
        dx, dy = rd.choice([(-1, 0), (1, 0), (0, -1), (0, 1)])
        self._particulas[i][0] += dx
        self._particulas[i][1] += dy

    def aparear(self): # Añadir la capacidad de morir!
        n = len(self._particulas)
        i = rd.randint(0, n-1)
        if rd.random() < self.p: # Nos morimos
           self._particulas.pop(i) 
        else:               # else Nos duplicamos
            self._particulas.append(self._particulas[i].copy())


    # TODO IMplementar que mienstras mas particulas hay
    # más probable es que se aparear()
    def actualizar(self):
        if self.vacio:
            raise Exception("Se intenta actualizar un RW vacío") 
        self.mover()
        # Mover OR aparear es bueno porque 
        # las particulas se pueden morir con cualquiera de los dos
        if (not self.vacio) and rd.random() < self.p:
            self.aparear()


class BRW(BaseBRW):
    """ Branching Random Walk estándar """
    pass


class BRW_IDLA(BaseBRW):
    """ Branching RW + IDLA """
    def __init__(self, p=0.8):
        super().__init__(p)
        self._mapa = [[0, 0]]  # origen ocupado

    @property
    def mapa(self):
        return np.asarray(self._mapa.copy())

    @mapa.setter
    def mapa(self, value):
        self._mapa = [list(v) for v in value]

    
    def mover(self):
        n = len(self._particulas)
        i = rd.randint(0, n-1)
        dx, dy = rd.choice([(-1, 0), (1, 0), (0, -1), (0, 1)])
        x_new = self._particulas[i][0] + dx
        y_new = self._particulas[i][1] + dy

        if [x_new, y_new] not in self._mapa:
            self._mapa.append([x_new, y_new])
            self._particulas.pop(i)
        else:
            self._particulas[i] = [x_new, y_new]



class BRW_IDLA_PERC(BRW_IDLA):
    """ Branching RW + IDLA + Percolación """
    def __init__(self, p=0.8):
        super().__init__(p)
        self.perc = []

    def crear_perc(self, N, pvert, phor):
        # TODO: implementar grilla con percolación
        pass

    def mover(self):
        # TODO: incluir validación contra percolación
        super().mover()
