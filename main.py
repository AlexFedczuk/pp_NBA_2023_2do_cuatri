from funciones import mostrar_menu_principal, pedir_un_numero_entero_regex
from equipo import Equipo

ubicacion_archivo_dt_json = "dream_team.json"
mensaje_de_desarollo = "\nEsta opcion esta en desarrollo..."

dream_team = Equipo()
lista_dt = dream_team.cargar_lista_json(ubicacion_archivo_dt_json)
lista_jugadores = lista_dt['jugadores']
ultimo_jugador_opcion_dos = {}

condicion = True
while condicion:
    mostrar_menu_principal()
    opcion_menu = pedir_un_numero_entero_regex("Ingrese una opcion del menu: ", "ERROR! Ha ingresado un valor invalido.")
    
    match opcion_menu:
        case 1:
            print(mensaje_de_desarollo)
        case 2:
            print(mensaje_de_desarollo)
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
            print("Saliendo del programa...")
            condicion = False
        case _:
            print("ERROR! Valor invalido ingresado.")