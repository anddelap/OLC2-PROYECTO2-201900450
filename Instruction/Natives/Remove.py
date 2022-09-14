from pickle import LIST
from Enum.typeExpression import typeExpression
from Environment.Environment import Environment
from Environment.Symbol import Symbol
from Abstract.Expression import Expression
from Enum.nativeFunction import nativeFunction
from Expression.Array import Array
from Expression.Primitive import Primitive

class Remove(Expression):
    def __init__(self, Exp: Expression, Exp2: Expression,fila,columna)-> None:
        self.Exp = Exp
        self.Exp2 = Exp2
        self.fila = fila
        self.columna = columna
    def execute(self, environment: Environment)->Symbol:
        List = self.Exp.execute(environment)
        tempValue = self.Exp2.execute(environment)
        posicion = 0
        if(List.getType()==typeExpression.VECTOR ):
            if(List.isMutable):
                for i in range(0,len(List.getValue())):
                    if(i==tempValue.getValue()):
                        posicion = i
                        break
                value = List.getValue()[posicion]
                List.getValue().pop(tempValue.getValue())
                return value
            else:
                archivo = open("Salida.txt", "a")
                archivo.write("Error: No se puede remover en un vector no mutable\n")
                archivo.close()
                Environment.saveError("Error: No se puede remover en un vector no mutable", 'Local', self.fila, self.columna)
        else:
            archivo = open("Salida.txt", "a")
            archivo.write("Error: remove es solo para vectores\n")
            archivo.close()
            Environment.saveError("Error: remove es solo para vectores", 'Local', self.fila, self.columna)
        return Symbol("",0,typeExpression.INTEGER,0,0)