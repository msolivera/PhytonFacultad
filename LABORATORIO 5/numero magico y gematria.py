def gematria(subcadena):
    abecedario=subcadena.lower()
    contador=0
    cadena="abcdefghijklmnñopqrstuvwxyz"
    for i in range (len(abecedario)):
        x=cadena.find(abecedario[i])
        contador=contador+(x+1)
    if contador==21:
        print("MAGICO")
    else:
        print ("numero comun")

    return contador

print(gematria("jja"))
