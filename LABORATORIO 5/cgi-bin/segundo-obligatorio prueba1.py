def cargar_med(medicamento):
    archivo_med = open("C:\\Users\\usuario\\AppData\\Local\\Programs\\Python\\Python36-32\\cgi-bin\\medicamentos.dat")
    for linea in archivo_med:
        med = linea.split(",")
        if med[1] == medicamento:
            return med[0]
        

print(cargar_med("dorzomed"))
