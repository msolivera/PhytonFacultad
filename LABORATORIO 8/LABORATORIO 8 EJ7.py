## Definición de la clase Nota
class Nota():
    def __init__(self, cedula, nombre, nota):
        self.cedula = cedula
        self.nombre = nombre
        self.nota = nota
    ## Métodos get y set correspondientes
    def get_nota(self):
        return self.nota
    
    def set_nota(self, nota):
        self.nota = nota
        
    def get_cedula(self):
        return self.cedula

    def set_cedula(self, cedula):
        self.cedula = cedula

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def __repr__(self):
        return self.cedula+" "+self.nombre+" "+self.nota

## Definición de la clase Grupo
class Grupo():
    def __init__(self, nombre, salon, notas):
        self.nombre = nombre
        self.salon = salon
        self.notas = notas

    def __repr__ (self):
        return self.nombre +"\n"+ self.salon +"\n"+ str(self.notas)

    ## Función de clase que crea un grupo y carga las notas desde un archivo
    def cargar(nombre_archivo, nombre_grupo, salon):
        archivo = open(nombre_archivo)

        lista_notas = []

        for linea in archivo:
            datos = linea.strip().split(",")
            nota = Nota(datos[0], datos[1], datos[2])
            lista_notas.append(nota)

        archivo.close()

        grupo = Grupo(nombre_grupo, salon, lista_notas)

        return grupo

    ## Función de clase que dada una lista de objetos Nota, graba un archivo con los nombres y nota de los alumnos que aprobaron.
    def grabar(notas):

        archivo = open("C:\\Temp\\ResultadosP1.txt", "w") ##CREAR EL ARCHIVO PARA QUE FUNCIONE 

        for obj in notas:
            if int(obj.get_nota()) >= 61:
                archivo.write(obj.get_nombre()+","+obj.get_nota()+"\n")

        archivo.close()
        


grupo1 = Grupo.cargar("C:\\Temp\\notas.txt", "grupo 1", "s1")

print(grupo1)

for nota in grupo1.notas:
    print(nota)

Grupo.grabar(grupo1.notas)










        

    
