print ("BIENVENIDO AL PROGRAMA DE TRANSFORMACION DE CADENAS")
print ("")
print ("Ingrese a continuación la cadena de caracteres que desea modificar:")
cadena = input()
while len(cadena) == 0:
    print ("Debe ingresar al menos un caracter")
    cadena = input()
print ("MENU PRICIPAL")
print ("0- Modo Comando\n1 – Cambiar todas las letras de minúsculas a MAYÚSCULAS.\n2 – Cambiar de minúscula a Mayúscula la primera letra de todas las palabras.\n3 – Cambiar de MAYÚSCULAS a minúsculas todas las letras.\n4 – Quitar todos los espacios a la izquierda del texto.\n5 – Quitar todos los espacios a la derecha del texto.\n6 – Reemplazar todas las ocurrencias de un carácter o palabra por otro\n7 – Cifrado utilizando cifrado Cesar.\n8 – Descifrado utilizando cifrado Cesar.\n9 – Salir")

print ("Ingrese la opción deseada")

x = int(input())


while x != 9:
    
    if x == 0:
        print("BIENVENIDO AL MODO COMANDO\nIngrese los comandos deseados utilizando el separador ¨|¨")
        x = input("Ingrese la opción deseada")
    
    if x ==1 or "mM" in str(x):
        cadena = cadena.upper()
        print (cadena)
        if x==1:
            x = int(input("Ingrese la opción deseada"))
        else:
            x = input("Ingrese la opción deseada")

    if x ==2 or "aA" in str(x):
        cadena = cadena.title ()
        print (cadena)
        if x==2:
            x = int(input("Ingrese la opción deseada"))
        else:
            x = input("Ingrese la opción deseada")
       
    if x ==3 or "Mm" in str(x):
        cadena = cadena.lower ()
        print (cadena)
        if x==3:
            x = int(input("Ingrese la opción deseada"))
        else:
            x = input("Ingrese la opción deseada")
        
    if x ==4 :
        cadena = cadena.lstrip()
        print (cadena)
        x = int (input("Ingrese la opción deseada"))

    if x ==5 :
        cadena = cadena.rstrip()
        print (cadena)
        x = int (input("Ingrese la opción deseada"))
        
    if str("-espacio") in str(x):
        cadena = cadena,strip()
        print (cadena)
        x = input("Ingrese la opción deseada")

    
    if x == 6 :
        modificado = input("Ingrese caracter o palabra a sustituir")
        modificador = input ("Ingrese caracter o palabra que sustituye")
        if modificado in cadena:
            cadena = cadena.split(modificado)
            cadena = modificador.join(cadena)
        else:
            print ("La palabra a sustituir no existe en la cadena")
        print (cadena)
        x = int(input("Ingrese la opción deseada"))

    if ">" in str(x):
        l = list(x)
        aux = l.split("|")
        indice = aux.index (">")
        modificado = aux[indice-1]
        modificador = aux[indice+1]
        if modificado in cadena:
            cadena = cadena.split(modificado)
            cadena = modificador.join(cadena)
        else:
            print ("La palabra a sustituir no existe en la cadena")
        print (cadena)
        x = input("Ingrese la opción deseada")

    if "más>+" in str(x):
        if "mas" in cadena:
            
            cadena = cadena.split ("mas")
            cadena = "+".join (cadena)
        else:
            print ("La palabra a sustituir no existe en la cadena")
        print (cadena)
        x = input("Ingrese la opción deseada")
        
    if x ==7:
        a = int(input("Ingrese el desplazamiento de cifrado"))
        cadena_comparadora= "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ .,_1234567890><!#$%&/()=?¡¿´+*[]{}_:;áéíóú"
        contador = 0
        cifrada = ""
        for i in range (len(cadena)):
            x= cadena_comparadora.find(cadena[i])
            cifrada += cadena_comparadora[x+a]
        cadena = cifrada
        print (cadena)
        x = int(input("Ingrese la opción deseada"))

    if "cif" in str(x) and "decif" not in str (x):
        indice = x.indice ("cif")
        a = int (indice + 2)
        cadena_comparadora= "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ .,_1234567890><!#$%&/()=?¡¿´+*[]{}_:;áéíóú"
        contador = 0
        cifrada = ""
        for i in range (len(cadena)):
            x= cadena_comparadora.find(cadena[i])
            cifrada += cadena_comparadora[x+a]
        cadena = cifrada
        print (cadena)
        x = input("Ingrese la opción deseada")

    if "decif" in str(x):
        indice = x.indice ("cif")
        a = int (indice + 2)
        cadena_comparadora= "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ .,_1234567890><!#$%&/()=?¡¿´+*[]{}_:;áéíóú"
        contador = 0
        cifrada = ""
        for i in range (len(cadena)):
            x= cadena_comparadora.find(cadena[i])
            cifrada += cadena_comparadora[x-a]
        cadena = cifrada
        print (cadena)
        x = input("Ingrese la opción deseada")


    if x ==8 :
        a = int(input("Ingrese el desplazamiento de descifrado"))
        cadena_comparadora= "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ .,_1234567890><!#$%&/()=?¡¿´+*[]{}_:;áéíóú"
        contador = 0
        cifrada = ""
        for i in range (len(cadena)):
            x= cadena_comparadora.find(cadena[i])
            cifrada += cadena_comparadora[x-a]
        cadena = cifrada
        print (cadena)
        x = int(input("Ingrese la opción deseada"))





