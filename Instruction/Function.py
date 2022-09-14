from Enum.transferSen import trasnferSen
from Environment.Symbol import Symbol
from Instruction.Main import Main
from Instruction.Parameter import Parameter
from Abstract.Instruction import Instruction
from Environment.Environment import Environment
from Enum.typeExpression import typeExpression

class Function(Instruction):
    
    def __init__(self, id: str, parameters ,block, typee, fila, columna) -> None:
        self.id = id
        self.parameters = parameters
        self.block = block
        self.typee = typee
        self.transfer = False
        self.fila=fila
        self.columna = columna

    def execute(self, environment: Environment):
        if(self.id == "main"):
            Main(self.block)
        else:
            environment.saveFunction(self.id,self,self.fila,self.columna)

    def executeFunction(self, environment: Environment):
        newEnv = Environment(environment)
        for parameter in self.parameters:
            parameter.execute(newEnv)
        
        for ins in self.block:
            tran = ins.execute(newEnv)
            tipo = str(type(ins))
            if tipo == "<class 'Expression.transSen.transSen'>":
                if(ins.type==trasnferSen.BREAK):
                        return "break"
                elif(ins.type==trasnferSen.CONTINUE):
                        return "continue"
                elif(ins.type==trasnferSen.RETURN):
                    #return  ins.value.execute(newEnv)
                    if(self.typee != None):
                        if(ins.value.execute(newEnv).getType()==self.typee):
                            return ins.value.execute(newEnv)
                        else:
                            archivo = open("Salida.txt", "a")
                            archivo.write("Error: Tipo de valor que se retorna no coinciden con el tipo de la funcion\n")
                            archivo.close()
                            #archivo = open("Errores/Errores.txt", "a")
                            #archivo.write("Error: la funcion "+ str(self.id) + " no retorna un valor de tipo "+ str(self.typee)+"\n")
                            #archivo.close()
                            Environment.saveError("Error: Tipo de valor que se retorna no coinciden con el tipo de la funcion",'Local', self.fila, self.columna)
                            if(self.typee==typeExpression.INTEGER):
                                return Symbol("", 0, self.typee,0,0)
                            elif(self.typee==typeExpression.STRING):
                                return Symbol("", "", self.typee,0,0)
                            elif(self.typee==typeExpression.BOOL):
                                return Symbol("", False, self.typee,0,0)
                            elif(self.typee==typeExpression.FLOAT):
                                return Symbol("", 0.0, self.typee,0,0)
                            elif(self.typee==typeExpression.CHAR):
                                return Symbol("", '', self.typee,0,0)
                            elif(self.typee==typeExpression.PSTRING):
                                return Symbol("", "", self.typee,0,0)
                            elif(self.typee==typeExpression.ARRAY):
                                error = []
                                return Symbol("", error, self.typee,0,0)
                            elif(self.typee==typeExpression.VECTOR):
                                error = []
                                return Symbol("", error, self.typee,0,0)

                    else:
                        archivo = open("Salida.txt", "a")
                        archivo.write("Error: La funcion no puede retornar\n")
                        archivo.close()
                        #archivo = open("Errores/Errores.txt", "a")
                        #archivo.write("Error: la funcion "+ str(self.id) + " no retorna un valor de tipo "+ str(self.typee)+"\n")
                        #archivo.close()
                        Environment.saveError("Error: La funcion no puede retornar",'Local', self.fila, self.columna)
            if(tran != None):
                if(tran == "break"):
                    return "break"
                elif(tran == "continue"):
                    return "continue" 
                else:
                    try:
                        if(self.typee != None):
                            if(tran.execute(newEnv).getType()==self.typee):
                                return tran.execute(newEnv)
                            else:
                                archivo = open("Salida.txt", "a")
                                archivo.write("Error: Tipo de valor que se retorna no coinciden con el tipo de la funcion\n")
                                archivo.close()
                                #archivo = open("Errores/Errores.txt", "a")
                                #archivo.write("Error: la funcion "+ str(self.id) + " no retorna un valor de tipo "+ str(self.typee)+"\n")
                                #archivo.close()
                                Environment.saveError("Error: Tipo de valor que se retorna no coinciden con el tipo de la funcion",'Local', self.fila, self.columna)
                                if(self.typee==typeExpression.INTEGER):
                                    return Symbol("", 0, self.typee,0,0)
                                elif(self.typee==typeExpression.STRING):
                                    return Symbol("", "", self.typee,0,0)
                                elif(self.typee==typeExpression.BOOL):
                                    return Symbol("", False, self.typee,0,0)
                                elif(self.typee==typeExpression.FLOAT):
                                    return Symbol("", 0.0, self.typee,0,0)
                                elif(self.typee==typeExpression.CHAR):
                                    return Symbol("", '', self.typee,0,0)
                                elif(self.typee==typeExpression.PSTRING):
                                    return Symbol("", "", self.typee,0,0)
                                elif(self.typee==typeExpression.ARRAY):
                                    return Symbol("", [], self.typee,0,0)
                                elif(self.typee==typeExpression.VECTOR):
                                    return Symbol("", [], self.typee,0,0)
                        else:
                            archivo = open("Salida.txt", "a")
                            archivo.write("Error: La funcion no puede retornar\n")
                            archivo.close()
                            #archivo = open("Errores/Errores.txt", "a")
                            #archivo.write("Error: la funcion "+ str(self.id) + " no retorna un valor de tipo "+ str(self.typee)+"\n")
                            #archivo.close()
                            Environment.saveError("Error: La funcion no puede retornar",'Local', self.fila, self.columna)
                    except:
                        if(self.typee != None):
                            if(tran.type==self.typee):
                                return tran
                            else:
                                archivo = open("Salida.txt", "a")
                                archivo.write("Error: Tipo de valor que se retorna no coinciden con el tipo de la funcion\n")
                                archivo.close()
                                #archivo = open("Errores/Errores.txt", "a")
                                #archivo.write("Error: la funcion "+ str(self.id) + " no retorna un valor de tipo "+ str(self.typee)+"\n")
                                #archivo.close()
                                Environment.saveError("Error: Tipo de valor que se retorna no coinciden con el tipo de la funcion",'Local', self.fila, self.columna)
                                if(self.typee==typeExpression.INTEGER):
                                    return Symbol("", 0, self.typee,0,0)
                                elif(self.typee==typeExpression.STRING):
                                    return Symbol("", "", self.typee,0,0)
                                elif(self.typee==typeExpression.BOOL):
                                    return Symbol("", False, self.typee,0,0)
                                elif(self.typee==typeExpression.FLOAT):
                                    return Symbol("", 0.0, self.typee,0,0)
                                elif(self.typee==typeExpression.CHAR):
                                    return Symbol("", '', self.typee,0,0)
                                elif(self.typee==typeExpression.PSTRING):
                                    return Symbol("", "", self.typee,0,0)
                                elif(self.typee==typeExpression.ARRAY):
                                    return Symbol("", [], self.typee,0,0)
                                elif(self.typee==typeExpression.VECTOR):
                                    return Symbol("", [], self.typee,0,0)
                        else:
                            archivo = open("Salida.txt", "a")
                            archivo.write("Error: La funcion no puede retornar\n")
                            archivo.close()
                            #archivo = open("Errores/Errores.txt", "a")
                            #archivo.write("Error: la funcion "+ str(self.id) + " no retorna un valor de tipo "+ str(self.typee)+"\n")
                            #archivo.close()
                            Environment.saveError("Error: La funcion no puede retornar",'Local', self.fila, self.columna)   