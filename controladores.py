from jugador import Jugador
from funciones import *


def controlador_opcion_uno(lista_jugadores:list[Jugador]) -> int:
    """
        Se encarga de contener todas las funciones necesarias para 
        realizar el algoritmo de la opcion 1 del menu principal.

        Parametros:
        lista : list
            Una lista de variables, en este caso serian jugadores del Dream Team.
        
        Returns:
            Retorna un numero entero (0) si algo salio mal, (1) si se pudo realizar la tarea con exito.
    """
    retorno = 0

    if validar_lista_Jugador(lista_jugadores):
        print("\nJugadores con sus Posiciones:\n****************************")
        listar_nombres_jugadores_con_posiciones(lista_jugadores)
        retorno = 1

    return retorno

def controlador_opcion_dos(lista_jugadores:list[Jugador]) -> Jugador:
    """
        Se encarga de contener todas las funciones necesarias para 
        realizar el algoritmo de la opcion 2 del menu principal.

        Parametros:
        lista : list
            Una lista de variables, en este caso serian jugadores del Dream Team.
        
        Returns:
            Retorna una variable vacia si algo salio mal, un objeto clase Jugador con la informacion
            del jugador seleccionado en la opcion 2.
    """
    retorno = None

    if validar_lista_Jugador(lista_jugadores):
        print("\n***** Lista de todos los jugadores del Dream Team *****\nIndice - Nombre Jugador\n-----------------------")
        listar_nombres_jugadores_con_indice(lista_jugadores)
        indice_elegido = pedir_indice_jugador(lista_jugadores)
        jugador_encontrado = encontrar_jugador_por_indice(lista_jugadores, indice_elegido)
        mostrar_estadisticas_completas_un_jugador(jugador_encontrado)
        retorno = jugador_encontrado

    return retorno

def controlador_opcion_tres(jugador:Jugador) -> int:
    """
        Se encarga de contener todas las funciones necesarias para 
        realizar el algoritmo de la opcion 3 del menu principal.

        Parametros:
        jugador : dict
            Un diccionario con la informacion del jugador seleccionado en la opcion 2.
        
        Returns:
        Retorna un numero entero (-1) si algo salio mal, (0) si la lista esta vacia o (1) si se pudo realizar la tarea con exito.
    """
    retorno = -1    

    if jugador != None:
        generar_archivo_csv(jugador)
        retorno = 1
    else:
        print("\nERROR! No hay elementos cargados como para ejecutar esta opción. Realice una operación en la opción 2 antes de realizar una operación en la opción 3.")
        retorno = 0
    return retorno

def controlador_opcion_cuatro(lista_jugadores:list[Jugador]) -> int:
    """
        Se encarga de contener todas las funciones necesarias para 
        realizar el algoritmo de la opcion 4 del menu principal.

        Parametros:
        lista : list
            Una lista de variables, en este caso serian jugadores del Dream Team.
        
        Returns:
        Retorna un numero entero (0) si algo salio mal, (1) si se pudo realizar la tarea con exito.
    """
    retorno = 0

    if validar_lista_Jugador(lista_jugadores):
        nombre_ingresado = pedir_un_nombre_regex("\nIngrese el nombre del jugador que quiere buscar: ",
                                                 "\nERROR! Ha ingresado un valor invalido. Ingrese caracteres alfabeticos.")
        jugador_encontrado = encontrar_jugador_por_nombre(lista_jugadores, nombre_ingresado)
        print(f"\n ***** Todos los logros de {jugador_encontrado.get_nombre()} *****")
        mostrar_logros_un_jugador(jugador_encontrado)
        retorno = 1
    else:
        print("\nERROR! No hay elementos cargados en la lista para realizar esta operacion.")

    return retorno

def controlador_opcion_cinco(lista_jugadores:list[Jugador]) -> int:
    """
        Se encarga de contener todas las funciones necesarias para 
        realizar el algoritmo de la opcion 5 del menu principal.

        Parametros:
        lista : list
            Una lista de variables, en este caso serian jugadores del Dream Team.
        
        Returns:
        Retorna un numero entero (0) si algo salio mal, (1) si se pudo realizar la tarea con exito.
    """
    retorno = 0

    if validar_lista_Jugador(lista_jugadores):
        promedio = calcular_promedio(lista_jugadores)
        print(f"\nEl promedio de puntos por partido de todo el equipo del Dream Team: {promedio}")
        lista_jugadores_ordenanda = ordenar_jugadores_por_nombre(lista_jugadores)# Falta una cosa mas en este controlador. Revisar las consignas!
        print("Lista de jugadores ordenada: \n****************************")
        for jugador in lista_jugadores_ordenanda:
            print(f"{jugador.get_nombre()}")
        retorno = 1
    else:
        print("\nERROR! No hay elementos cargados en la lista para realizar esta operacion.")

    return retorno

def controlador_opcion_seis(lista_jugadores:list[Jugador]) -> int:
    """
        Se encarga de contener todas las funciones necesarias para 
        realizar el algoritmo de la opcion 6 del menu principal.

        Parametros:
        lista : list
            Una lista de variables, en este caso serian jugadores del Dream Team.
        
        Returns:
        Retorna un numero entero (-1) si algo salio mal, (0) si la lista esta vacia o (1) si se pudo realizar la tarea con exito.
    """
    retorno = -1

    if validar_lista_Jugador(lista_jugadores):
        nombre_ingresado = pedir_un_nombre_regex("\nIngrese el nombre del jugador que quiere buscar: ",
                                                 "\nERROR! Ha ingresado un valor invalido. Ingrese caracteres alfabeticos.")
        
        palabra_clave = "Salon de la Fama del Baloncesto"

        jugador_encontrado = encontrar_jugador_por_nombre(lista_jugadores, nombre_ingresado)

        if comprobar_logro_en_un_jugador(jugador_encontrado, palabra_clave):
            print(f"\nEl jugador {jugador_encontrado.get_nombre()} es perteneciente al {palabra_clave}.")
        else:
            print(f"\nEl jugador {jugador_encontrado.get_nombre()} no es perteneciente al {palabra_clave}.")
        retorno = 1
    else:
        print("\nERROR! No hay elementos cargados en la lista para realizar esta operacion.")
        retorno = 0

    return retorno

def controlador_opcion_siete(lista_jugadores:list[Jugador]) -> int:
    """
        Se encarga de contener todas las funciones necesarias para 
        realizar el algoritmo de la opcion 7 del menu principal.

        Parametros:
        lista : list
            Una lista de variables, en este caso serian jugadores del Dream Team.
        
        Returns:
        Retorna un numero entero (0) si algo salio mal, (1) si se pudo realizar la tarea con exito.
    """
    retorno = 0

    if validar_lista_Jugador(lista_jugadores):
        jugador_encontrado = encontrar_jugador_por_mayor_valor(lista_jugadores)
        print(f"\nEl jugador con la mayor cantidad de rebotes totales es {jugador_encontrado.get_nombre()}, con un total de {jugador_encontrado.get_estadisticas().get_rebotes_totales()}.")
        retorno = 1
    else:
        print("\nERROR! No hay elementos cargados en la lista para realizar esta operacion.")
        retorno = 0

    return retorno

def controlador_opcion_ocho(lista_jugadores:list[Jugador]) -> int:
    """
        Se encarga de guardar un archivo csv con los puntos totales
        de cada jugador.

        Parametros:
        lista : list
            Una lista de variables, en este caso serian jugadores del Dream Team.
        
        Returns:
        Retorna un numero entero (0) si algo salio mal, (1) si se pudo realizar la tarea con exito.
    """
    retorno = 0

    if validar_lista_Jugador(lista_jugadores):
        guardar_nueva_lista_en_csv(lista_jugadores, "jugadores_del_DT_y_sus_puntos.csv")
        retorno = 1
    else:
        print("\nERROR! No hay elementos cargados en la lista para realizar esta operacion.")
        retorno = 0

    return retorno