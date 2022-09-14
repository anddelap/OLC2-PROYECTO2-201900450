from Enum.transferSen import trasnferSen
from Enum.typeExpression import typeExpression
from Environment.Environment import Environment
from Environment.Symbol import Symbol
from Abstract.Expression import Expression

class Struct(Expression):
    def __init__(self, id, atributos, fila, columna):
        self.id = id
        self.atributos = atributos
        self.fila = fila
        self.columna = columna
    def execute(self, environment: Environment):
        environment.saveStruct(self.id, self, self.fila, self.columna)
