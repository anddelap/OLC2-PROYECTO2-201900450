from Enum.transferSen import trasnferSen
from Environment.Environment import Environment
from Environment.Symbol import Symbol
from Abstract.Expression import Expression

class transSen(Expression):
    
    def __init__(self, type: trasnferSen, value: Expression):
        self.type = type
        self.value = value
        self.transfer = True
    def execute(self, environment: Environment) -> Symbol:
        return Symbol("", self.value, self.type,0,0)