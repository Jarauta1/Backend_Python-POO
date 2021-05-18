class Usuario():
    # Propiedades
    nombre = ""
    apellidos = ""
    __dni = ""
    __edad = 0

    # Constructor
    def __init__(self, nombre, apellidos, dni, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.__dni = dni
        self.__edad = edad

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

    # Métodos
    def saludar(self):
        print(f'Hola, me llamo {self.nombre}')

    def despedida(self):
        print(f'Adios {self.nombre}')

    def cumple(self):
        self.__edad += 1


class Alumno(Usuario):
    # Propiedades
    asignaturas = []

    # Constructor
    def __init__(self, nombre, apellidos, dni, edad):
        super().__init__(nombre, apellidos, dni, edad)

    # Get / Set

    # Métodos
    def anyadir_asignatura(self, asignatura):
        self.asignaturas.append(asignatura)


class Profesor(Usuario):
    # Propiedades
    especialidad = ""

    # Constructor
    def __init__(self, nombre, apellidos, dni, edad):
        super().__init__(nombre, apellidos, dni, edad)

    # Get / Set

    # Métodos


class Clase():
    # Propiedades
    __id = 0
    profesor = None
    alumnos = []
    asignaturas = []

    # Constructor
    def __init__(self, profesor, alumnos, asignaturas):
        self.profesor = profesor
        self.__cargar_alumnos(alumnos)
        self.__cargar_asignatura(asignaturas)

    # Get / set
    @property
    def id(self):
        return self.__id

    # Métodos
    def __anyadir_asignatura(self, asignatura):
        self.asignaturas.append(asignatura)

    def quitar_asignatura(self, asignatura):
        self.asignatura.remove(asignatura)

    def __anyadir_alumno(self, alumno):
        if (alumno.edad >= 18):
            self.alumnos.append(alumno)

    def quitar_alumno(self, alumno):
        self.alumnos.append(alumno)

    def cargar_alumnos(self, alumnos):
        for nombre in alumnos:
            nuevo_alumno = Alumno(nombre, "", "", 18)
            self.anyadir_alumno(nuevo_alumno)

    def cargar_asignatura(self, asignaturas):
        for nombre in asignaturas:
            nueva_asignatura = Asignatura(nombre)
            self.anyadir_asignatura(nueva_asignatura)

    def mostrar(self):
        for i_alumnos in self.alumnos:
            print(i_alumnos.nombre)
        for i_asignaturas in self.asignaturas:
            print(i_asignaturas.nombre)


if __name__ == '__main__':


# See PyCharm help at https://www.jetbrains.com/help/pycharm/