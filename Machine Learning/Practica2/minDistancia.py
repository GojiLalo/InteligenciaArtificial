import funciones as fun
import numpy as np
from collections import Counter

class minimaDistancia:
    def __init__(self, entrada, modo):
        self.entrada = entrada
        self.modo = modo
        self.base = fun.leerArchivo("Base.txt", ",")
        self.etiquetas = []
        self.Promedios = {}
        self.clase = None

    def getIndice(self):
        #Obtener el indice donde se encuentra la etiqueta
        for i in range(0, len(self.base[0]), 1):
            if isinstance(self.base[0][i], str):
                return i

    def getPromedios(self):
        ind = self.getIndice()
        vector_Promedios = []        
        #Recorrer toda la base buscando todas las posibles etiquetas
        for i in self.base:
            if i[ind] not in self.etiquetas:
                self.etiquetas.append((i[ind]))
        #Obtener promedios
        for i in self.etiquetas:
            for j in self.base:
                if j[ind] == i:
                    vector_Promedios.append([valor for valor in j if not isinstance(valor, str)])
                    
            promedios = np.mean(vector_Promedios, axis=0)
            lista_promedios = promedios.tolist()
            self.Promedios.update({i:lista_promedios})
            vector_Promedios = []

    def clasificar(self):
        self.getPromedios()
        distancias = {}
        for clave, valor in self.Promedios.items():
            distancia, clase = fun.calcularDistancia(valor, self.entrada, "euclidiana")
            distancias.update({clave:distancia})
            
        distancias = dict(sorted(distancias.items(), key=lambda item: item[1])) #Ordenar
        primera_clave, primer_valor = next(iter(distancias.items())) #Primer elemento
        self.clase = primera_clave

def dMinimaVarias(distancia):
    Entradas = fun.leerArchivo("Entradas.txt", ",")
    with open('Resultados.txt', 'w') as f:
        pass
    for i in Entradas:
        with open('Resultados.txt', 'a') as f:
            Entrada = minimaDistancia(i, distancia)
            Entrada.clasificar()
            valores = f"{', '.join(map(str, i))}"
            f.write((f"{valores},{Entrada.clase}\n"))

