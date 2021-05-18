class Alumno():
    # Propiedades
    nombre = ""
    apellido = ""
    __dni = "" # Modificado kata_04 de dni a __dni
    __edad = 0 # Modificado kata_04 de edad a __edad

    # Añadido de kata_02
    asignaturas = []

    # Quitado de kata_01
    # nota = 0

    # Constructor
    def __init__(self, nombre, apellido, dni, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.__dni = dni # Modificado kata_04 de dni a __dni
        self.__edad = edad # Modificado kata_04 de edad a __edad

    # Añadido kata_04
    # Get / Set
    @property
    def dni(self):
        return self.__dni

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):
        if (edad > 0 and edad < 100):
            self.__edad = edad
        else:
            raise TypeError("Edad fuera del rango")

    # Metodos
    def Saludar(self):
        print("Hola " + self.nombre)

    def Nota(self, nota):
        if (nota <= 10 and nota >= 0):
            self.nota = nota

    def Cumple(self):
        self.__edad += 1 # Modificado kata_04 de edad a __edad

    def Mostrar_alumno(self):
        print(f'Su nombre es {self.nombre} {self.apellido}.')
        print("Con DNI: " + self.__dni) # Modificado kata_04 de dni a dni
        print("Tiene " + str(self.__edad) + " años.") # Modificado kata_04 de edad a __edad

        # Añadido kata_02
        print(self.asignaturas)

    # Función añadida kata_02
    def anyadir_asignatura(self, asignatura):
        self.asignaturas.append(asignatura)

        # Quitado de kata_01
        # print("Su nota es: " + str(self.nota))