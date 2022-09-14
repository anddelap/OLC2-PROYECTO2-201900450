from Environment.Symbol import Symbol
from Expression.Primitive import Primitive
from Environment.Environment import Environment
from Abstract.Expression import Expression
from Enum.typeExpression import typeExpression

class VariableCall(Expression):
    def __init__(self, id: str, fila,columna) -> None:
        self.id = id
        self.fila = fila
        self.columna = columna
        
    def execute(self, environment: Environment) -> Symbol:
        retValue = environment.getVariable(self.id)
        #print(retValue.getType())
        if(retValue == None):
            archivo = open("Salida.txt", "a")
            archivo.write("Error: la variable "+ str(self.id) + " no existe\n")
            archivo.close()
            Environment.saveError("Error: la variable "+ str(self.id) + " no existe",'Local', self.fila, self.columna)
            retValue = Primitive(0,typeExpression.INTEGER).execute(environment)

        return retValue
