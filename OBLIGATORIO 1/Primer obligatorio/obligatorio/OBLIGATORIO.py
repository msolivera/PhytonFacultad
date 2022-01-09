print ("BIENVENIDO AL PROGRAMA DE TRANSFORMACION DE CADENAS")
print ("")
print ("Ingrese a continuación la cadena de caracteres que desea modificar:")
cadena = str(input())

print ("MENU PRICIPAL")
print ("0- Modo Comando\n1 – Cambiar todas las letras de minúsculas a MAYÚSCULAS.\n2 – Cambiar de minúscula a Mayúscula la primera letra de todas las palabras.\n3 – Cambiar de MAYÚSCULAS a minúsculas todas las letras.\n4 – Quitar todos los espacios a la izquierda del texto.\n5 – Quitar todos los espacios a la derecha del texto.\n6 – Reemplazar todas las ocurrencias de un carácter o palabra por otro\n7 – Cifrado utilizando cifrado Cesar.\n8 – Descifrado utilizando cifrado Cesar.\n9 – Salir")

print ("Ingrese la opción deseada")

x = int(input())

while x != 9:

    if x == 0:
        print("BIENVENIDO AL MODO COMANDO\nSi desea salir del modo comando por favor ingrese ¨salir¨")
        x = str(input("Ingrese la opción deseada"))
        
    if x == 1 or x == "mM":
        cadena = cadena.upper()
        print (cadena)
        if x == "mM":
            x = str(input("Ingrese la opción deseada"))
        else:
            x = int(input("Ingrese la opción deseada"))

    if x == 2 or x == "aA":
        cadena = cadena.title ()
        print (cadena)
        if x == "aA":
            x = str(input("Ingrese la opción deseada"))
        else:
            x = int(input("Ingrese la opción deseada"))

    if x ==3 or x == "Mm":
        cadena = cadena.lower ()
        print (cadena)
        if x == "Mm":
            x = str(input("Ingrese la opción deseada"))
        else:
            x = int(input("Ingrese la opción deseada"))

    if x == 4:
        cadena = cadena.lstrip()
        print (cadena)
        x = int(input("Ingrese la opción deseada"))

    if x == 5:
        cadena = cadena.rstrip()
        print (cadena)
        x = int(input("Ingrese la opción deseada"))
        
    if x == "-espacio":
        cadena = cadena,strip()
        print (cadena)
        x = str(input("Ingrese la opción deseada"))

    
    if x == 6:
        modificado = input("Ingrese caracter o palabra a sustituir")
        modificador = input ("Ingrese caracter o palabra que sustituye")
        if modificado in cadena:
            cadena = cadena.split(modificado)
            cadena = modificador.join(cadena)
        else:
            print ("La palabra a sustituir no existe en la cadena")
        print (cadena)
        x = int(input("Ingrese la opción deseada"))

    if x == 7:
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


    if x == 8:
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

    else:
        print ("la opción que ud. ingresó es incorrecta")
        x = int(input("Ingrese la opción deseada"))









        
        

