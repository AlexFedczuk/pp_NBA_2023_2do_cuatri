from funciones import mostrar_menu_principal, pedir_un_numero_entero_regex, listar_nombres_jugadores_con_posiciones
from equipo import Equipo

ubicacion_archivo_dt_json = "dream_team.json"
mensaje_de_desarollo = "\nEsta opcion esta en desarrollo..."

dream_team = Equipo(ubicacion_archivo_dt_json)
lista_jugadores = dream_team.cargar_lista_jugadores()

#ultimo_jugador_opcion_dos = {}

condicion = True
while condicion:
    mostrar_menu_principal()
    opcion_menu = pedir_un_numero_entero_regex("Ingrese una opcion del menu: ", "ERROR! Ha ingresado un valor invalido.")
    
    match opcion_menu:
        case 1:
            print("\nJugadores con sus Posiciones:\n****************************")
            listar_nombres_jugadores_con_posiciones(lista_jugadores)
        case 2:
            print("\n***** Lista de  jugadores del Dream Team *****\nIndice - Nombre Jugador\n-----------------------")
        case 3:
            print(mensaje_de_desarollo)
        case 4:
            print(mensaje_de_desarollo)
        case 5:
            print(mensaje_de_desarollo)
        case 6:
            print(mensaje_de_desarollo)
        case 7:
            print(mensaje_de_desarollo)
        case 8:
            print(mensaje_de_desarollo)
        case 0:
            print("\nSaliendo del programa...")
            condicion = False
        case _:
            print("ERROR! Valor invalido ingresado.")

"""

if len(lista) > 0:
        print("\n***** Lista de todos los jugadores del Dream Team *****\nIndice - Nombre Jugador\n-----------------------")
        listar_nombres_jugadores_con_indice(lista)
        indice_elegido = pedir_indice_jugador(lista)
        jugador_encontrado = encontrar_jugador_por_indice(lista, indice_elegido)
        mostrar_estadisticas_completas_un_jugador(jugador_encontrado)
        retorno = jugador_encontrado
    else:
        print("\nERROR! No hay elementos cargados en la lista para realizar esta operacion.")

"""