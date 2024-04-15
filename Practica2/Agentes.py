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

    
    def sensarArriba(self):
        y = self.PA[1]-1
        x = self.PA[0]-1
        if y == 0:
            self.CONOCIDO[y][x] = self.matriz[y][x]
            return False
        else:
            self.CONOCIDO[y][x] = self.matriz[y][x]
            self.CONOCIDO[y-1][x] = self.matriz[y-1][x]
            if self.CONOCIDO[y-1][x] == 0:
                return False
            else:
                return True
            
    def sensarAbajo(self):
        y = self.PA[1]-1
        x = self.PA[0]-1
        if y == len(self.CONOCIDO)-1:
            self.CONOCIDO[y][x] = self.matriz[y][x]
            return False
        else:
            self.CONOCIDO[y][x] = self.matriz[y][x]
            self.CONOCIDO[y+1][x] = self.matriz[y+1][x]
            if self.CONOCIDO[y+1][x] == 0:
                return False
            else:
                return True
            
    def sensarDerecha(self):
        y = self.PA[1]-1
        x = self.PA[0]-1
        if x == len(self.CONOCIDO[0])-1:
            self.CONOCIDO[y][x] = self.matriz[y][x]
            return False
        else:
            self.CONOCIDO[y][x] = self.matriz[y][x]
            self.CONOCIDO[y][x+1] = self.matriz[y][x+1]
            if self.CONOCIDO[y][x+1] == 0:
                return False
            else:
                return True
            
    def sensarIzquierda(self):
        y = self.PA[1]-1
        x = self.PA[0]-1
        if x == 0:
            self.CONOCIDO[y][x] = self.matriz[y][x]
            return False
        else:
            self.CONOCIDO[y][x] = self.matriz[y][x]
            self.CONOCIDO[y][x-1] = self.matriz[y][x-1]
            if self.CONOCIDO[y][x-1] == 0:
                return False
            else:
                return True
            
    def sensar4Dir(self):
        Des = []
        Des.append(self.sensarArriba()) #ARRIBA
        Des.append(self.sensarAbajo()) #ABAJO
        Des.append(self.sensarIzquierda()) #IZQUIERDA
        Des.append(self.sensarDerecha()) #DERECHA
        return Des
    
    def moverArriba(self):
        self.PA = [self.PA[0], self.PA[1]-1]
    def moverAbajo(self):
        self.PA = [self.PA[0], self.PA[1]+1]
    def moverDerecha(self):
        self.PA = [self.PA[0]+1, self.PA[1]]
    def moverIzquierda(self):
        self.PA = [self.PA[0]-1, self.PA[1]]
    
    def marcarMascara(self):
        y = self.PA[1]-1
        x = self.PA[0]-1
        #Obtener laterales
        if x > 0 and x < len(self.MASCARA[0])-1:
            if self.MASCARA[y][x-1] == 9:
                self.MASCARA[y][x-1] = self.CONOCIDO[y][x-1]
            if self.MASCARA[y][x+1] == 9:
                self.MASCARA[y][x+1] = self.CONOCIDO[y][x+1]
        #Obtener horizontales
        if y > 0 and y < len(self.MASCARA)-1:
            if self.MASCARA[y-1][x] == 9:
                self.MASCARA[y-1][x] = self.CONOCIDO[y-1][x]
            if self.MASCARA[y+1][x] == 9:
                self.MASCARA[y+1][x] = self.CONOCIDO[y+1][x]    
    
    
    def getLibres(self, valorLibs):
        count = 0
        y = self.PA[1]-1
        x = self.PA[0]-1
        #Obtener laterales
        if x >= 0 and x < len(self.MASCARA[0])-1:
            if self.CONOCIDO[y][x-1] == valorLibs:
                count = count +1
            if self.CONOCIDO[y][x+1] == valorLibs:
                count = count +1
        if x == len(self.MASCARA[0])-1:
            if self.CONOCIDO[y][x-1] == valorLibs:
                count = count +1
        #Obtener horizontales
        if y >= 0 and y < len(self.MASCARA)-1:
            if self.CONOCIDO[y-1][x] == valorLibs:
                count = count +1
            if self.CONOCIDO[y+1][x] == valorLibs:
                count = count +1 
        if y == len(self.MASCARA)-1:
            if self.CONOCIDO[y-1][x] == valorLibs:
                count = count +1
        return count
     
    def Manual(self):
        y = self.PA[1]-1
        x = self.PA[0]-1
        Des = self.sensar4Dir()
        if x == self.PI[0]-1 and y == self.PI[1]-1:
            if self.getLibres(1) > 1:
                if (x,y) not in self.LD:
                    self.LD.append((x, y))
        else:
            if (self.getLibres(1)-1) > 1:
                if (x,y) not in self.LD:
                    self.LD.append((x, y))
        if pygame.key.get_pressed()[pygame.K_UP]:  
            if Des[0]:
                self.moverArriba()
                self.MASCARA[y][x] = "V"
        if pygame.key.get_pressed()[pygame.K_DOWN]:  
            if Des[1]:
                self.moverAbajo()
                self.MASCARA[y][x] = "V"
        if pygame.key.get_pressed()[pygame.K_LEFT]:  
            if Des[2]:
                self.moverIzquierda()
                self.MASCARA[y][x] = "V"
        if pygame.key.get_pressed()[pygame.K_RIGHT]:  
            if Des[3]:
                self.moverDerecha()
                self.MASCARA[y][x] = "V" 
        if (x,y) not in self.LV:
            self.LV.append((x, y))
        self.marcarMascara()


        

        


    def AutomaticoProfundidad(self):
        y = self.PA[1]-1
        x = self.PA[0]-1
        ARBOL = TR.Arbol(self.PI, self.sensar4Dir() , "I", None, None)
        ESTADO = ""
        ARBOL.crearNodosAncho(self.PI[0],self.PI[1])
        if self.getLibres(1) >= 2:
            ESTADO = "DECIDIR"
        elif self.getLibres(1) == 1:
            ESTADO = "MOVER"
        if ESTADO == "MOVER":
            self.moverArriba()
        print(ESTADO)
        print(ARBOL)
        


        if (x,y) not in self.LV:
            self.LV.append((x, y))
        self.marcarMascara()
            

        
        
        