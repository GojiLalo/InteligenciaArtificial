import pygame
import sys
import csv
import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

DELIMITADORES = {
    "Coma":",",
    "Espacio":" ",
    "Punto y coma":";",
    "Dos puntos":":"
}

def obtenerSeparadores():
    def on_button_click():
        global seleccion
        seleccion = lista.get()
        ventana.destroy()
        
    global seleccion
    seleccion = None
    
    ventana = tk.Tk()
    ventana.config(width=300, height=200)
    ventana.title("Elegir delimitador")

    delList = list(DELIMITADORES.keys())
    lista = ttk.Combobox(ventana, values=delList)
    lista.place(x=50, y=50)

    boton = tk.Button(ventana, text="Aceptar", command=on_button_click)
    boton.place(x=100, y=100)

    ventana.mainloop()
    
    return seleccion

def leerCSV():
    matriz = []   
    ruta = filedialog.askopenfilename(initialdir=(os.getcwd()+"\\Bases"))
    seleccion = obtenerSeparadores()
     
    with open(ruta, 'r') as file:
        reader = csv.reader(file, delimiter=seleccion)
        for row in reader:
            matriz.append([cell for cell in row])
    return matriz