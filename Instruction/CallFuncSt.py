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
        newEnvironment = Environment(environment)
        if(tempFunc != None):
            if self.parameters ==None and tempFunc.parameters==[]:
                pointer =0
                for temp in Environment.getTemporales():
                    if(len(temp)==4):
                        if(temp[0]=="void"):
                            if(temp[1]==self.id):
                                pointer = temp[2]
                                break
                Environment.saveTemporal("P + "+str(pointer), "", "", str(-100000))               
                Environment.saveExpression(self.id+"();")
                Environment.saveTemporal("P - "+str(pointer), "", "", str(-100000))  
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
                    pointer = 0
                    parameters = []
                    for temp in Environment.getTemporales():
                        if(len(temp)==4):
                            if(temp[0]=="void"):
                                if(temp[1]==self.id):
                                    pointer = temp[2]
                                    parameters= temp[3]
                                    break
                    arrayParameter = []
                    for i in range(0,len(self.parameters)):
                        pam = self.parameters[i].execute(newEnvironment)
                        arrayParameter.append(pam)
                        parameters[i][1] = pam.getValue()
                    Environment.saveTemporal("P + "+str(pointer), "", "", str(-100000))  
                    #print(arrayParameter)
                    for i in range(0,len(parameters)):
                        print(parameters[i][1])
                        print(arrayParameter[i].getType())
                        aux = parameters[i][1]
                        for temp in Environment.getTemporales():
                            if(len(temp) == 5):
                                if str(parameters[i][1]) == str(temp[4]):
                                    aux = temp[0]
                        Environment.saveTemporal(parameters[i][2], "", "", str(-100000)) 
                        if(arrayParameter[i].getType() == typeExpression.INTEGER or arrayParameter[i].getType() == typeExpression.FLOAT):
                            Environment.saveExpression("stack[(int)t"+str(Environment.getContador()-1)+"] = "+str(aux)+";")
                        elif (arrayParameter[i].getType()==typeExpression.STRING or arrayParameter[i].getType()==typeExpression.PSTRING):
                            Environment.saveTemporal("H","","",str(-100000))
                            Environment.saveExpression("stack[(int)t"+str(Environment.getContador()-2)+"] = t"+str(Environment.getContador()-1)+";")
                            Environment.saveExpression("heap[(int)H] = "+str(len(aux))+";")
                            for v in aux:
                                Environment.saveExpression("H = H + 1;")
                                Environment.aumentarH()
                                Environment.saveExpression("heap[(int)H] = "+str(ord(v))+";")
                            Environment.saveExpression("H = H + 1;")
                            Environment.aumentarH()
                        elif(arrayParameter[i].getType()==typeExpression.BOOL):
                            if(aux == True):
                                Environment.saveExpression("stack[(int)t"+str(Environment.getContador()-1)+"] = 1;")
                            else:
                                Environment.saveExpression("stack[(int)t"+str(Environment.getContador()-1)+"] = 0;") 
                        elif(arrayParameter[i].getType() == typeExpression.VECTOR or arrayParameter[i].getType() == typeExpression.ARRAY):
                            pointers =self.arrayToC3D(arrayParameter[i])
                            #Environment.saveTemporal("P + "+str(Environment.getP()),"","",str(-100000))
                            Environment.saveTemporal("H","","",0)
                            Environment.saveExpression("stack[(int)t"+str(Environment.getContador()-2)+"] = t"+str(Environment.getContador()-1)+";")
                            #Environment.saveExpression("heap[(int)H] = "+str(len(tempArray.getValue()))+";")
                            self.arraytoHeap(pointers)
                    Environment.saveExpression(self.id+"();")
                    Environment.saveTemporal("P - "+str(pointer), "", "", str(-100000))  
                    
                    #for x in range(0,len(tempFunc.parameters)):
                    #    tempPar: Parameter = tempFunc.parameters[x]
                        
                    #    tempPar.setValue(self.parameters[x])
                    #tran = tempFunc.executeFunction(environment)
                    #if tran!=None:
                    #    if(tran=="break"):
                    #        return "break"
                    #    elif(tran=="continue"):
                    #        return "continue"
                    #    else:
                    #        return tran
                            #return Symbol("", tran.value, tran.type,0,0)   
                else:
                    archivo = open("Salida.txt", "a")
                    archivo.write("Error: la funcion "+ str(self.id) + " requiere "+ str(len(tempFunc.parameters))+" parametros\n")
                    archivo.close()
                    #archivo = open("Errores/Errores.txt", "a")
                    #archivo.write("Error: la funcion "+ str(self.id) + " requiere "+ str(len(tempFunc.parameters))+" parametros\n")
                    #archivo.close()
                    Environment.saveError("Error: la funcion "+ str(self.id) + " requiere "+ str(len(tempFunc.parameters))+" parametros", 'Local', self.fila, self.columna)

    def arrayToC3D(self, expression:Symbol):
        valor = []
        valor.append(len(expression.getValue()))
        #Environment.aumentarH()
        for i in range(0,len(expression.getValue())):
            if expression.getValue()[i].isArray():
                    #print(i)
                    if(i==0):
                        valor.append(Environment.getH()+(len(expression.getValue())+1))
                        for j in range(0,len(expression.getValue())):
                            Environment.aumentarH()
                        Environment.aumentarH()
                    else:
                        for j in range(0,len(expression.getValue()[i].getValue())):
                            Environment.aumentarH()
                        Environment.aumentarH()
                        valor.append(Environment.getH())
            else:
                valor.append(expression.getValue()[i].value)
        for i in range(0,len(expression.getValue())):
            if expression.getValue()[i].isArray():
                    valor.append(self.arrayToC3D(expression.getValue()[i]))
        return valor
    
    def arraytoHeap(self, expression):
        contador = 0
        for exp in expression:
            if isinstance(exp, list):
                self.arraytoHeap(exp)
            else:
                Environment.saveExpression("heap[(int)H] = "+str(exp)+";")
                Environment.saveExpression("H = H + 1;")
                Environment.aumentarH()

            contador +=1
