import serie #Trae la clase Serie
import videojuego #Trae la clase Videojuego

if __name__ == '__main__':
    #Creación de una serie
    serie1 = serie.Serie("Modern Family", "Comedia", "No lo se")

    #Mostrar serie creada
    print(serie1)

    #Creación de un videojuego
    videojuego1 = videojuego.Videojuego("Uncharted", "Shooter", "NaughtyDog")

    #Mostrar serie creada
    print(videojuego1)

    serie1.entregar()
    serie1.isEntregado()
    serie1.devolver()
    serie1.isEntregado()