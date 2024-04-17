class Arbol:
    def __init__(self, POS, ACC_D, TIPO, DIRECCION, PADRE):
        self.POS = POS  # Es una tupla de coordenadas (x, y)
        self.ACC_D = ACC_D  # Una lista de valores booleanos (arriba, abajo, izquierda, derecha)
        self.TIPO = TIPO  # (INICIAL O FINAL)
        self.HIJOS = [] 
        self.PADRE = PADRE
        self.DIRECCION = DIRECCION
    
    def crear_hijo(self, POS, ACC_D, TIPO, DIRECCION, PADRE):
        nuevo_hijo = Arbol(POS, ACC_D, TIPO, DIRECCION, self)
        self.HIJOS.append(nuevo_hijo)

    def cambiar_nodo_actual(self, nueva_posicion):
        nodo_actual = self.buscar_nodo(self, nueva_posicion)
        if nodo_actual:
            return nodo_actual
        else:
            print("No se encontró un nodo con la posición especificada.")
            return None

    def buscar_nodo(self, nodo_actual, posicion_buscada):
        if nodo_actual.POS == posicion_buscada:
            return nodo_actual
        for hijo in nodo_actual.HIJOS:
            nodo_encontrado = self.buscar_nodo(hijo, posicion_buscada)
            if nodo_encontrado:
                return nodo_encontrado
        return None

    def eliminarDirRep(self):
        if self.PADRE is not None and self.DIRECCION == self.PADRE.DIRECCION:
            self.PADRE.HIJOS.remove(self)

    def crearNodosAncho(self, x, y):
        if self.ACC_D[0]: #CREAR NODO ARRIBA
            self.crear_hijo( (x, y-1), self.ACC_D, "D", "ARR", self)
        if self.ACC_D[1]: #CREAR NODO ABAJO
            self.crear_hijo( (x, y+1), self.ACC_D, "D", "ABA", self)
        if self.ACC_D[2]: #CREAR NODO DERECHA
            self.crear_hijo( (x-1, y), self.ACC_D, "D", "DER", self)
        if self.ACC_D[3]: #CREAR NODO IZQUIERDA
            self.crear_hijo( (x+1, y), self.ACC_D, "D", "IZQ", self)
        self.eliminarDirRep()

    def imprimir_arbol(self, nivel=0):
        if nivel == 0:
            print("Raíz:", self.POS)
        else:
            print(" " * nivel * 4 + "|___", self.POS, self.PADRE)
        for hijo in self.HIJOS:
            hijo.imprimir_arbol(nivel + 1)
    
    


