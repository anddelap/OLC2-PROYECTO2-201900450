from Enum.typeExpression import typeExpression
from Environment.Environment import Environment
from Environment.Symbol import Symbol
from Abstract.Expression import Expression
from Enum.nativeFunction import nativeFunction
from Expression.Array import Array
from Expression.Primitive import Primitive

class StructAccess(Expression):
    def __init__(self, id1: str, id2: str, fila, columna) -> None:
        self.id1 = id1
        self.id2 = id2
        self.fila = fila
        self.columna = columna
    
    def execute(self, environment: Environment) -> Symbol:
        Struct = self.id1.execute(environment)
        if(isinstance(Struct.getType(), list)):
            if(Struct.getType()[0] == typeExpression.STRUCT):
                encontro = False
                for i in range(0,len(Struct.getValue()[1])):
                    if(Struct.getValue()[1][i][0] == self.id2):
                        encontro = True
                        return Struct.getValue()[1][i][2]
                #print(asig.getValue()[1][0][2].getValue())
                if(encontro==False):
                    archivo = open("Salida.txt", "a")
                    archivo.write("Error: El atributo "+ self.id2 + " no existe\n")
                    archivo.close()
                    Environment.saveError("Error: El atributo "+ self.id2 + " no existe", 'Local', self.fila, self.columna)
                    return Symbol("",0,typeExpression.INTEGER,0,0)
        else:
            archivo = open("Salida.txt", "a")
            archivo.write("Error: Los atributos solo pueden usados para structs\n")
            archivo.close()
            Environment.saveError("Error: Los atributos solo pueden usados para structs", 'Local', self.fila, self.columna)
            return Symbol("",0,typeExpression.INTEGER,0,0)