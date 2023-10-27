import json
from jugador import Jugador

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
            