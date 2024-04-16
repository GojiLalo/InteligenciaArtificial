import pygame
import Arbol as TR

class AgenteL: 
    def __init__(self, matriz, PI, PF):
        self.matriz = matriz
        self.PI = (PI[0], PI[1])
        self.PF = (PF[0], PF[1])
        self.CONOCIDO = [[9] * len(matriz[0]) for i in range(len(matriz))]
        self.PA = PI
        self.MASCARA = [[9] * len(matriz[0]) for i in range(len(matriz))]
        self.LV = []
        self.LD = []

    
    def sensarArriba(self, Obstaculos):
        y = self.PA[1]-1
        x = self.PA[0]-1
        if y == 0:
            return False
        else:
            self.CONOCIDO[y][x] = self.matriz[y][x]
            self.CONOCIDO[y-1][x] = self.matriz[y-1][x]
            if self.CONOCIDO[y-1][x] in Obstaculos:
                return False
            else:
                return True
            
    def sensarAbajo(self, Obstaculos):
        y = self.PA[1]-1
        x = self.PA[0]-1
        if y == len(self.CONOCIDO)-1:
            self.CONOCIDO[y][x] = self.matriz[y][x]
            return False
        else:
            self.CONOCIDO[y][x] = self.matriz[y][x]
            self.CONOCIDO[y+1][x] = self.matriz[y+1][x]
            if self.CONOCIDO[y+1][x] in Obstaculos:
                return False
            else:
                return True
            
    def sensarDerecha(self, Obstaculos):
        y = self.PA[1]-1
        x = self.PA[0]-1
        if x == len(self.CONOCIDO[0])-1:
            self.CONOCIDO[y][x] = self.matriz[y][x]
            return False
        else:
            self.CONOCIDO[y][x] = self.matriz[y][x]
            self.CONOCIDO[y][x+1] = self.matriz[y][x+1]
            if self.CONOCIDO[y][x+1] in Obstaculos:
                return False
            else:
                return True
                     
    def sensarIzquierda(self, Obstaculos):
        y = self.PA[1]-1
        x = self.PA[0]-1
        if x == 0:
            self.CONOCIDO[y][x] = self.matriz[y][x]
            return False
        else:
            self.CONOCIDO[y][x] = self.matriz[y][x]
            self.CONOCIDO[y][x-1] = self.matriz[y][x-1]
            if self.CONOCIDO[y][x-1] in Obstaculos:
                return False
            else:
                return True
            
    def sensar4Dir(self, Obstaculos):
        Des = []
        y = self.PA[1]-1
        x = self.PA[0]-1
        if (x>=0 and x<=len(self.CONOCIDO[0])-1) and (y>=0 and y<=len(self.CONOCIDO)-1):
            Des.append(self.sensarArriba(Obstaculos)) #ARRIBA
            Des.append(self.sensarAbajo(Obstaculos)) #ABAJO
            Des.append(self.sensarIzquierda(Obstaculos)) #IZQUIERDA
            Des.append(self.sensarDerecha(Obstaculos)) #DERECHA
        return Des
    
    def moverArriba(self):
        self.PA = [self.PA[0], self.PA[1]-1]
    def moverAbajo(self):
        self.PA = [self.PA[0], self.PA[1]+1]
    def moverDerecha(self):
        self.PA = [self.PA[0]+1, self.PA[1]]
    def moverIzquierda(self):
        self.PA = [self.PA[0]-1, self.PA[1]]
    
    
    def IAMov(self, Obstaculos, DIR):       
        y = self.PA[1]-1
        x = self.PA[0]-1
        if DIR == "ARRIBA":
            if (y>=0):
                if (self.sensar4Dir(Obstaculos) == [True, False, False, False]) or (self.sensar4Dir(Obstaculos) == [True, True, False, False]):
                    self.moverArriba()
        if DIR == "ABAJO":  
             if (y<=len(self.CONOCIDO)-1):
                if (self.sensar4Dir(Obstaculos) == [False, True, False, False]) or (self.sensar4Dir(Obstaculos) == [True, True, False, False]):
                    self.moverAbajo()
        if DIR == "IZQUIERDA":
            if (x>0 and x<=len(self.CONOCIDO[0])-1) and (y>=0 and y<=len(self.CONOCIDO)-1):
                    if (self.sensar4Dir(Obstaculos) == [False, False, True, False]) or (self.sensar4Dir(Obstaculos) == [False, False, True, True]):
                        self.moverIzquierda()
        if DIR == "DERECHA":
             if (x>=0 and x<len(self.CONOCIDO[0])-1) and (y>=0 and y<=len(self.CONOCIDO)-1):
                if (self.sensar4Dir(Obstaculos) == [False, False, False, True]) or (self.sensar4Dir(Obstaculos) == [False, False, True, True]):
                    self.moverDerecha()

    def AutomaticoProfundidad(self):
        y = self.PA[1]-1
        x = self.PA[0]-1
        Obstaculos = [0]
        #ARBOL = TR.Arbol(self.PI, self.sensar4Dir(Obstaculos) , "I", None, None)
        ESTADO = "INICIO"
        self.IAMov(Obstaculos, "IZQUIERDA")

            #print(self.sensar4Dir(Obstaculos))
        if (x,y) not in self.LV:
            self.LV.append((x, y))
            #self.marcarMascara()
            

        
        
        