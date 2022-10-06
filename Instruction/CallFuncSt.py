from Expression.VariableCall import VariableCall
from Enum.transferSen import trasnferSen
from Environment.Symbol import Symbol
from Instruction.Parameter import Parameter
from Instruction.Function import Function
from Expression.Primitive import Primitive
from Abstract.Instruction import Instruction
from Environment.Environment import Environment
from Abstract.Expression import Expression
from Enum.typeExpression import typeExpression

class CallFuncSt(Instruction):

    def __init__(self,id,parameters, fila, columna) -> None:
        self.id = id
        self.parameters = parameters
        self.transfer = False
        self.fila = fila
        self.columna = columna
    def execute(self, environment: Environment):
        tempFunc: Function = environment.getFunction(self.id, self.fila, self.columna)
        newEnvironment = Environment(environment.getGlobal())
        if(tempFunc != None):
            if self.parameters ==None and tempFunc.parameters==[]:
                Environment.saveExpression(self.id+"();")
                #tran = tempFunc.executeFunction(environment)
                #if tran!=None:
                #    if(tran=="break"):
                #        return "break"
                #    elif(tran=="continue"):
                #        return "continue"
                #    else:
                #        return tran
            else:
                if(len(tempFunc.parameters)==len(self.parameters)):
                    for x in range(0,len(tempFunc.parameters)):
                        tempPar: Parameter = tempFunc.parameters[x]
                        
                        tempPar.setValue(self.parameters[x])
                    tran = tempFunc.executeFunction(environment)
                    if tran!=None:
                        if(tran=="break"):
                            return "break"
                        elif(tran=="continue"):
                            return "continue"
                        else:
                            return tran
                            #return Symbol("", tran.value, tran.type,0,0)   
                else:
                    archivo = open("Salida.txt", "a")
                    archivo.write("Error: la funcion "+ str(self.id) + " requiere "+ str(len(tempFunc.parameters))+" parametros\n")
                    archivo.close()
                    #archivo = open("Errores/Errores.txt", "a")
                    #archivo.write("Error: la funcion "+ str(self.id) + " requiere "+ str(len(tempFunc.parameters))+" parametros\n")
                    #archivo.close()
                    Environment.saveError("Error: La función " + id + " no existe", 'Local', self.fila, self.columna)
