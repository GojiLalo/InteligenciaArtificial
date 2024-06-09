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
    with open('en_rango.txt', 'w') as f:
        for item in en_rango:
            f.write(f"{item}\n")
    
    # Escribir fuera_de_rango a un archivo de texto
    with open('fuera_de_rango.txt', 'w') as f:
        for item in fuera_de_rango:
            f.write(f"{item}\n")

  

matriz = leerArchivo("iris.data", ',')

getSubmatriz(matriz, ([100,150]), [4])
