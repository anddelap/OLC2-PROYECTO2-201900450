from Enum.transferSen import trasnferSen
from turtle import left
from Enum.typeExpression import typeExpression
from Environment.Symbol import Symbol
from Environment.Environment import Environment
from Abstract.Instruction import Instruction
from Abstract.Expression import Expression

class For(Instruction):
    def __init__(self, id1 , id2 ,leftExp: Expression, rightExp: Expression, block, fila, columna) -> None:
        self.id1 = id1
        self.id2 = id2
        self.block = block
        self.leftExp = leftExp
        self.rightExp = rightExp
        self.fila = fila
        self.columna = columna
        self.transfer = False
    def execute(self, environment: Environment):
        leftValue = self.leftExp.execute(environment)
        if (self.id2==None):
            if(self.rightExp!=None):
                rightValue = self.rightExp.execute(environment)
                if(leftValue.getType()==typeExpression.INTEGER and rightValue.getType()==typeExpression.INTEGER):
                    tempSy = Symbol("",0,leftValue.type,0,0)
                    #========== For de intervalo ==========               
                    for i in range(leftValue.getValue(),rightValue.getValue()):
                        newEnv = Environment(environment)
                        newEnv.saveVariable(self.id1, tempSy, typeExpression.INTEGER,0,0,False,True, True)  
                        transfer=""
                        tempVar = newEnv.getVariable(self.id1)
                        tempVar.value = i
                        for ins in self.block:
                            #ins.execute(newEnv)
                            tran = ins.execute(newEnv)
                            tipo = str(type(ins))
                            if tipo == "<class 'Instruction.transSen.transSen'>":
                                if(ins.type==trasnferSen.BREAK):
                                        transfer = "break"
                                elif(ins.type==trasnferSen.CONTINUE):
                                        transfer = "continue"
                                elif(ins.type==trasnferSen.RETURN):
                                        return  ins.value.execute(newEnv)
                            elif(tran != None):
                                if(tran == "break"):
                                    transfer =  "break"
                                elif(tran == "continue"):
                                    transfer = "continue"
                                else:
                                    try:
                                        return tran.execute(newEnv)
                                    except:
                                        return tran                     
                        if(transfer == "break"):
                            break
                        elif(transfer == "continue"):
                            continue      
                else:
                    ruta = "Salida.txt"
                    archivo = open(ruta, "a")
                    archivo.write("Error: El rango debe ser dado por valores Integer\n")
                    archivo.close()
                    #archivo = open("Errores/Errores.txt", "a")
                    #archivo.write("Error: El rango debe ser dado por valores Integer\n")
                    #archivo.close()
                    Environment.saveError("Error: El rango debe ser dado por valores Integer", 'Local', self.fila, self.columna)
            else:
                if(leftValue.getType()==typeExpression.ARRAY or leftValue.getType()==typeExpression.VECTOR):
                    #tempSy = Symbol("",None,leftValue.getType(),0,0)      
                    for i in leftValue.getValue():
                        newEnv = Environment(environment)
                        newEnv.saveVariable(self.id1, Symbol("",None,i.getType(),0,0) , i.getType(),0,0,False,True, True)
                        transfer=""
                        tempVar = newEnv.getVariable(self.id1)
                        if(i.getType()==typeExpression.ARRAY or i.getType()==typeExpression.VECTOR) :
                            tempVar.array = True
                        tempVar.value = i.getValue()
                        for ins in self.block:
                            tran = ins.execute(newEnv)
                            tipo = str(type(ins))
                            if tipo == "<class 'Instruction.transSen.transSen'>":
                                if(ins.type==trasnferSen.BREAK):
                                        transfer = "break"
                                elif(ins.type==trasnferSen.CONTINUE):
                                        transfer = "continue"
                                elif(ins.type==trasnferSen.RETURN):
                                        return  ins.value.execute(newEnv)
                            elif(tran != None):
                                if(tran == "break"):
                                    transfer =  "break"
                                elif(tran == "continue"):
                                    transfer = "continue"
                                else:
                                    try:
                                        return tran.execute(newEnv)
                                    except:
                                        return tran                     
                        if(transfer == "break"):
                            break
                        elif(transfer == "continue"):
                            continue      
                else:
                    ruta = "Salida.txt"
                    archivo = open(ruta, "a")
                    archivo.write("Error: La exprecion debe de ser Array o Vector\n")
                    archivo.close()
                    #archivo = open("Errores/Errores.txt", "a")
                    #archivo.write("Error: El rango debe ser dado por valores Array o Vector\n")
                    #archivo.close()
                    Environment.saveError("Error: La exprecion debe de ser Array o Vector", 'Local', self.fila, self.columna)
        