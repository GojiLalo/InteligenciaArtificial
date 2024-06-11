import csv
import numpy as np

def leerArchivo(nombre_archivo, delimitador):
    matriz = []
    try:
        with open(nombre_archivo, mode='r', newline='', encoding='utf-8') as archivo:
            lector = csv.reader(archivo, delimiter=delimitador)
            for fila in lector:
                fila_converted = []
                for elemento in fila:
                    try:
                        # Intenta convertir el elemento a int
                        elemento = int(elemento)
                    except ValueError:
                        try:
                            # Intenta convertir el elemento a float
                            elemento = float(elemento)
                        except ValueError:
                            if elemento.lower() == 'true':
                                elemento = True
                            elif elemento.lower() == 'false':
                                elemento = False
                    fila_converted.append(elemento)
                matriz.append(fila_converted)
        
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no se encuentra.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
    return matriz


def TipoAtributo(lista):
    TIPOS = {
        int: "Discreta",
        float: "Continua",
        str: "Nominal",
        bool: "Binaria",
    }
    tipos = []

    for elemento in lista:
        tipo = type(elemento)
        if tipo in TIPOS:
            tipo_nombre = TIPOS[tipo]
            tipos.append(tipo_nombre)
    return tipos


def getSubconjunto(lista, indices):
    if not indices: 
        return lista
    return [lista[i] for i in indices if i < len(lista)]

def getSubmatriz(lista, intervalo, ind_subcon):
    if not intervalo:
        return lista
    inicio, fin = intervalo
    en_rango = []
    fuera_de_rango = []
    for i, elemento in enumerate(lista):
        nuevo_elemento = getSubconjunto(elemento, ind_subcon)
        if inicio <= i <= fin:
            en_rango.append(nuevo_elemento)
        else:
            fuera_de_rango.append(nuevo_elemento)

    # Escribir en_rango a un archivo de texto
    with open('Base.txt', 'w') as f:
        for item in en_rango:
            f.write(f"{', '.join(map(str, item))}\n")
    
    # Escribir fuera_de_rango a un archivo de texto
    with open('Entradas.txt', 'w') as f:
        for item in fuera_de_rango:
            f.write(f"{', '.join(map(str, item))}\n")


    return en_rango, fuera_de_rango


  
def calcularDistancia(base, puntos2, tipo):
    distancia = 0
    puntos1 = []
    clase = None
    for elemento in base:
        if isinstance(elemento, str):
            clase = elemento 
        else:
            puntos1.append(elemento) 

    if len(puntos1) == len(puntos2):
        if tipo == "euclidiana":
            for i in range(0, len(puntos1), 1):
                distancia =  distancia + (puntos1[i] - puntos2[i]) ** 2
            distancia = np.sqrt(distancia)
        elif tipo == "manhattan":
            for i in range(0, len(puntos1), 1):
                distancia =  distancia + np.abs(puntos1[i] - puntos2[i])
    else:
        print("Los valores de los vectores no son iguales")
    return distancia, clase
    
