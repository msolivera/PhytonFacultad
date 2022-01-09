def transformar_nombres(lista):
    resultado=[]
    for i in range (len(lista)):
        resultado=resultado.append(lista[i][0]+ " "+lista[i][1])
    return resultado
lista=transformar_nombres([["Micaela","olivera"],["jorge","llagarias"]])

