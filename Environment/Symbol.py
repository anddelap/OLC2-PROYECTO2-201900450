class Symbol:
    #Los simbolos poseen id, valor y tipo
    def __init__(self, id: str, value, type, fila: int, columna: int):
        self.id = id
        self.value = value
        self.type = type
        self.fila = fila
        self.columna = columna
        self.array = False
        self.mutable = False
        self.VectorCapacity = 0

    def getId(self):
        return self.id
    def getValue(self):
        return self.value
    def getType(self):
        return self.type
    def isArray(self):
        return self.array
    def isMutable(self):
        return self.mutable
    def getVectorCapacity(self):
        return self.VectorCapacity