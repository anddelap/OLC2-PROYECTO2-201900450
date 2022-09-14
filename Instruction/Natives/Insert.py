from Enum.typeExpression import typeExpression
from Environment.Symbol import Symbol
from Environment.Environment import Environment
from Abstract.Instruction import Instruction
from Abstract.Expression import Expression

class Insert(Instruction):
    def __init__(self,  Exp: Expression, Exp1: Expression, Exp2: Expression,fila,columna)-> None:
        self.Exp = Exp
        self.Exp1 = Exp1
        self.Exp2 = Exp2
        self.fila = fila
        self.columna = columna
    def execute(self, environment: Environment):
        List = self.Exp.execute(environment)
        position = self.Exp1.execute(environment)
        tempValue = self.Exp2.execute(environment)
        if(List.getType()==typeExpression.VECTOR ):
            if(List.isMutable):
                if(position.getType()==typeExpression.INTEGER):
                    List.getValue().insert(position.getValue(),tempValue)
                else:
                    archivo = open("Salida.txt", "a")
                    archivo.write("Error: la posicion debe de ser Integer\n")
                    archivo.close()
                    Environment.saveError("Error: la posicion debe de ser Integer", 'Local', self.fila, self.columna)
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