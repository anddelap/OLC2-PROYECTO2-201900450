class Error:

    def __init__(self, num: int, description, ambito, fila: int, columna: int, hora):
        self.num = num
        self.description = description
        self.type = ambito
        self.fila = fila
        self.columna = columna
        self.hora = hora

    """ def getId(self):
        return self.id
    def getValue(self):
        return self.value
    def getType(self):
        return self.type
    def isArray(self):
        return self.array """