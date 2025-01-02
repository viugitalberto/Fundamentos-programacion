#==========================================================================
# ACTIVIDAD 1: INTRODUCCIÓN A PYTHON

# Universidad Internacional de Valencia (VIU)
# Grado en Ciencia de Datos e Inteligencia Artificial.
# Asignatura: 04GIAR Fundamentos de programación

# Versión: 0.04
# Autor  : Alberto Gutiérrez Seldas -- agutierrezs4@student.universidadviu.com
# Fecha Inicio: 20/11/2024
# Fecha Fin:30/11/2024

#==========================================================================
#La actividad consiste en crear una aplicacion para gestionar las estadisticas de un equipo de baloncesto.
#Se dispondrá de un menú con las siguientes opciones:
#[1] Introducir un nuevo jugador
#[2] Listar jugadores
#[3] Máximo anotador
#[4] Estadísticas del equipo
#[0] Salir del programa
#Para un determinado jugador se almacenarán las siguientes características que se deben almacenar al introducir un nuevo jugador
#Nombre
#Dorsal
#Canastas de 3
#Canastas de 2
#Canastas de 1
#En el listado de jugadores se mostrará cada uno de nombres de los jugadores y su dorsal así como sus anotaciones totales.
#Las estadísticas del equipo mostrarán tanto la puntuación total como cada una de las canastas de 3, 2 y 1
#==========================================================================

#En lugar de comenzar con el menú de opciones, se me ha ocurrido empezar creando una lista de jugadores.
#De este modo al llegar al menú todas las opciones son seleccionables.

print("Bienvenido, aquí podrás encontrar las estadísticas de nuestro equipo") #Mensaje de Bienvenida
print("Aún no hay ningún jugador, introduce uno.")

#Defino listas vacías:
lista_anotaciones = []
lista_dorsales = []
lista_canastas_de_3 = []
lista_canastas_de_2 = []
lista_canastas_de_1 = []
lista_jugadores = []
maxima_anotacion = 0
nombre_jugador_maxima_anotacion = ""


#Aqui solicito los inputs:

for jugador in range(1):

    jugador = input(f"Introduce el nombre del jugador {jugador} ")#Nombre
    dorsal = int(input(f"Introduce el dorsal de {jugador} "))#dorsal
    canastas_de_3 = int(input(f"Introduce numero de canastas de 3 de {jugador} "))#canastas de 3
    canastas_de_2 = int(input(f"Introduce numero de canastas de 2 de {jugador} "))#canastas de 2
    canastas_de_1 = int(input(f"Introduce numero de canastas de 1 de {jugador} "))#canastas de 1

    # Defino (anotación) como el sumatorio de las canastas para tener la puntuación total de cada jugador
    anotacion = sum([3 * canastas_de_3, 2 * canastas_de_2, canastas_de_1], 0)
    #Añado los datos a las listas
    lista_anotaciones.append(anotacion)
    lista_jugadores.append(jugador)
    lista_dorsales.append(dorsal)
    lista_canastas_de_3.append(canastas_de_3)
    lista_canastas_de_2.append(canastas_de_2)
    lista_canastas_de_1.append(canastas_de_1)


    if (anotacion > maxima_anotacion):#Si la anotación es mayor a la anterior pasa a ser maxima_anotacion
        maxima_anotacion = anotacion
        # Asignamos también el nombre del jugador relacionado con esa anotacion
        nombre_jugador_maxima_anotacion = jugador





#Ahora que ya tenemos una lista llegamos al menú

print("Ya existe una lista de jugadores")
print("¿Que deseas hacer? Elige una opción: ")

print(" 1.- Introducir un nuevo jugador ")
print(" 2.- Listar jugadores ")
print(" 3.- Máximo anotador")
print(" 4.- Estadísticas del equipo ")
print(" 0.- Salir del programa ")



#Este es el bucle del menu
while True:
    opcion = int(input("Elige una acción: "))

    if(opcion==1):


        for jugador in range(1):

            jugador = input(f"Introduce el nombre del jugador {jugador} ")
            dorsal = input(f"Introduce el dorsal de {jugador} ")
            canastas_de_3 = int(input(f"Introduce numero de canastas de 3 de {jugador} "))
            canastas_de_2 = int(input(f"Introduce numero de canastas de 2 de {jugador} "))
            canastas_de_1 = int(input(f"Introduce numero de canastas de 1 de {jugador} "))

            # Defino (anotación) como el sumatorio de las canastas para tener la puntuación total de cada jugador
            anotacion = sum([3*canastas_de_3, 2*canastas_de_2, canastas_de_1], 0)

            # Añado los datos a las listas
            lista_anotaciones.append(anotacion)
            lista_jugadores.append(jugador)
            lista_dorsales.append(dorsal)
            lista_canastas_de_3.append(canastas_de_3)
            lista_canastas_de_2.append(canastas_de_2)
            lista_canastas_de_1.append(canastas_de_1)

            if (anotacion > maxima_anotacion):  # Si la anotación es mayor a la anterior pasa a ser maxima_anotacion
                maxima_anotacion = anotacion
                # Asignamos también el nombre del jugador relacionado con esa anotacion
                nombre_jugador_maxima_anotacion = jugador

            

    elif(opcion==2):
        #Imprime las listas de nombres, dorsales y puntuaciones
        print(f"Estos son los jugadores"  ,(lista_jugadores))
        print(f"Estos sus dorsales"       ,(lista_dorsales))
        print(f"Y estas sus puntuaciones" ,(lista_anotaciones))


    elif(opcion==3):
        #Imprime el nombre del maximo anotador y su puntuacion.
        print(f"El máximo anotador es {nombre_jugador_maxima_anotacion} con {maxima_anotacion} puntos")

    elif(opcion==4):
        #Puntuacion total del equipo y canastas de 1, 2 y 3 puntos del equipo.
        # Sumatorio de las anotaciones de los jugadores.
        puntuacion_total = sum(lista_anotaciones ,0)
        # Sumatorios de las canastas de los jugadores
        canastas_de_1_totales = sum(lista_canastas_de_1 ,0)
        canastas_de_2_totales = sum(lista_canastas_de_2, 0)
        canastas_de_3_totales = sum(lista_canastas_de_3, 0)
        #Y lo imprimimos
        print(f"La puntuacion total del equipo es", (puntuacion_total))
        print(f"El total de canastas de 1 es", (canastas_de_1_totales))
        print(f"El total de canastas de 2 es", (canastas_de_2_totales))
        print(f"El total de canastas de 3 es", (canastas_de_3_totales))
    elif(opcion==0):
        #La opción 0 rompe el bucle.
        break
    else:
        #Si se introduce un int distinto a las opciones validas le pedimos al usuario que elija una opcion válida
        print("Selecciona una opcion valida")



#==========================================================================



