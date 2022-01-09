comando = input ("Ingrese los comandos deseados: ")
comando = list(comando)
comando = "".join(comando)
comando = comando.split("|")
print (comando)

intercambio = []
cadena_comparadora= "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ .,_1234567890><!#$%&/()=?¡¿´+*[]{}_:;áéíóú"
lista_abc = list(cadena_comparadora)
for i in lista_abc:
    for j in lista_abc:
        intercambio.append (str(str(i)+">"+str(j)))
lista_de_comandos = ["mM","Mm","aA","-espacio","mas>+","cif x","decif x"]+ intercambio

verificador = 0
while verificador < len(comando):
    for i in range (len(comando)):
        if comando[i] in lista_de_comandos:
            verificador += 1
        else:
            print ("Error: Verifique los comandos ingresados")
            comando = input ("Ingrese los comandos deseados: ")
            comando = list(comando)
            comando = "".join(comando)
            comando = comando.split("|")

    
print(intercambio)




