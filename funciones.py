import json, re

from jugador import Jugador

def cargar_lista_json(nombre_archivo_json:str) -> list:
    """
        Se encarga de cargar toda la informacion que esta en el archivo json en una lista.

        Parametros
        ----------
        nombre_archivo_json : str
            El nombre del archivo json a cargar.
        
        Returns
        -------
        tipo : list
            Devuelve una lista vacia en caso de que no se haya podido cargar la lista.
            En el caso de que se ya haya realizado con exito la funcion, devuelve una lista caragda.
    """
    lista_cargada = []
    #if verificar_nombre_archivo(nombre_archivo_json): 
    with open(nombre_archivo_json) as archivo:
        lista_cargada = json.load(archivo)
    return lista_cargada

def mostrar_menu_principal():
    """
        Muestra las opciones del menu principal.

        Parametros
        ----------
        void
        
        Returns
        -------
        void
    """
    print("\n ---------- Menú Principal del 'Dream Team' ----------\n")
    print("1. Mostrar la lista de todos los jugadores del Dream Team.")
    print("2. Mostrar un jugador con sus estadisticas completas.")
    print("3. Guardar las estadisticas del jugador selecionado (en la opcion 2) en un archivo CSV.")
    print("4. Buscar un jugador por su nombre y mostrar sus logros.")
    print("5. Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream Team.")
    print("6. Ingresar el nombre de un jugador (validar con regex) y mostrar si ese jugador es miembro del Salón de la Fama del Baloncesto.")
    print("7. Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.")
    print("8. Exportar a CSV.")
    print("0. Salir del programa")

def pedir_un_numero_entero_regex(mensaje:str, mensaje_error:str) -> int:
    """
        Pide un numero de tipo entero usando expresiones regulares.

        Parametros:
        mensaje:str
            El mensaje para instruir al usuario.
        mensaje_error:str
            El mensaje para instruir al usuario en caso de un error.
        
        Returns:
        tipo : int
            El valor ingresado por el usuario validado.
    """
    while True:
        data_ingresada = input(mensaje)
        resultado = validar_numero_entero(data_ingresada)
        if resultado == True:
            retorno = int(data_ingresada)
            break
        else:
            print(mensaje_error)
    return retorno

def validar_numero_entero(cadena:str) -> bool:
    """
        Valida si la cadena pasada por parametros representa un numero entero.

        Parametros:
        cadena:str
            La cadena a validar.
        
        Returns:
        tipo : bool
            Devuelve True en el caso que la cadena represente un numero entero, False en el caso de que no.
    """
    patron = r"^-?\d+$"

    if re.match(patron, cadena):
        retorno = True
    else:
        retorno = False
    return retorno

def listar_nombres_jugadores_con_posiciones(lista:list[Jugador]) -> int:
    """
        Lista todos los nombres de los jugadores del Dream Team con sus posiciones. 

        Parametros:
        lista : list
            La lista con los nombres a listar con sus posiciones.
        
        Returns:
        tipo : int
            Retorna un numero entero (-1) si algo salio mal, (0) si la lista esta vacia o (1) si se pudo realizar la tarea con exito.
    """
    retorno = -1

    if len(lista) > 0:
        for jugador in lista:
            print(f"{jugador.get_nombre()} - {jugador.get_posicion()}")
    else:
        print("\nERROR! No hay elementos cargados en la lista para mostrar.")
        retorno = 0
    return retorno