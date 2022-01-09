def fecha (parametro):
    reemplazo=""
    contador=1
    s=parametro
    s1=s[ :2]
    s2=s[3:5]
    s3=s[6: ]
    for i in range (len(parametro)):
        if parametro[i] in "/":
            reemplazo="-"
            contador=contador+1
            resultado= s3+reemplazo+s2+reemplazo+s1
    return resultado

print(fecha("23/12/2017"))
            

