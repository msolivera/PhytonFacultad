def estadistica (nombre_archivo):

    archivo = open (nombre_archivo)

    resultado = {}

    porcentajes = {}
    
    total  = 0    
    for linea in archivo:
        for c in linea.lower().strip(): #c=cada caracter no cada palabra

            if c in resultado:

                resultado[c]= resultado[c]+1
                
            else:
                resultado[c] = 1

            total += 1

    archivo.close()

    for c in resultado :
        resultado [c] = (resultado[c]/total)*100 
    return resultado 
    
print(estadistica("c:\\temp\\prueba.txt"))
