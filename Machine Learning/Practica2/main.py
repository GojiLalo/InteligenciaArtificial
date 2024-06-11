import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import funciones

DELIMITADORES = {
    "Coma": ",",
    "Espacio": " ",
    "Punto y coma": ";",
    "Dos puntos": ":"
}

class App:
    def __init__(self, root):
        self.root = root
        self.ruta_archivo = None
        self.matriz = None
        self.tipoDatos = None
        self.n_atributos = 0
        self.n_patrones = 0
        self.ind_atributos = []
        self.ind_matriz = []
        
        self.root.config(width=1200, height=500)
        self.root.title("Machine Learning Practica 1")
        
        # Crear una etiqueta de texto
        label = tk.Label(self.root, text="Delimitador:")
        label.place(x=13, y=50)
        
        # Crear la lista desplegable
        delList = list(DELIMITADORES.keys())
        self.lista = ttk.Combobox(self.root, values=delList, state="readonly")
        self.lista.place(x=85, y=50)
        self.lista.set("Coma")
        
        # Crear un botón para seleccionar un archivo
        boton_archivo = tk.Button(self.root, text="Seleccionar archivo", command=self.seleccionar_archivo)
        boton_archivo.place(x=1050, y=13)
        
        # Crear una etiqueta para mostrar el nombre del archivo seleccionado
        self.etiqueta_archivo = tk.Label(self.root, text="No se ha seleccionado ningún archivo", bg="white", bd=1, relief="solid", width=147, height=2, anchor='w')
        self.etiqueta_archivo.place(x=10, y=10)

        # Crear una caja de texto para ingresar números (Sumatrices)
        self.etiqueta_sub = tk.Label(self.root, text="Submatrices:")
        self.etiqueta_sub.place(x=10, y=73)
        self.caja_numeros = tk.Entry(self.root, width=50)
        self.caja_numeros.place(x=85, y=75)

        # Crear una caja de texto para ingresar números (Subdatos)
        self.etiqueta_submat = tk.Label(self.root, text="Subdatos:")
        self.etiqueta_submat.place(x=10, y=98)
        self.caja_numerosmat = tk.Entry(self.root, width=50)
        self.caja_numerosmat.place(x=85, y=100)

        #Crear un boton para generan submatrices
        boton_submatrices = tk.Button(self.root, text="Generar submatrices", command=self.generarSubMat)
        boton_submatrices.place(x=85, y=125)

        # Crear un Text para mostrar la salida de la consola
        self.consola = tk.Text(self.root, width=80, height=10, bg="lightgrey")
        self.consola.place(x=50, y=200)
    
    def seleccionar_archivo(self):
        self.ruta_archivo = filedialog.askopenfilename(
            title="Seleccionar archivo",
            filetypes=(("Texto plano", "*.csv *.data *.txt *.dat"), ("Todos los archivos", "*.*"))
        )
        if self.ruta_archivo:
            self.etiqueta_archivo.config(text=f"{self.ruta_archivo}")
            delimitador_seleccionado = self.lista.get()
            self.matriz = funciones.leerArchivo(self.ruta_archivo, DELIMITADORES[delimitador_seleccionado])
            self.tipoDatos = funciones.TipoAtributo(self.matriz[0])
            self.n_atributos = len(self.matriz[0])
            self.n_patrones = len(self.matriz)
            self.imprimir_consola(f"Archivo: {os.path.basename(self.ruta_archivo)} || Delimitador: {DELIMITADORES[delimitador_seleccionado]}")
            self.imprimir_consola(f"La base de datos tiene {self.n_patrones} patrones con {self.n_atributos} atributos")
            self.imprimir_consola(f"Los atributos son {str(self.tipoDatos)}")

    def generarSubMat(self):
        subconjunto_indices = self.obtener_indices(self.caja_numeros.get())
        submatrices_indices = self.obtener_indices(self.caja_numerosmat.get())
        funciones.getSubmatriz(self.matriz, subconjunto_indices, submatrices_indices)
        self.imprimir_consola("Archivos de texto generados")

    def obtener_indices(self, texto):
        try:
            # Convertir el texto de la caja en una lista de enteros
            indices = list(map(int, texto.split(',')))
            return indices
        except ValueError:
            self.imprimir_consola("")
            return []

    def imprimir_consola(self, mensaje):
        self.consola.insert(tk.END, mensaje + "\n")
        self.consola.see(tk.END)  # Desplazar el texto automáticamente al final

if __name__ == '__main__':
    ventana = tk.Tk()
    app = App(ventana)
    ventana.mainloop()
