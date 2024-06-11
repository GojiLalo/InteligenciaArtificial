import FuncionesCSV as CSV

if __name__ == '__main__':
        delimitador = CSV.obtenerSeparadores()
        matriz = CSV.leerCSV(CSV.DELIMITADORES[delimitador])
        n_atributos = len(matriz[0])
        n_patrones = len(matriz)
        print(f"La base de datos tiene {n_patrones} patrones con {n_atributos} atributos")
<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes

