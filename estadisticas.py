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

    def get_temporadas(self):
        return self.temporadas
    
    def get_puntos_totales(self):
        return self.puntos_totales
    
    def get_promedio_puntos_por_partido(self):
        return self.promedio_puntos_por_partido
    
    def get_rebotes_totales(self):
        return self.rebotes_totales
    
    def get_promedio_rebotes_por_partido(self):
        return self.promedio_rebotes_por_partido
    
    def get_asistencias_totales(self):
        return self.asistencias_totales
    
    def get_promedio_asistencias_por_partido(self):
        return self.promedio_asistencias_por_partido
    
    def get_robos_totales(self):
        return self.robos_totales
    
    def get_bloqueos_totales(self):
        return self.bloqueos_totales
    
    def get_porcentaje_tiros_de_campo(self):
        return self.porcentaje_tiros_de_campo
    
    def get_porcentaje_tiros_libres(self):
        return self.porcentaje_tiros_libres
    
    def get_porcentaje_tiros_triples(self):
        return self.porcentaje_tiros_triples
