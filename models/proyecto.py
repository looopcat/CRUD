class Proyecto:
    def __init__(self, id=None, nombre="", descripcion ="", fecha=""):
        self._id = id
        self._nombre = nombre
        self._descripcion = descripcion
        self._fecha = fecha

    # Getters
    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_descripcion(self):
        return self._descripcion
    
    def get_fecha(self):
        return self._fecha

    # Setters
    def set_id(self, id):
        self._id = id

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_descripcion(self, descripcion):
        self._descripcion = descripcion

    def get_fecha(self):
        return self._fecha

    def __str__(self) -> str:
        return self._nombre