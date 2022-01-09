#EJERCICIO 2:
def fecha (d,m,a):
    while ((a%4==0 and a%100!=0) or a%400==0)and d==29 and m==2:
        return "FECHA VALIDA"
    while ((a%4!=0 and a%100!=0) or a%400!=0)and d==29 and m==2:
        return "FALSO"
    if d<=30 and m==2 or m==4 or m==6 or m==8 or m==11:
        return "FECHA VALIDA"
    if d<=31 and m==1 or m==3 or m==5 or m==7 or m==9 or m==10 or m==12:
        return "FECHA VALIDA"
    elif d>31 or m>12:
        return "FALSO"
    elif d>28 and m==2: 
        return "FALSO"
    elif d>31 and m==1 or m==3 or m==5 or m==7 or m==9 or m==10 or m==12:
        return "FALSO"
    elif d>30 and m==2 or m==4 or m==6 or m==8 or m==11:
        return "FALSO"
    
print ( fecha(29,56,2017))

#EJERCICIO 3:

