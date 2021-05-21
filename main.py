import serie #Trae la clase Serie
import videojuego #Trae la clase Videojuego

if __name__ == '__main__':
    series = [] # Array de Series
    videojuegos = [] # Array de Videojuegos

    #Creación de las series
    serie1 = serie.Serie("Modern Family", "Comedia", "Christopher Lloyd",11)
    serie2 = serie.Serie("Arrow","Superhéroes","Greg Berlanti",8)
    serie3 = serie.Serie("The Big Bang Theory","Comedia","Chuck Lorre",12)
    serie4 = serie.Serie("The Witcher","Fantástico","Lauren Schmidt Hissrich", 2)
    serie5 = serie.Serie("Malviviendo","Comedia", "David Sainz")

    #Creación de los videojuegos
    videojuego1 = videojuego.Videojuego("Uncharted", "Acción-aventura", "Naughty Dog")
    videojuego2 = videojuego.Videojuego("SpiderMan", "Acción-aventura", "Insomniac Games",8)
    videojuego3 = videojuego.Videojuego("Batman: Arkham Knight", "Acción-aventura", "Unreal Engine 3",14)
    videojuego4 = videojuego.Videojuego("Rocket League","Deportes","Psyonix")
    videojuego5 = videojuego.Videojuego("FIFA21","Fútbol","EA-Sports",6)

    #Añadir a los arrays
    series.extend([serie1,serie2,serie3,serie4,serie5])
    videojuegos.extend([videojuego1,videojuego2,videojuego3,videojuego4,videojuego5])

    #Mostrar serie creada
    #print(serie1)
    #print(serie2)

    # Mostrar videojuego creado
    # print(videojuego1)

    # Entregar Series y videojuegos
    serie2.isEntregado() # Estado de entregado de la serie 2 (debe ser False)
    serie2.entregar() # Lo entregamos
    serie2.isEntregado() # Ahora debe ser True

    serie4.entregar()
    videojuego1.entregar()
    videojuego3.entregar()
    videojuego5.entregar()

    # Contar cuantas Series y Videojuegos hay entregados
    total_series_entregadas = 0
    total_videojuegos_entregados = 0

    for element_serie in series:
        if element_serie.entregado == True:
            total_series_entregadas += 1
            print(f'La serie {element_serie.titulo} está entregada') #Mostramos la serie entregada

    for element_videojuego in videojuegos:
        if element_videojuego.entregado == True:
            total_videojuegos_entregados += 1
            print(f'El videojuego {element_videojuego.titulo} está entregado') #Mostramos el videojuego entregado

    #Sacamos el total de Series y Videojuegos entregados
    print(f'Hay {total_series_entregadas} series entregadas y {total_videojuegos_entregados} videojuegos entregados.')

    #Mostrar la info completa de la serie que tiene más temporadas y del videojuego que tiene más horas
    serie2.compareTo(videojuegos)
    serie2.compareTo(series)
