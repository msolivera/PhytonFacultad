def dibujo (palabra,columna):
    columa1= (palabra+" ")*columna
    blancos = " "*(len(palabra)+1)
    columna2= palabra+" "+blancos*4+palabra
   
   
    print (columa1)
    print (columna2)
    print (columna2)
    print (columa1)

    
prueba= dibujo ("mica",6)
