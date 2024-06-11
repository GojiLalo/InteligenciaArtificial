import funciones as fun
from collections import Counter

class KNN:
    def __init__(self, entrada, n, modo):
        self.n = n
        self.modo = modo
        self.base = fun.leerArchivo("Base.txt", ",") #Fase de aprendizaje
        self.entrada = entrada
        self.distancias = {}
        self.clase = None

    def recuperacion(self):
        for i in self.base:
            llave, valor = fun.calcularDistancia(i, self.entrada, self.modo)
            self.distancias[llave] = valor
        self.distancias = dict(sorted(self.distancias.items())) #Ordenar distancias
        self.distancias = {k: self.distancias[k] for k in list(self.distancias)[:5]} #Regresar los K vecinos mas cercanos

        valores = self.distancias.values() # Extraer los valores del diccionario
        contador_valores = Counter(valores) # Contar la frecuencia de cada valor        
        self.clase, frecuencia = contador_valores.most_common(1)[0] # Identificar el valor con la mayor frecuencia
        #print(f"El valor más repetido es {self.clase} con una frecuencia de {frecuencia}.")
    

m1 = [5.4, 3.9, 1.7, 0.4]
m2 = [5.7, 2.8, 4.5, 1.3]
m3 = [7.6, 3, 6.6, 2.1]

prueba = KNN(m3, 1, "euclidiana")
prueba.recuperacion()
for clave, valor in prueba.distancias.items():
    print(f'{clave}: {valor}')
print(prueba.clase)