class Alumno():
    # Propiedades
    nombre = ""
    apellido = ""
    dni = ""
    edad = 0
    nota = 0

    # Constructor
    def __init__(self,nombre,apellido,dni,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.edad = edad

    # Metodos
    def Saludar(self):
        print("Hola " + self.nombre)

    def Nota(self, nota):
        if(nota <= 10 and nota >= 0):
            self.nota = nota

    def Cumple(self):
        self.edad += 1

    def Mostrar_alumno(self):
        print(f'Su nombre es {self.nombre} {self.apellido}.')
        print("Con DNI: " + self.dni)
        print("Tiene " + str(self.edad) + " años.")
        print("Su nota es: " + str(self.nota))