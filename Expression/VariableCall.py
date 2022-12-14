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
            encontrado = False
            for temp in Environment.getTemporales(): 
                if(isinstance(temp, list)):
                    if(len(temp) == 3):
                        if(temp[0] == self.id):
                            pointer = temp[2]
                            encontrado = True
                            break
            if(encontrado==False):
                for temp in Environment.getTemporales():
                    if(len(temp)==4):
                        if(temp[0]=="void"):
                            for t in temp[3]:
                                if(t[0] == self.id):
                                    pointer = t[2]
                                
                
            #print(self.id)
            Environment.saveTemporal(pointer,"","",str(-100000))
            if(retValue.getType() == typeExpression.INTEGER or retValue.getType() == typeExpression.FLOAT):
                Environment.saveTemporal("stack[(int)t"+str(Environment.getContador()-1)+"]","","",retValue.getValue())
            elif(retValue.getType() == typeExpression.BOOL):
                if(retValue.getValue() == True):
                    Environment.saveTemporal("stack[(int)t"+str(Environment.getContador()-1)+"]","","",1)
                else:
                    Environment.saveTemporal("stack[(int)t"+str(Environment.getContador()-1)+"]","","",0)
            elif(retValue.getType() == typeExpression.STRING or retValue.getType() == typeExpression.PSTRING) :
                Environment.saveTemporal("stack[(int)t"+str(Environment.getContador()-1)+"]","","",len(retValue.getValue()))
            elif(retValue.getType() == typeExpression.ARRAY or retValue.getType() == typeExpression.VECTOR):
                Environment.saveTemporal("stack[(int)t"+str(Environment.getContador()-1)+"]","","",len(retValue.getValue()))
            #Environment.saveExpression("stack[(int)t"+str(Environment.getContador()-1)+"] = "+aux[1]+";")    
            return retValue
