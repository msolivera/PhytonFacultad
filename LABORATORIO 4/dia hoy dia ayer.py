def dia_mes_año (d,m,a):
    if ((a%4==0 and a%100!=0) or a%400==0)and d==1 and m==3:
        return 29,m-1,a
    elif d>31 or m>12:
        return "false"
    elif d>28 and m==2: 
        return "false"
    elif d>30 and m==4 or m==6 or m==9 or m==11:
        return "false"
    elif d>1:
        return d-1,m,a
    elif d==1 and m==3:
        return 28,m-1,2017
    elif d==1 and m==1:
        return 31,12,a-1
    elif d==1 and m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
        return 30, m-1,a
    elif d==1 and m==2 or m==4 or m==6 or m==9 or m==11:
        return 31,m-1,a
   
    
    
        
print (dia_mes_año (1,3,2017))


