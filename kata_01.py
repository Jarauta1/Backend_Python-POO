class Alumno():
    # Propiedades
    nombre = ""
    apellido = ""
    dni = ""
    edad = 0

    # Añadido de kata_02
    asignaturas = []

    # Quitado de kata_01
    # nota = 0

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

        # Añadido kata_02
        print(self.asignaturas)

    # Función añadida kata_02
    def anyadir_asignatura(self, asignatura):
        self.asignaturas.append(asignatura)

        # Quitado de kata_01
        # print("Su nota es: " + str(self.nota))