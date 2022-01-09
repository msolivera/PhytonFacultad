#PREPARACION CUARTO LABORATORIO

#EJERCICIO 1:

def obtener_cadena():

    texto=""
    cadena=""
    
    while cadena != "fin":
        cadena=input("Ingrese cadena deseada: ")

        if len(cadena)<1:
            print("ingrese al menos un caracter: ")
            cadena=input("Ingrese cadena deseada: ")
        while "1" in cadena or "2" in cadena or "3" in cadena or "4" in cadena or "5" in cadena or "6" in cadena or "7" in cadena or "8" in cadena or "9" in cadena or "0" in cadena:
            print("No puede ingresar numeros: ")
            cadena=input("Ingrese cadena deseada: ")

            
        texto= texto + " " + cadena    

    if cadena == "fin":

        print("Ha finalizado la escritura")
        print("CADENA: ",texto)    
        
        
       
obtener_cadena()    


