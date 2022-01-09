
cadena= "agus"
cadena_min = cadena.lower()
cadena_comparadora= "abcdefghijklmnopqrstuvwxyz .,_1234567890"
contador = 0
cifrada = ""
for i in range (len(cadena_min)):
    x= cadena_comparadora.find(cadena_min[i])
    cifrada += cadena_comparadora[x+3]
print (cifrada)
