class Marca:
    def __init__(self, nombre: str):
        self.Marca = nombre
    
    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nombre: str):
        self._nombre = nombre