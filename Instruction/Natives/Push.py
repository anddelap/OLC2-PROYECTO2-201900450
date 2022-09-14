from Enum.typeExpression import typeExpression
from Environment.Symbol import Symbol
from Environment.Environment import Environment
from Abstract.Instruction import Instruction
from Abstract.Expression import Expression
from Expression.Primitive import Primitive

class Push(Instruction):
    def __init__(self, Exp: Expression, Exp2: Expression,fila,columna)-> None:
        self.Exp = Exp
        self.Exp2 = Exp2
        self.fila = fila
        self.columna = columna
    def execute(self, environment: Environment):
        List = self.Exp.execute(environment)
        tempValue = self.Exp2.execute(environment)
        if(List.getType()==typeExpression.VECTOR ):
            if(List.isMutable):
                if(List.getVectorCapacity()==0):
                    List.getValue().append(tempValue)
                elif(List.getVectorCapacity().execute(environment).getValue()):
                        if(len(List.getValue())<List.getVectorCapacity().execute(environment).getValue()):
                            List.getValue().append(tempValue)
                        else:
                            List.VectorCapacity = Primitive(List.getVectorCapacity().execute(environment).getValue()*2,typeExpression.INTEGER)
                            List.getValue().append(tempValue)
            else:
                archivo = open("Salida.txt", "a")
                archivo.write("Error: No se puede hacer push en un vector no mutable\n")
                archivo.close()
                Environment.saveError("Error: No se puede hacer push en un vector no mutable", 'Local', self.fila, self.columna)
        else:
            archivo = open("Salida.txt", "a")
            archivo.write("Error: push es solo para vectores\n")
            archivo.close()
            Environment.saveError("Error: push es solo para vectores", 'Local', self.fila, self.columna)