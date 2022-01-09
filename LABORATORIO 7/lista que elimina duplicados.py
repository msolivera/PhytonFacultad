
lista=[]
lista=[1,2,2,3,5,7,4,3,3,5,7,3,4547,678,3]
nuevalista=[]
for i in lista:
    if i not in nuevalista:
        nuevalista=lista.append(i)
print (nuevalista)
