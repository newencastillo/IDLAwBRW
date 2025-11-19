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
        "Ecoge aleatoriamente una particula y la mueve"
        n = len(self._particulas)
        i = rd.randint(0, n-1)
        dx, dy = rd.choice([(-1, 0), (1, 0), (0, -1), (0, 1)])
        self._particulas[i][0] += dx
        self._particulas[i][1] += dy

    def mover(self, i):
        """Mueve aleatoriamente la i-esima particula"""
        try:
            dx, dy = rd.choice([(-1, 0), (1, 0), (0, -1), (0, 1)])
            self._particulas[i][0] += dx
            self._particulas[i][1] += dy
        except: Exception("Se intenta mover una particula que no existe")

    def aparear(self): # Añadir la capacidad de morir!
        n = len(self._particulas)
        i = rd.randint(0, n-1)
        if self.p == 0:
            self.mover(i)
            return
        if rd.uniform(0.0, 1.0) < self.p: # Nos morimos
           self._particulas.pop(i) 
        else:               # else Nos duplicamos y nos movemos
            self._particulas.append(self._particulas[i].copy())
            self.mover(i)
            self.mover(n) # ASi solo hay que modificar o implementar mover en las clases hijo


    # TODO IMplementar que mienstras mas particulas hay
    # más probable es que se aparear()
    def actualizar(self):
        if self.vacio:
            raise Exception("Se intenta actualizar un RW vacío") 
        self.aparear()
        
        """
        self.mover()
        # Mover OR aparear es bueno porque 
        # las particulas se pueden morir con cualquiera de los dos
        if (not self.vacio) and rd.random() < self.p:
            self.aparear()"""


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

    @property
    def N(self):
        '''Tamaño del cluster'''
        return len(self._mapa)

    
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

    def mover(self, i):
        """Mueve aleatoriamente la i-esima particula,
        considera la restricción del cluster """
        try:
            dx, dy = rd.choice([(-1, 0), (1, 0), (0, -1), (0, 1)])
            x_new = self._particulas[i][0] + dx
            y_new = self._particulas[i][1] + dy
            if [x_new, y_new] not in self._mapa:
                self._mapa.append([x_new, y_new])
                self._particulas.pop(i)
            else:
                self._particulas[i] = [x_new, y_new]
        except: Exception("Se intenta mover una particula que no existe")


class BRW_IDLA_PERC(BRW_IDLA):
    """ Branching RW + IDLA + Percolación """
    def __init__(self, p=0.8):
        super().__init__(p)
        self.perc = set()

    def crear_perc(self, N, pvert, phor):
        print("Generando Percolación")
        
        # SOLUCION
        # almacenar arista nomas como {[(1,2),(2,2)]} pero implementar funcion que haga el chequeo como (uv in E) or (vu in E)
       

        # la idea es partir desde (-N,-N) (hacemos la grilla de 2Nx2N)
        # y avanzamos calculando la "L" de aristas adyacentes que se quedan
        # LLLLL
        # LLLLL
        # LLLLL
        for i in range(-N,N):
            # Desde (-N,-N) a (N,-N)        # (-N,i) a (N,i)
            for j in range(-N,N):
                
                actual = (i,j)
                # quietar Arista Horizontal
                if rd.random() < phor: # quitamos la arista (añadirla a perc)
                    self.perc.add( ((i,j), (i,j+1)) )
                # quitar arista vertical
                if rd.random() < pvert:
                    self.perc.add( ((i,j), (i+1,j)) )                


        # self.validarpercolacion(🥱😪😴) NO QUIERO HACER ESTO Q LATAA
        pass

    def mover(self):
        '''Fuerza un movimiento válido '''
        # TODO: incluir validación contra percolación 
        # se forzará a que una particula 
        n = len(self._particulas)
        i = rd.randint(0, n-1)
        x = self._particulas[i][0]
        y = self._particulas[i][1]
        while True:
            dx, dy = rd.choice([(-1, 0), (1, 0), (0, -1), (0, 1)])
            x_new = x + dx
            y_new = y + dy

            if ((x_new,y_new), (x,y)) in self.perc or ((x,y), (x_new,y_new)) in self.perc: 
                continue
        
            if [x_new, y_new] not in self._mapa:
                self._mapa.append([x_new, y_new])
                self._particulas.pop(i)
                
            else:
                self._particulas[i] = [x_new, y_new]
            return
        
    def mover(self, i):
        """Mueve aleatoriamente la i-esima particula,
        considera la restricción del cluster
         y de la percolación generada """
        try:
            x = self._particulas[i][0]
            y = self._particulas[i][1]
            while True:
                # Proponemos movernos a un lugar
                dx, dy = rd.choice([(-1, 0), (1, 0), (0, -1), (0, 1)])
                x_new = x + dx
                y_new = y + dy

                # Vemos si este movimiento esta prohibido por la percolacion
                if ((x_new,y_new), (x,y)) in self.perc or ((x,y), (x_new,y_new)) in self.perc: 
                    continue
                
                # Si se permite el movimiento hacemos el movimiento estandar de IDLA
                if [x_new, y_new] not in self._mapa:
                    self._mapa.append([x_new, y_new])
                    self._particulas.pop(i)
                    
                else:
                    self._particulas[i] = [x_new, y_new]
                return
        except: Exception("Se intenta mover una particula que no existe")
