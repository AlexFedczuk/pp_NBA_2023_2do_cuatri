from estadisticas import Estadisticas

class Jugador():
    def __init__(self, nombre:str, posicion:str, estadisticas:dict, logros:list[str]) -> None:
        self.nombre = nombre
        self.posicion = posicion
        self.estadisticas = Estadisticas(estadisticas)
        self.logros = logros

    def get_nombre(self) -> str:
        return self.nombre
    
    def get_posicion(self) -> str:
        return self.posicion
    
    def get_estadisticas(self) -> Estadisticas:
        return self.estadisticas
    
    def get_logros(self) -> list[str]:
        return self.logros
    
    def set_nombre(self, nombre:str) -> None:
        self.nombre = nombre
    
    def set_posicion(self, posicion:str) -> None:
        self.posicion = posicion
    
    def set_estadisticas(self, estadisticas:Estadisticas) -> None:
        self.estadisticas = estadisticas
    
    def set_logros(self, logros:list[str]) -> None:
        self.logros = logros