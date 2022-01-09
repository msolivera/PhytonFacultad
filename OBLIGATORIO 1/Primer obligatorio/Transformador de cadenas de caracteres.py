#definimos bloque como conjunto de lineas que poseen una funcion

# Presentación del programa
print ("BIENVENIDO A 'TRANSFORMADOR DE CADENAS DE CARACTERES'")
print ("")
print ("Ingrese a continuación la cadena de caracteres que desea modificar:")

cadena = input()    #ingreso de la cadena a editar
Cadena_Inicial = cadena #se guarda el valor inicial para luego mostrar al final del programa

#bloque que impide que se ingrese una cadena de longitud 0
while len(cadena) == 0:     
    print ("Debe ingresar al menos un caracter")
    cadena = input()    #se solicita nuevamente la cadena

#definicion de menu, opciones y cadena comparadora para utilizar más adelante
menu = "MENU PRICIPAL\n\n0- Modo Comando\n1 – Cambiar todas las letras de minúsculas a MAYÚSCULAS.\n2 – Cambiar de minúscula a Mayúscula la primera letra de todas las palabras.\n3 – Cambiar de MAYÚSCULAS a minúsculas todas las letras.\n4 – Quitar todos los espacios a la izquierda del texto.\n5 – Quitar todos los espacios a la derecha del texto.\n6 – Reemplazar todas las ocurrencias de un carácter o palabra por otro\n7 – Cifrado utilizando cifrado Cesar.\n8 – Descifrado utilizando cifrado Cesar.\n9 – Salir\n10- Mostrar MENU\n11- Contacto"
opciones = ["0","1","2","3","4","5","6","7","8","9","10","11"]        
cadena_comparadora= "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ .,_1234567890><!#$%&/()=?¡¿´+*[]{}_:;áéíóú"

print (menu)#mostrar menu
x = ""# variable con la que se va a trabajar para elegir las opciones del menu
while x != "9":   #mientras la opciion ingresada no sea la salida, se produce un bucle que permite hacer varias modificaciones a la cadena

    x = input("Ingrese la opción deseada: ")#se ingresa una opcion
    while x not in opciones:
        print ("La opción que Ud. ingresó no es válida")#si la misma no se encuentra dentro de la lista opciones, se pide ingresar nuevamente
        x = input("Ingrese la opción deseada: ")

    if x == "1":    #opcion 1 Cambiar todas las letras de minúsculas a MAYÚSCULAS
        cadena = cadena.upper()

    elif x == "2":    #opcion 2 Cambiar de minúscula a Mayúscula la primera letra de todas las palabras
        cadena = cadena.title ()
                       
    elif x == "3":    #opcion 3 Cambiar de MAYÚSCULAS a minúsculas todas las letras.
        cadena = cadena.lower ()
                
    elif x == "4":    #opcion 4 Quitar todos los espacios a la izquierda del texto
        cadena = cadena.lstrip()
                
    elif x == "5":    #opcion 5 Quitar todos los espacios a la derecha del texto.
        cadena = cadena.rstrip()
                
    elif x == "6":    #opcion 6 Reemplazar todas las ocurrencias de un carácter o palabra por otro
        modificado = input("Ingrese caracter o palabra a sustituir ")
        modificador = input ("Ingrese caracter o palabra que sustituye ")
        if modificado in cadena:
            cadena = cadena.split(modificado)   #separa y elimino las ocurrencias del modificado
            cadena = modificador.join(cadena)   #une utilizando como nexo el modificador
        else:
            print ("La palabra a sustituir no existe en la cadena") #si el modificado ingresado, no se encuentra en cadena, desplega error
        
    elif x == "7": #opcion 7 Cifrado utilizando cifrado Cesar.
        print("Utilice valores positivos")
        despl = input("Ingrese el desplazamiento de cifrado ")
        a = ""
        for n in despl:#se verifica que los valores de desplazamiento sean numeros
            if n in "0123456789":
                a += n#se suman los caracteres numericos
            else:
                print("Error en el valor de desplazamiento ingresado")
                a=0     #en caso de error, se realiza transformacion con valor cero
                break   #se utiliza break para que no se sigan agregando valores a la variable "a"
        a = int(a)

        cifrada = "" #cifrada es una cadena vacia en la que se agregaran los valores cifrados
        for i in cadena:#se recorre cada elemento de cadena
            x= cadena_comparadora.find(i)   #se ubica dicho elemento en la cadena comparadora, asignandole un valor
            while x+a >= 97:    # se define el rango en el que se buscaran los elementos en la cadena_comparadora (97 es la cantidad de elementos en la cadena_comparadora)
                a -= 97
            cifrada += cadena_comparadora[x+a] #el valor agregado a cifrada es el elemento en la cadena comparadora en la posicion con el desplazamiento sumado
        cadena = cifrada
    
    elif x == "8":    #opcion 8 Descifrado utilizando cifrado Cesar.
        print("Utilice valores positivos")
        despl = input("Ingrese el desplazamiento de decifrado ")
        a = ""
        for n in despl:#se verifica que los valores de desplazamiento sean numeros
            if n in "0123456789":
                a += n #se suman los caracteres numericos
            else:
                print("Error en el valor de desplazamiento ingresado")
                a=0     #en caso de error, se realiza transformacion con valor cero
                break   #se utiliza break para que no se sigan agregando valores a la variable "a"
        a = int(a)

        cifrada = "" #cifrada es una cadena vacia en la que se agregaran los valores cifrados
        for i in cadena:#se recorre cada elemento de cadena
            x= cadena_comparadora.find(i)   #se ubica dicho elemento en la cadena comparadora, asignandole un valor
            while x+a >= 97:    # se define el rango en el que se buscaran los elementos en la cadena_comparadora (97 es la cantidad de elementos en la cadena_comparadora)
                a -= 97
            cifrada += cadena_comparadora[x-a] #el valor agregado a cifrada es el elemento en la cadena comparadora en la posicion con el desplazamiento restado
        cadena = cifrada 
        
    elif x== "11": #contacto
        print ("")
        print ("Contacto:\nPor consultas comuníquese via mail con nosotros: Micaela Olivera (micaela.olivera@correo.ucu.edu.uy) , Agustin Picos(agustin.picos@correo.ucu.edu.uy)\nMuchas gracias")
                
    elif x == "10": #mostrar menu
        print ("")
        print (menu)

    elif x == "0":    #opcion 0 Modo Comando
        bucle = 1 #variable que indica que se realice un bucle de transformaciones dentro del modo comando
        while bucle ==1:
            cadena0 = cadena #se guarda la cadena sin transformar por si se producen errores de comando
            print("Modo Comando")
            comando = input ("Ingrese los comandos deseados: ") #se ingresa el comando
            comando = comando.split("|")    #se separan los elementos divididos por 'pipe'
            
            for i in comando:  #se recorren los comandos ingresados para proceder en orden de ingreso

                if i =="10":#menu
                    x= "10" #opcion menu
                    bucle = 0 #al ingresarse al menu se sale del modo comando
                    print(menu)

                elif i =="9":#salir
                    x= "9" # opcion salir
                    bucle = 0#al ingresarse al menu se sale del modo comando
                    
                elif i == "mM":
                    cadena = cadena.upper() #Transforma texto a MAYUSCULAS

                elif i =="Mm":
                    cadena = cadena.lower() #Transforma texto a minusculas

                elif i == "aA":
                    cadena = cadena.title () #transforma texto a formato titulo

                elif i == "-espacio":
                    cadena = cadena.strip() #quita los espacios a ambos lados del texto

                elif len(i) == 3 and i[1] == ">": # comprueba que el largo del comando que contiene '>' y la ubicacion del signo
                    lista1 = i # usa un auxiliar para trabajar con el comando
                    lista1 = lista1.split(">") # separa el comando en sus dos elementos de modificacion
                    aux = cadena.split(lista1[0]) # se separa y quita el elemento modificado de la cadena
                    aux2= lista1[1].join(aux) # se une la cadena mediante el elemento modificador
                    cadena = aux2 

                elif i == "más>+": # Transforma las ocurrencias de 'más' por '+'
                    if "más" in cadena: #se verifica que la opcion se encuentre en la cadena
                        cadena = cadena.split("más")# quita y separa los 'más'
                        cadena = "+".join(cadena) #une mediante '+'
                    else:  #en caso de que la cadena no contenga la palabra más (con tilde)
                        print ("La palabra a sustituir no existe en la cadena")
                        print ("")
                        print (cadena)

            
                elif "cif " in i and "decif " not in i: #se verifica que 'cif ' este en el comando, pero que no sea 'decif ' el comando
                    aux = i
                    aux = aux.split(" ") #se separa el comando del valor de cifrado
                    cifrada = "" #cadena en la que se agregan los elementos cifrados
                    a = "" #variable donde se guarda el valor de cifrado
                    cif = 1
                    for c in aux [1]: #se corrobora que el valor de cifrado ingresado por el usuario sean numeros
                        if c in "0123456789": 
                            a += c
                        else:   #en caso de un error, se realiza una transformacion con valor 0
                            a = 0
                            cif =0 #indicador de error
                            break
                    a = int(a)
                    if cif ==0: # error 
                        print ("Error en el comando cif ")
                    else:
                        for i in cadena: # recorre la cadena
                            x = cadena_comparadora.find(i)#ubica el caracter en la cadena_comapradora
                            while x+a>=97: #delimita el rango de busqueda dentro de la cadena_comparadora
                                x-=97
                            cifrada += cadena_comparadora [x+a] # agrega el valor de cifrado
                        cadena = cifrada
                    
                elif "decif " in i:#se verifica que 'decif ' este en el comando
                    aux = i
                    aux = aux.split(" ") #se separa el comando del valor de cifrado
                    cifrada = "" #cadena en la que se agregan los elementos cifrados
                    a = "" #variable donde se guarda el valor de cifrado
                    cif = 1
                    for c in aux [1]: #se corrobora que el valor de cifrado ingresado por el usuario sean numeros
                        if c in "0123456789": 
                            a += c
                        else:   #en caso de un error, se realiza una transformacion con valor 0
                            a = 0
                            cif =0 #indicador de error
                            break
                    a = int(a)
                    if cif ==0: # error 
                        print ("Error en el comando decif ")
                    else:
                        for i in cadena:# recorre la cadena
                            x = cadena_comparadora.find(i)#ubica el caracter en la cadena_comapradora
                            while x+a>=97: #delimita el rango de busqueda dentro de la cadena_comparadora
                                x-=97
                            cifrada += cadena_comparadora [x-a] # agrega el valor de cifrado
                        cadena = cifrada
                    
                else: # si un comando no esta en las opciones de comando
                    print ("El comando que Ud. ingresó no es válido")
                    cadena = cadena0 #se vuelve a la cadena previa a las transformaciones

            if cadena != cadena0: #si se realizo alguna transformacion, se muestra el valor
                print ("")
                print (cadena)

    else:#si la opcion no esta en las opciones validas
        print ("La opción que Ud. ingresó no es válida")

    print("")#luego de cada transformacion se muestra el nuevo resultado
    print(cadena)
       
            

print ("Usted ha finalizado el programa.")
print ("Cadena Inicial",Cadena_Inicial)
print ("Cadena final",cadena)
a=input() #evita que se cierre el programa para que se pueda ver el resultado final

