from Enum.typeExpression import typeExpression
from Enum.arithmeticOperation import arithmeticOperation
from Enum.Dominant import Dominant
from Environment.Environment import Environment
from Environment.Symbol import Symbol
from Abstract.Expression import Expression

class Array(Expression):

    def __init__(self, exp, cantidad, listExp, fila, columna) -> None:
        self.listExp = listExp
        self.fila = fila
        self.columna = columna
        self.exp = exp
        self.cantidad = cantidad

    def execute(self, environment: Environment) -> Symbol:
        if(self.exp != None and self.cantidad != None):
            cant = self.cantidad.execute(environment)
            if(cant.getType() == typeExpression.INTEGER):
                tempExp = []
                for i in range(0, int(cant.getValue())):
                    tempExp.append(self.exp.execute(environment))
                tempSymbol: Symbol = Symbol('',tempExp,typeExpression.ARRAY,self.fila,self.columna)
                tempSymbol.array = True
                return tempSymbol
            else:
                archivo = open("Salida.txt", "a")
                archivo.write("Error: la cantidad debe de ser Integer\n")
                archivo.close()
                #archivo = open("Errores/Errores.txt", "a")
                #archivo.write("No es posible realizar la operacion raiz con "+ str(Value.getValue()) +"\n")
                #archivo.close()
                Environment.saveError("Error: la cantidad debe de ser Integer", 'Local', self.fila, self.columna)
                tempExp = []
                tempSymbol: Symbol = Symbol('',tempExp,typeExpression.ARRAY,self.fila,self.columna)
                tempSymbol.array = True
                return tempSymbol
        elif(self.listExp!=None):
            tempExp = []
            for exp in self.listExp:
                tempExp.append(exp.execute(environment))

            tempSymbol: Symbol = Symbol('',tempExp,typeExpression.ARRAY,self.fila,self.columna)
            tempSymbol.array = True

            return tempSymbol