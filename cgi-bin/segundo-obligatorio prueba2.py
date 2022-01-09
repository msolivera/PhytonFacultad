medicamento = "dorzomed"
def cargar_med():
    archivo_med = open("C:\\Users\\usuario\\AppData\\Local\\Programs\\Python\\Python36-32\\cgi-bin\\medicamentos.dat")
    for linea in archivo_med:
        med = linea.split(",")
        if med[1] == medicamento:
            return med[0]
        
def cargar_farmacias_med():
    archivo_farm_med = open("C:\\Users\\usuario\\AppData\\Local\\Programs\\Python\\Python36-32\\cgi-bin\\farm-med.dat")
    lista = []
    for linea in archivo_farm_med:
        farm = linea.strip().split(",")
        if farm[1] == cargar_med():
            lista.append(farm[0])

    return lista

print(cargar_farmacias_med())


