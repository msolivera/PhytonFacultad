def año (aa):
    if ((aa%4==0 and aa%100!=0) or aa%400==0):
        return "año bisiesto"
año(2016)

     
print (año(2016))

