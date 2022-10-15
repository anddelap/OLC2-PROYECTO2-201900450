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
            return Primitive(0,typeExpression.INTEGER).execute(environment)
        else:
            pointer=""
            for temp in Environment.getTemporales(): 
                if(isinstance(temp, list)):
                    if(len(temp) == 3):
                        if(temp[0] == self.id):
                            pointer = temp[2]
                            break
            Environment.saveTemporal(pointer,"","",Environment.getP())
            Environment.saveTemporal("stack[(int)t"+str(Environment.getContador()-1)+"]","","",retValue.getValue())
            #Environment.saveExpression("stack[(int)t"+str(Environment.getContador()-1)+"] = "+aux[1]+";")    
            return retValue
