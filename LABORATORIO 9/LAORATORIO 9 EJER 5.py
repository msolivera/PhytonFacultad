def misma_inicial (nombre_archivo):

    archivo = open (nombre_archivo)

    resultado = {}

    
    for linea in archivo:

       for c in linea:
            for c in range (0):
                print (c)
                """if c in resultado:
                    resultado[c] += 1
                else:
                    resultado[c] = 1

        return resultado"""
                
        
        
print(misma_inicial("C:\\Temp\\ejer5.txt"))
        
        
