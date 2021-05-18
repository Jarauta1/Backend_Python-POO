import kata_01
import kata_02

class Clase():
    # Propiedades
    profesor = None
    alumnos = []
    asignaturas = []

    # Constructor
    def __init__(self, alumnos, asignaturas):
        self.cargar_alumnos(alumnos)
        self.cargar_asignatura(asignaturas)

    # Métodos
    def anyadir_asignatura(self, asignatura):
        self.asignaturas.append(asignatura)

    def quitar_asignatura(self, asignatura):
        self.asignatura.remove(asignatura)

    def anyadir_alumno(self, alumno):
        if (alumno.edad >= 18):
            self.alumnos.append(alumno)

    def quitar_alumno(self, alumno):
        self.alumnos.append(alumno)

    def cargar_alumnos(self, alumnos):
        for nombre in alumnos:
            nuevo_alumno = kata_01.Alumno(nombre, "", "", 18)
            self.anyadir_alumno(nuevo_alumno)

    def cargar_asignatura(self, asignaturas):
        for nombre in asignaturas:
            nueva_asignatura = kata_02.Asignatura(nombre)
            self.anyadir_asignatura(nueva_asignatura)

    def mostrar(self):
        for i_alumnos in self.alumnos:
            print(i_alumnos.nombre)
        for i_asignaturas in self.asignaturas:
            print(i_asignaturas.nombre)