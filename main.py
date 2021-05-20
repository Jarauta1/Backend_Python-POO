import serie #Trae la clase Serie
import videojuego #Trae la clase Videojuego

if __name__ == '__main__':
    series = []
    videojuegos = []

    #Creación de una serie
    serie1 = serie.Serie("Modern Family", "Comedia", "No lo se",6)
    serie2 = serie.Serie("Hola","Comedia","Yo",8)

    #Mostrar serie creada
    #print(serie1)
    #print(serie2)
    series.append(serie1)
    series.append(serie2)

    #print(series[0].titulo)
    serie1.compareTo(series)


    #Creación de un videojuego
    videojuego1 = videojuego.Videojuego("Uncharted", "Shooter", "NaughtyDog")

    #Mostrar serie creada
    #print(videojuego1)

    #serie1.entregar()
    #serie1.isEntregado()
    #serie1.devolver()
    #serie1.isEntregado()