class TV:
    _numTV = 0
    
    def __init__(self, marca, estado):
        self._marca = marca
        self._estado = estado
        self._canal = 1
        self._precio = 500
        self._volumen = 1
        self._control = None

        TV._numTV += 1
    
    
    def setMarca (self, marca):
        self.marca = marca
    
    def getMarca (self):
        return self._marca
    
    def setCanal (self, canal):
        self.canal = canal
    
    def getCanal (self):
        return self._canal
    
    def setPrecio (self, precio):
        self.precio = precio

    def getPrecio (self):
        return self._precio
    
    def setVolumen (self, volumen):
        self.volumen = volumen
    
    def getVolumen (self):
        return self._volumen
    
    def setControl (self, control):
        self.control = control
    
    def getControl (self):
        return self._control
    
    @classmethod
    def setNumTV (cls, numTV):
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
    
    def getEstado (self):
        return self._estado