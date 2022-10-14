from Environment.Symbol import Symbol
from Expression.Primitive import Primitive
from Environment.Environment import Environment
from Abstract.Expression import Expression
from Enum.typeExpression import typeExpression
from Abstract.Instruction import Instruction

class Parameter(Instruction):

    def __init__(self, id: str, tipo: typeExpression, fila, columna, pointer:bool, array:bool, vector:bool) -> None:
        self.id = id
        self.value = None
        self.fila=fila
        self.columna=columna
        self.transfer = False
        self.pointer = pointer
        self.array = array
        self.vector = vector
        self.tipo=tipo

    def setValue(self, value: Expression):
        self.value = value

    def execute(self, environment: Environment):
        tempValue = self.value.execute(environment)

        #if(self.tipo != None):
        #    environment.saveVariable(self.id,tempValue,tempValue.getType(),self.fila,self.columna, False, True, True)
        #else:

        #    environment.saveVariable(self.id,tempValue,self.tipo,self.fila,self.columna, False, True, True)
            

        