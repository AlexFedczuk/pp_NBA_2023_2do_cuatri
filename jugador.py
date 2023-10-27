from estadisticas import Estadisticas

class Jugador():
    def __init__(self, nombre:str, posicion:str, estadisticas:dict, logros:list) -> None:
        self.nombre = nombre
        self.posicion = posicion
        self.estadisticas = Estadisticas(estadisticas)
        self.logros = logros

    def get_nombre(self) -> str:
        return self.nombre
    
    def get_posicion(self) -> str:
        return self.posicion
    
    def get_estadisticas(self) -> dict:
        return self.estadisticas
    
    def get_logros(self) -> list:
        return self.logros