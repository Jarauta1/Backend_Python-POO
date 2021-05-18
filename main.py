import kata_01
import kata_02
import kata_03


if __name__ == '__main__':
    # Quitado kata_01
    # diego = kata_01.Alumno("Diego", "Jarauta", "00000000A", 33)
    # diego.Mostrar_alumno()
    # diego.Saludar()
    # diego.Nota(8)
    # diego.Cumple()
    # diego.Mostrar_alumno()

    # Quitado kata_02
    # matematicas = kata_02.Asignatura("Matemáticas")
    # fisica = kata_02.Asignatura("Fisica")
    # matematicas.anyadir_nota(8)
    # diego = kata_01.Alumno("Diego", "Jarauta", "000000000A", 33)
    # diego.anyadir_asignatura(matematicas)
    # diego.anyadir_asignatura(fisica)
    # diego.Mostrar_alumno()

    # Quitado kata_03
    # alumnos = ["Manuel", "Ana", "Jorge"]
    # asignaturas = ["Matematicas", "Fisica", "Sociales", "Gimnasia"]
    # aula = kata_03.Clase(alumnos, asignaturas)
    # aula.mostrar()

    # Añadido kata_04
    diego = kata_01.Alumno("Diego", "Jarauta", "00000000X", 33)
    print(diego.dni)
    print(diego.edad)
    # diego.dni = ""
    diego.edad = 50
    print(diego.dni)
    print(diego.edad)
    diego.edad = 101

# See PyCharm help at https://www.jetbrains.com/help/pycharm/