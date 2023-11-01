import json, csv
from jugador import Jugador
from funciones import validar_lista_Jugador

class Equipo():
    def __init__(self, path:str) -> None:
        self.equipo = self.cargar_lista_json(path)

    def cargar_lista_json(self, nombre_archivo_json:str) -> list:
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
        if self.verificar_existencia_archivo(nombre_archivo_json): 
            with open(nombre_archivo_json) as archivo:
                lista_cargada = json.load(archivo)
            return lista_cargada
    
    def verificar_existencia_archivo(self, path:str) -> bool:
        """
            Se encarga de verificar la existencia del archivo.

            Parametros
            ----------
            nombre_archivo_json : str
                La ubicacion del archivo en la computadora..
            
            Returns
            -------
            tipo : list
                Devuelve un True si la vreficacion fue exitosa, un False si no se puedo encontrar.
        """
        try:
            with open(path):
                print("El archico fue verificado exitosamente.")
                retorno = True
        except FileNotFoundError: 
            print("El archivo no existe.")
            retorno = False

        return retorno
    
    def cargar_lista_jugadores(self) -> list[Jugador]:
        lista_jugadores = []

        for jugador in self.equipo['jugadores']:
            jugador = Jugador(jugador['nombre'], jugador['posicion'], jugador['estadisticas'], jugador['logros'])
            lista_jugadores.append(jugador)

        return lista_jugadores
    
    def guardar_lista_jugadores_a_json(lista_jugadores:list[Jugador], nombre_archivo:str) -> int:
        """
            Genera un archivo de tipo JSON con los promedios de asistencias por partido de cada jugador. 

            Parametros:
            lista : list
                La lista de jugadores.
            nombre_del_archivo:str
                nombre del archivo
            
            Returns:
            tipo : int
                Retorna un numero entero (0) si algo salio mal, (1) si se pudo realizar la tarea con exito.
        """
        retorno = 0
        if validar_lista_Jugador(lista_jugadores) and nombre_archivo != None:
            lista_dict_jugadores = []
            for jugador in lista_jugadores:
                diccionario_aux = {}
                diccionario_aux[str(jugador.get_nombre())] = jugador.get_estadisticas().get_promedio_asistencias_por_partido()
                lista_dict_jugadores.append(diccionario_aux)

            with open(nombre_archivo, 'w') as archivo_json:
                json.dump(lista_dict_jugadores, archivo_json)
            print("El archivo JSON se pudo generar con exito!")
            retorno = 1

        return retorno
    
    def guardar_una_lista_en_csv(lista_jugadores:list[Jugador], nombre_del_archivo:str) -> int:
        """
            Genera un archivo de tipo CSV con los jugadores ordenados. 

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

        if validar_lista_Jugador(lista_jugadores) and nombre_del_archivo != None:
            titulos = ["Jugador","Promedio Asistencias"]

            with open(nombre_del_archivo, 'w', newline='') as archivo_csv:
                escritor_csv = csv.writer(archivo_csv)
                escritor_csv.writerow(titulos)
                for jugador in lista_jugadores:
                    lista_datos = [
                        jugador.get_nombre(),
                        jugador.get_estadisticas().get_promedio_asistencias_por_partido()
                    ]
                    escritor_csv.writerow(lista_datos)
            print("\nEl archivo CSV ORDENADO se pudo generar con exito!")
            retorno = 1
        else:
            print("\nERROR! No hay elementos cargados en la lista para mostrar.")
            retorno = 0
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

        if validar_lista_Jugador(lista_jugadores) and nombre_del_archivo != None:
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
            