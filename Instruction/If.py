from Enum.transferSen import trasnferSen
from Enum.typeExpression import typeExpression
from Environment.Symbol import Symbol
from Environment.Environment import Environment
from Abstract.Instruction import Instruction
from Abstract.Expression import Expression

class If(Instruction):

    def __init__(self, condition: Expression, block, elseBlock, fila, columna) -> None:
        self.condition = condition
        self.block = block
        self.elseBlock = elseBlock
        self.fila = fila
        self.columna = columna
        self.transfer = False

    def execute(self, environment: Environment):
        tempCondition: Symbol = self.condition.execute(environment)
        if tempCondition.type == typeExpression.BOOL:
            if(tempCondition.getValue() == True):
                newEnv = Environment(environment)
                for ins in self.block:
                    #ins.execute(newEnv)
                    tran = ins.execute(newEnv)
                    tipo = str(type(ins))
                    if tipo == "<class 'Expression.transSen.transSen'>":
                        if(ins.type==trasnferSen.BREAK):
                            return "break"
                        elif(ins.type==trasnferSen.CONTINUE):
                            return "continue"
                        elif(ins.type==trasnferSen.RETURN):
                            return  ins.value
                    if(tran != None):
                        if(tran == "break"):
                            return "break"
                        elif(tran == "continue"):
                            return "continue"  
                        else:
                            try:
                                return tran.execute(newEnv)
                            except:
                                return tran       
                tempCondition = self.condition.execute(environment)
            else:
                if(self.elseBlock!=None):
                    newEnv = Environment(environment)
                    ins = str(type(self.elseBlock))
                    if ins == "<class 'Instruction.If.If'>":
                        tran = self.elseBlock.execute(environment)
                        tipo = str(type(ins))
                        if tipo == "<class 'Expression.transSen.transSen'>":
                            if(ins.type==trasnferSen.BREAK):
                                return "break"
                            elif(ins.type==trasnferSen.CONTINUE):
                                return "continue"
                            elif(ins.type==trasnferSen.RETURN):
                                return  ins.value.execute(newEnv)
                        elif(tran != None):
                            if(tran == "break"):
                                return "break"
                            elif(tran == "continue"):
                                return "continue"  
                            else:
                                try:
                                    return tran.execute(newEnv)
                                except:
                                    return tran 
                    else:
                        for ins in self.elseBlock:
                            #ins.execute(newEnv)
                            tran = ins.execute(newEnv)
                            tipo = str(type(ins))
                            if tipo == "<class 'Expression.transSen.transSen'>":
                                if(ins.type==trasnferSen.BREAK):
                                    return "break"
                                elif(ins.type==trasnferSen.CONTINUE):
                                    return "continue"
                                elif(ins.type==trasnferSen.RETURN):
                                    return  ins.value.execute(newEnv)
                            elif(tran != None):
                                if(tran == "break"):
                                    return "break"
                                elif(tran == "continue"):
                                    return "continue"  
                                else:
                                    try:
                                        return tran.execute(newEnv)
                                    except:
                                        return tran           
        else:
            ruta = "Salida.txt"
            archivo = open(ruta, "a")
            archivo.write("Error: Condicion no valida.  \n")
            archivo.close()
            #archivo = open("Errores/Errores.txt", "a")
            #archivo.write("Error: Condicion no valida.  \n")
            #archivo.close()
            Environment.saveError("Error: Condicion no valida.",'Local', self.fila, self.columna)