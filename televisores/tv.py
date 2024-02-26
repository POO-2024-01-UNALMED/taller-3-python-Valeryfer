class TV:
    _numTV = 0
    def __init__(self, marca, canal, precio, estado, volumen, control):
        self.marca = marca
        self.canal = 1
        self.precio = 500
        self.estado = estado
        self.volumen = 1
        self.control = control
    
    def __init__(self, marca, estado):
        self.marca = marca
        self.estado = estado
    
    def setMarca (self, marca):
        self.marca = marca
    
    def getMarca (self):
        return self.marca
    
    def setCanal (self, canal):
        self.canal = canal
    
    def getCanal (self):
        return self.canal
    
    def setPrecio (self, precio):
        self.precio = precio

    def getPrecio (self):
        return self.precio
    
    def setVolumen (self, volumen):
        self.volumen = volumen
    
    def getVolumen (self):
        return self.volumen
    
    def setControl (self, control):
        self.control = control
    
    
    def getControl (self):
        return self.control
    
    @classmethod
    def setNumTV (cls, numTV: int):
        cls._numTV = numTV
    
    @classmethod
    def getNumTV (cls):
        return cls._numTV
    
    def turnOn (self):
        self._estado = True

    def turnOff (self):
        self._estado = False
    
    def canalUp (self):
        self.setCanal(self._canal + 1)

    def canalDown (self):
        self.setCanal(self._canal - 1)
    
    def volumenUp (self):
        self.setVolumen(self._volumen + 1)
    
    def volumenDown (self):
        self.setVolumen(self._volumen - 1)