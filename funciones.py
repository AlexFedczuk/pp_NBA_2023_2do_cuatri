import json, re, csv

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

def pedir_un_nombre_regex(mensaje:str, mensaje_de_error:str) -> str:
    """
        Pide un numero nombre al usuario por la terminal.

        Parametros:
        mensaje:str
            El mensaje para instruir al usuario.
        mensaje_error:str
            El mensaje para instruir al usuario en caso de un error.
        
        Returns:
        tipo : int
            Retorna una variable tipo string vacia si sale algo mal, retorna una cadena con un nombre en el cas oque este bien validado.
    """
    retorno = ""
    patron = r"^[A-Za-z\s]+$"    

    while True:
        nombre_ingresado = input(mensaje)

        if re.match(patron, nombre_ingresado):
            retorno = formalizar_nombre_completo(nombre_ingresado)
            break
        else:
            print(mensaje_de_error)            
    return retorno

def formalizar_nombre_completo(nombre_completo:str) -> str:
    """
        Formaliza el nombre completo ingresado por parametros.

        Parametros:
        nombre_completo:str
            El nombre a formalizar.
        
        Returns:
        tipo : int
            Retorna el nombre formalizado.
    """
    nombre_completo = nombre_completo.lower()
    nombres = nombre_completo.split(" ")
    nombre_completo_aux = []

    for nombre_aux in nombres:
        nombre_completo_aux.append(nombre_aux.capitalize())
    nombre_formalizado = " ".join(nombre_completo_aux)

    return nombre_formalizado

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

def listar_nombres_jugadores_con_indice(lista_jugadores:list[Jugador]) -> int:
    """
        Lista todos los nombres de los jugadores del Dream Team con sus indices correspondientes. 

        Parametros:
        lista : list
            La lista con los nombres a listar con sus indices.
        
        Returns:
        tipo : int
            Retorna un numero entero (-1) si algo salio mal, (0) si la lista esta vacia o (1) si se pudo realizar la tarea con exito.
    """
    retorno = -1
    contador = 0

    if lista_jugadores != None:
        for jugador in lista_jugadores:
            print(f"{contador} - {jugador.get_nombre()}")
            contador+=1
    else:
        print("\nERROR! No hay elementos cargados en la lista para mostrar.")
        retorno = 0
    return retorno

def pedir_indice_jugador(lista_jugadores:list[Jugador]) -> int:
    """
        Pide al usuario que ingrese por la terminal el indice de un jugador del DT. 

        Parametros:
        lista : list
            La lista con los jugadores del DT.
        
        Returns:
        tipo : int
            Retorna un numero entero (-1) si algo salio mal, el indice del jugador si se pudo realizar la tarea con exito.
    """
    retorno = -1

    if lista_jugadores != None:
        while True:
            indice_ingresado = pedir_un_numero_entero_regex("Ingrese el indice del jugador que quiere mostrar sus estadisticas: ", "ERROR! Ha ingresado un valor invalido.")

            if indice_ingresado > -1 and indice_ingresado < len(lista_jugadores):
                retorno = indice_ingresado
                break
            else:
                print("ERROR! Ha ingresado un indice invalido, ingrese un indice que este dentro de la lista.")
    else:
        print("\nERROR! No hay elementos cargados en la lista como para pedir un indice.")
    return retorno

def encontrar_jugador_por_indice(lista_jugadores:list[Jugador], indice_a_buscar:int) -> dict:
    """
        Busca en la lista de jugadores del DT por un indice ingresado por parametros. 

        Parametros:
        lista:list
            La lista con los jugadores del DT.
        indice_a_buscar:int
            El indice del jugador a buscar.
        
        Returns:
        tipo : int
            Retorna un diccionario vacio si algo salio mal, devuelve el diccionario del jugador
            en el caso que se haya realizado la tarea con exito.
    """
    retorno = {}
    contador = 0

    if lista_jugadores != None and (indice_a_buscar > -1 and indice_a_buscar < len(lista_jugadores)):
        for jugador in lista_jugadores:
            if contador == indice_a_buscar:
                retorno = jugador
                break
            contador+=1
    else:
        print("\nERROR! No hay elementos cargados en la lista como para buscar un jugador.")

    return retorno

def mostrar_estadisticas_completas_un_jugador(jugador:Jugador) -> int:
    """
        Muestar todas las estadisticas del jugador ingresado por parametros.

        Parametros:
        jugador:dict
            El jugador a mostrar sus estadisticas.
        
        Returns:
        tipo : int
            Retorna un numero entero (-1) si salio algo mal, (0) si el diccionario esta vacio (1) si se pudo realizar la tarea con exito.
    """
    retorno = -1

    print(f"\n ***** Estadisticas completas de {jugador.get_nombre()} *****")
    estadisticas = jugador.get_estadisticas()
    print(f"Temporadas jugadas: {estadisticas.get_temporadas()}")
    print(f"Puntos totales: {estadisticas.get_puntos_totales()}")
    print(f"Promedio de puntos por partido: {estadisticas.get_promedio_puntos_por_partido()}")
    print(f"Rebotes totales: {estadisticas.get_rebotes_totales()}")
    print(f"Promedio de rebotes por partido: {estadisticas.get_promedio_rebotes_por_partido()}")
    print(f"Asistencias totales: {estadisticas.get_asistencias_totales()}")
    print(f"Promedio de asistencias por partido: {estadisticas.get_promedio_asistencias_por_partido()}")
    print(f"Robos totales: {estadisticas.get_robos_totales()}")
    print(f"Bloqueos totales: {estadisticas.get_bloqueos_totales()}")
    print(f"Porcentaje de tiros de campo: {estadisticas.get_porcentaje_tiros_de_campo()}")
    print(f"Porcentaje de tiros libres: {estadisticas.get_porcentaje_tiros_libres()}")
    print(f"Porcentaje de tiros triples: {estadisticas.get_porcentaje_tiros_triples()}")
    
    return retorno

def generar_archivo_csv(jugador:Jugador) -> int:
    """
        Genera un archivo tipo csv con toda las estadisticas de un jugar del DT.

        Parametros:
        jugador:dict
            El jugador a guardar sus estadisticas estadisticas.
        
        Returns:
        tipo : int
            Retorna un numero entero (-1) si salio algo mal, (1) en el caso que se haya podido generar el archivo con exito.
    """
    retorno = -1

    if jugador != None:
        nombre_del_csv = jugador.get_nombre() + ".csv"
        estadisticas_jugador = jugador.get_estadisticas()

        encabezado = ["Nombre",
            "Posición", 
            "Temporadas", 
            "Puntos totales", 
            "Promedio de puntos por partido", 
            "Rebotes totales", 
            "Promedio de rebotes por partido", 
            "Asistencias totales", 
            "Promedio de asistencias por partido", 
            "Robos totales", 
            "Bloqueos totales", 
            "Porcentaje de tiros de campo", 
            "Porcentaje de tiros libres", 
            "Porcentaje de tiros triples"
        ]
        estadisticas = [
            jugador.get_nombre(),
            jugador.get_posicion(),
            estadisticas_jugador.get_temporadas(),
            estadisticas_jugador.get_puntos_totales(),
            estadisticas_jugador.get_promedio_puntos_por_partido(),
            estadisticas_jugador.get_rebotes_totales(),
            estadisticas_jugador.get_promedio_rebotes_por_partido(),
            estadisticas_jugador.get_asistencias_totales(),
            estadisticas_jugador.get_promedio_asistencias_por_partido(),
            estadisticas_jugador.get_robos_totales(),
            estadisticas_jugador.get_bloqueos_totales(),
            estadisticas_jugador.get_porcentaje_tiros_de_campo(),
            estadisticas_jugador.get_porcentaje_tiros_libres(),
            estadisticas_jugador.get_porcentaje_tiros_triples()
            ]
        with open(nombre_del_csv, 'w', newline='') as archivo_csv:
            writer = csv.writer(archivo_csv)
            writer.writerow(encabezado)
            writer.writerow(estadisticas)
        print("\nEl archivo CSV ya se ha generado con exito!")
        retorno = 1
    else:
        print("\nERROR! No hay elementos cargados como para ejecutar esta opción. Realice una operación en la opción 2 antes de realizar una operación en la opción 3.")
        retorno = 0
    return retorno

def encontrar_jugador_por_nombre(lista_jugador:list[Jugador], nombre_a_buscar:str) -> Jugador:
    """
        Busca en la lista de jugadores del DT por un nombre ingresado por parametros. 

        Parametros:
        lista:list
            La lista con los jugadores del DT.
        nombre_a_buscar:str
            El nombre del jugador a buscar.
        
        Returns:
        tipo : int
            Retorna un diccionario vacio si algo salio mal, devuelve el diccionario del jugador
            encontrado en el caso que se haya realizado la tarea con exito.
    """
    retorno = {}

    if lista_jugador != None:
        for jugador in lista_jugador:
            if jugador.get_nombre() == nombre_a_buscar:
                retorno = jugador
                break
    else:
        print("\nERROR! No hay elementos cargados en la lista como para buscar un jugador.")

    return retorno

def mostrar_logros_un_jugador(jugador:Jugador) -> int:
    """
        Muestar todos los logros del jugador ingresado por parametros.

        Parametros:
        jugador:dict
            El jugador a mostrar sus logros.
        
        Returns:
        tipo : int
            Retorna un numero entero (-1) si salio algo mal, (0) si el diccionario esta vacio (1) si se pudo realizar la tarea con exito.
    """
    retorno = -1
    logros = jugador.get_logros()

    if jugador != {}:
        for logro in logros:
            print(f"{logro}")
        retorno = 1
    else:
        print("ERROR! No se han encontrado logros del jugador indicado.")
        retorno = 0
    
    return retorno

def calcular_promedio(lista_jugadores:list[Jugador]) -> float:
    """
        Calcula el promedio de un total de una estadistica indicada por una clave por parametros.

        Parametros:
        lista : list
            La lista con los datos necesarios para calcular un promedio.
        clave:str
            La clave que indica de que estadistica hay que calcular el promedio.
        
        Returns:
        tipo : float
            Devuelve el promedio calculado.
    """
    retorno = -1

    if lista_jugadores != None:
        acumulador = 0
        for jugador in lista_jugadores:
            acumulador = acumulador + jugador.get_estadisticas().get_promedio_puntos_por_partido()
        promedio = round(float(acumulador/len(lista_jugadores)), 2)
        retorno = promedio
    else:
        print("ERROR! No hay datos en la lista como para realizar un promedio.")
        retorno = 0

    return retorno

def comprobar_logro_en_un_jugador(jugador:Jugador, palabra_clave:str) -> bool:
    """
        Comprueba si el jugador del DT tiene x logro usando una palabra o frase clave.

        Parametros:
        jugador:dict
            El jugador a analizar.
        palabra_clave:str
            Palabra clave para chequear en sus logros.

        Returns:
        tipo : bool
            Deveulve True en el caso que se compruebe que el jugador tiene x logro indicado, False en el caso que no
    """
    logros = jugador.get_logros()
    for logro in logros:
        if palabra_clave.lower() in logro.lower():
            retorno = True
            break
        else:
            retorno = False
    return retorno

def encontrar_jugador_por_mayor_valor(lista_jugadores:list[Jugador]) -> Jugador:
    """
        Busca al jugador con el valor mas alto de la estadistica indicada por una clave.

        Parametros:
        lista:list
            La lista con los jugadores el DT.
        clave:str
            La estadistica indicada a por clave.
        
        Returns:
        tipo : int
            Devuelve el jugador encontrado mediante un diccionarion en el caso que no
            se haya podido encontrar devuleve un diccionario vacio.
    """
    retorno = {}

    if lista_jugadores != None:
        jugador_maximo = calcular_jugador_con_mayor_valor(lista_jugadores)
        retorno = jugador_maximo
    else:
        print(f"ERROR! No hay datos en la lista como para encontrar un jugador por 'metodo'.")

    return retorno

def calcular_jugador_con_mayor_valor(lista_jugadores:list[Jugador]) -> Jugador:
    """
        Calcula cual es el jugador con el valor mas alto de la estadistica indicada por una clave.

        Parametros:
        lista:list
            La lista con los jugadores el DT.
        clave:str
            La estadistica indicada a por clave.
        
        Returns:
        tipo : int
            Devuelve el jugador calculado con el valor mas alto, en el caso que no
            se haya podido calcular devuleve un diccionario vacio.
    """
    retorno = {}
    jugador_maximo = None
    bandera = 0

    if lista_jugadores != None:
        for jugador in lista_jugadores:
            if bandera == 0 or jugador_maximo.get_estadisticas().get_rebotes_totales() < jugador.get_estadisticas().get_rebotes_totales():
                jugador_maximo = jugador
                bandera = 1
    else:
        print(f"ERROR! No hay datos en la lista como para encontrar un jugador por 'metodo'.")

    retorno = jugador_maximo

    return retorno

def guardar_nueva_lista_en_csv(lista_jugadores:list[Jugador], nombre_del_archivo:str) -> int:
    """
        Genera un archivo de tipo CSV con los puntos totales de cada jugador. 

        Parametros:
        lista : list
            La lista con los nombres a listar con sus posiciones.
        nombre_del_archivo:str
            nombre del archivo
        
        Returns:
        tipo : int
            Retorna un numero entero (-1) si algo salio mal, (0) si la lista esta vacia o (1) si se pudo realizar la tarea con exito.
    """
    retorno = -1

    if lista_jugadores != None and nombre_del_archivo != None:
        titulos = ["Jugador","Puntos","Rebotes","Asistencias","Robos"]

        with open(nombre_del_archivo, 'w', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            escritor_csv.writerow(titulos)
            for jugador in lista_jugadores:
                lista_datos = [
                    jugador.get_nombre(),
                    jugador.get_estadisticas().get_puntos_totales(),
                    jugador.get_estadisticas().get_rebotes_totales(),
                    jugador.get_estadisticas().get_asistencias_totales(),
                    jugador.get_estadisticas().get_robos_totales()
                    ]
                escritor_csv.writerow(lista_datos)
        print("\nEl archivo CSV se pudo generar con exito!")
        retorno = 1
    else:
        print("\nERROR! No hay elementos cargados en la lista para mostrar.")
        retorno = 0
    return retorno