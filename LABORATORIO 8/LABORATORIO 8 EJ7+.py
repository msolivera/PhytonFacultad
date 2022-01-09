class Nota():
    def __init__ (self,cedula,nombre,nota_final):
        self.cedula = cedula
        self.nombre = nombre
        self.nota_final = nota_final

    def get_cedula (self):
        return self.cedula
    def set_cedula (self,cedula):
        return self.cedula

    def get_nombre (self):
        return self.nombre
    def set_nombre (self,nombre):
        return self.nombre

    def get_nota_final(self):
        return self.nota_final
    def set_nota_final(self):
        return self.nota_final

class grupo ():
    def __init__ (self,nombre_grupo, salon, notas):

        self.nombre_grupo = nombre_grupo
        self.salon = salon
        self.notas = notas

    def cargar_nota (nombre_grupo, salon,archivo):
        archivo = open(archivo)
        lista_de_notas =[]

        for linea in archivo:
            datos = linea.strip().split(",")
            nota= nota_final(datos[0],datos[1],datos[2])
            lista_nota.append(nota)

        grupo_final = grupo(nombre_grupo, salon, lista_de_notas)

        return grupo_final
        
        archivo.close()

    def grabar(notas):

        archivo = open("C:\\Temp\\ResultadosP1.txt", "w")
        for objeto in notas:
            if int(objeto.get_nota_final()) >= 61:

                archivo.write(objeto.nombre + ";" +objeto.get_nota_final()+"\n")

        archivo.close()
        
grupo1= grupo.cargar_nota ("grupo 3", "s5","C:\\Temp\\notas.txt")
grupo.grabar(grupo1.notas)











        
