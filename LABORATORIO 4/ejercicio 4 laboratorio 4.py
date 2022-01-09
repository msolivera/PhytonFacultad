def dibujo (base,altura):
    dibujo=print("x"*base)
    for fila in range (altura):
        print("x"+" "*(base-2)+"x")
    dibujo=print("x"*base)
dibujo(7,5)

