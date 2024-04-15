import pygame
import sys
import csv
import tkinter as tk
from tkinter import filedialog

# Definir colores
GRAY = (128, 128, 128)
FLESH = (250, 206, 135)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 128, 0)
BLACK = (0, 0, 0)

# Tamaño de la cuadrícula
GRID_SIZE = 20

def leerCSV():
    matriz = []
    raiz = tk.Tk()
    raiz.withdraw()
    
    ruta = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
     
    with open(ruta, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            matriz.append([int(cell) for cell in row])
    return matriz

def convertirCSV(nombre):
    matriz = [] 
    with open(nombre) as file:
        reader = csv.reader(file)
        for row in reader:
            matriz.append([int(cell) for cell in row])
    return matriz
