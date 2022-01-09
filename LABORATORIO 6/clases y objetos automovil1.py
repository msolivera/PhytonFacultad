class automovil:
    def __init__(self,_marca,_modelo,_matricula,_año,_color):
        self.matricula=_matricula
        self.marca=_marca
        self.modelo=_modelo
        self.año=_año
        self.color=_color
auto1=automovil("BMW","135i","sbc999",2014,"blanco")
print (auto1)
print(auto1.marca)
