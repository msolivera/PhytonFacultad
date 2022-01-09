class persona:
    def __init__(self,nom,ap,ci,dire,tel):
        self.nombre=nom
        self.apellido=ap
        self.cedula=ci
        self.direccion=dire
        self.telefono=tel

    def __repr__ (self):
        return "Nombre: "+self.nombre+" Apellido: "+self.apellido+" Cedula: "+str(self.cedula)+" Diereccion: "+self.direccion+" Tel: "+str(self.telefono)

    def get_nombre (self):
        return self.nombre
    def get_apellino (self):
        return self.apellido
    def get_cedula (self):
        return self.cedula
    def get_direccion (self):
        return self.direccion
    def get_telefono (self):
        return self.telefono

    def set_nombre (self,nuevo_n):
        if len(nuevo_n)>=1:
            self.nombre=nuevo_n
    def set_apellino (self,nuevo_a):
        if len(nuevo_a)>=1:
            self.apellido=nuevo_a
    def set_direccion (self,nuevo_d):
        if len(nuevo_d)>=1:
            self.direccion=nuevo_d
    def set_telefono (self,nuevo_t):
        if len(nuevo_t)==8
        self.telefono=nuevo_t



p1=persona("Micaela","Olivera",52304220,"sebastopol 5665",25146676)

print(p1)
pi.set_nombre()


#TERMINAR , VERIFICAR QUE FUNCIONE
