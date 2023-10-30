class Estadisticas():
    def __init__(self, estadisticas:dict) -> None:
        self.temporadas = estadisticas['temporadas'] 
        self.puntos_totales = estadisticas['puntos_totales'] 
        self.promedio_puntos_por_partido = estadisticas['promedio_puntos_por_partido'] 
        self.rebotes_totales = estadisticas['rebotes_totales'] 
        self.promedio_rebotes_por_partido = estadisticas['promedio_rebotes_por_partido'] 
        self.asistencias_totales = estadisticas['asistencias_totales'] 
        self.promedio_asistencias_por_partido = estadisticas['promedio_asistencias_por_partido'] 
        self.robos_totales = estadisticas['robos_totales'] 
        self.bloqueos_totales = estadisticas['bloqueos_totales'] 
        self.porcentaje_tiros_de_campo = estadisticas['porcentaje_tiros_de_campo'] 
        self.porcentaje_tiros_libres = estadisticas['porcentaje_tiros_libres'] 
        self.porcentaje_tiros_triples = estadisticas['porcentaje_tiros_triples']

    def get_temporadas(self) -> int:
        return self.temporadas
    
    def get_puntos_totales(self) -> int:
        return self.puntos_totales
    
    def get_promedio_puntos_por_partido(self) -> float:
        return self.promedio_puntos_por_partido
    
    def get_rebotes_totales(self) -> int:
        return self.rebotes_totales
    
    def get_promedio_rebotes_por_partido(self) -> float:
        return self.promedio_rebotes_por_partido
    
    def get_asistencias_totales(self) -> int:
        return self.asistencias_totales
    
    def get_promedio_asistencias_por_partido(self) -> float:
        return self.promedio_asistencias_por_partido
    
    def get_robos_totales(self) -> int:
        return self.robos_totales
    
    def get_bloqueos_totales(self) -> int:
        return self.bloqueos_totales
    
    def get_porcentaje_tiros_de_campo(self) -> float:
        return self.porcentaje_tiros_de_campo
    
    def get_porcentaje_tiros_libres(self) -> float:
        return self.porcentaje_tiros_libres
    
    def get_porcentaje_tiros_triples(self) -> float:
        return self.porcentaje_tiros_triples
    
    def get_temporadas(self, temporadas:int) -> None:
        self.temporadas = temporadas
    
    def get_puntos_totales(self, puntos_totales:int) -> None:
        self.puntos_totales = puntos_totales
    
    def get_promedio_puntos_por_partido(self, promedio_puntos_por_partido:float) -> None:
        self.promedio_puntos_por_partido = promedio_puntos_por_partido
    
    def get_rebotes_totales(self, rebotes_totales:int) -> None:
        self.rebotes_totales = rebotes_totales
    
    def get_promedio_rebotes_por_partido(self, promedio_rebotes_por_partido:float) -> None:
        self.promedio_rebotes_por_partido = promedio_rebotes_por_partido
    
    def get_asistencias_totales(self, asistencias_totales:int) -> None:
        self.asistencias_totales = asistencias_totales
    
    def get_promedio_asistencias_por_partido(self, promedio_asistencias_por_partido:float) -> None:
        self.promedio_asistencias_por_partido = promedio_asistencias_por_partido
    
    def get_robos_totales(self, robos_totales:int) -> None:
        self.robos_totales = robos_totales
    
    def get_bloqueos_totales(self, bloqueos_totales:int) -> None:
        self.bloqueos_totales = bloqueos_totales
    
    def get_porcentaje_tiros_de_campo(self, porcentaje_tiros_de_campo:float) -> None:
        self.porcentaje_tiros_de_campo = porcentaje_tiros_de_campo
    
    def get_porcentaje_tiros_libres(self, porcentaje_tiros_libres:float) -> None:
        self.porcentaje_tiros_libres = porcentaje_tiros_libres
    
    def get_porcentaje_tiros_triples(self, porcentaje_tiros_triples:float) -> None:
        self.porcentaje_tiros_triples = porcentaje_tiros_triples
