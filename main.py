from funciones import mostrar_menu_principal, pedir_un_numero_entero_regex
from equipo import Equipo
from controladores import *

ubicacion_archivo_dt_json = "dream_team.json"
mensaje_de_desarollo = "\nEsta opcion esta en desarrollo..."

dream_team = Equipo(ubicacion_archivo_dt_json)
lista_jugadores = dream_team.cargar_lista_jugadores()

ultimo_jugador_opcion_dos = None

condicion = True
while condicion:
    mostrar_menu_principal()
    opcion_menu = pedir_un_numero_entero_regex("Ingrese una opcion del menu: ", "ERROR! Ha ingresado un valor invalido.")
    
    match opcion_menu:
        case 1:
            controlador_opcion_uno(lista_jugadores)
        case 2:
            ultimo_jugador_opcion_dos = controlador_opcion_dos(lista_jugadores)
        case 3:
            controlador_opcion_tres(ultimo_jugador_opcion_dos)
        case 4:
            controlador_opcion_cuatro(lista_jugadores)
        case 5:
            controlador_opcion_cinco(lista_jugadores)
        case 6:
            controlador_opcion_seis(lista_jugadores)
        case 7:
            controlador_opcion_siete(lista_jugadores)
        case 8:
            controlador_opcion_ocho(lista_jugadores)
        case 9:
            controlador_opcion_nueve(lista_jugadores)
        case 10:
            controlador_opcion_diez(lista_jugadores)
        case 11:
            controlador_opcion_once(lista_jugadores)
        case 0:
            print("\nSaliendo del programa...")
            condicion = False
        case _:
            print("ERROR! Valor invalido ingresado.")