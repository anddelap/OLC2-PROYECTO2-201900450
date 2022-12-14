from Expression.transSen import transSen
from Enum.transferSen import trasnferSen
from Enum.typeExpression import typeExpression
from Environment.Symbol import Symbol
from Environment.Environment import Environment
from Abstract.Instruction import Instruction
from Abstract.Expression import Expression

class While(Instruction):

    def __init__(self, condition: Expression, block, fila, columna) -> None:
        self.condition = condition
        self.block = block
        self.transfer = False
        self.fila = fila
        self.columna = columna

    def execute(self, environment: Environment):
        transfer = ""
        position = len(Environment.getTemporales())-1
        tempCondition: Symbol = self.condition.execute(environment)
        if tempCondition.type == typeExpression.BOOL:
            Environment.saveExpression("L"+str(Environment.getEtiqueta())+":")
            Environment.aumentarContadorL()
            newEnv = Environment(environment)
            positionBreak = 0
            positionContinue = 0
            for ins in self.block:
                tran = ins.execute(newEnv)
                tipo = str(type(ins))
                if tipo == "<class 'Expression.transSen.transSen'>":
                    if(ins.type==trasnferSen.BREAK):
                            positionBreak =  len(Environment.getTemporales())
                            transfer = "break"
                    elif(ins.type==trasnferSen.CONTINUE):
                            positionContinue =  len(Environment.getTemporales())
                            transfer = "continue"
                    elif(ins.type==trasnferSen.RETURN):
                            """  return  ins.value.execute(newEnv) """
                            value = ins.value.execute(newEnv)
                            aux = ""
                            for temp in Environment.getTemporales():
                                if(len(temp) == 5):
                                    if str(value.getValue()) == str(temp[4]):
                                        aux = temp[0]
                                        asignacion = True
                            Environment.saveExpression("stack[P] = "+aux+";")
                """ if(tran != None):
                    if(tran == "break"):
                        transfer =  "break"
                    elif(tran == "continue"):
                        transfer = "continue"
                    else:
                        try:
                            return tran.execute(newEnv)
                        except:
                            return tran  """
            Environment.saveExpression("L"+str(Environment.getEtiqueta())+":")
            position2 = len(Environment.getTemporales())
            if(positionBreak != 0):
                Environment.getTemporales().insert(positionBreak,"goto L"+str(Environment.getEtiqueta())+";")
            Environment.aumentarContadorL()
            """ position2 = len(Environment.getTemporales()) """
            Environment.getTemporales().insert(position,"L"+str(Environment.getEtiqueta())+":")
            Environment.getTemporales().insert(position2,"goto L"+str(Environment.getEtiqueta())+";")

            if(positionContinue != 0):
                """ print(Environment.getTemporales()[positionContinue])
                print(Environment.getTemporales()) """
                Environment.getTemporales().insert(positionContinue,"goto L"+str(Environment.getEtiqueta())+";")

            #print(Environment.getEtiqueta())
            """ while(tempCondition.getValue() == True):
                newEnv = Environment(environment)
                for ins in self.block:
                    tran = ins.execute(newEnv)
                    tipo = str(type(ins))
                    if tipo == "<class 'Expression.transSen.transSen'>":
                        if(ins.type==trasnferSen.BREAK):
                                transfer = "break"
                        elif(ins.type==trasnferSen.CONTINUE):
                                transfer = "continue"
                        elif(ins.type==trasnferSen.RETURN):
                                return  ins.value.execute(newEnv)
                    if(tran != None):
                        if(tran == "break"):
                            transfer =  "break"
                        elif(tran == "continue"):
                            transfer = "continue"
                        else:
                            try:
                                return tran.execute(newEnv)
                            except:
                                return tran          
                tempCondition = self.condition.execute(environment)
                if(transfer == "break"):
                    break
                elif(transfer == "continue"):
                    continue      """
                #tempCondition = self.condition.execute(environment) 
        else:
            ruta = "Salida.txt"
            archivo = open(ruta, "a")
            archivo.write("Error: La condicion del while debe de ser booleana. \n")
            archivo.close()
            #archivo = open("Errores/Errores.txt", "a")
            #archivo.write("Error: Condicion no valida.  \n")
            #archivo.close()
            Environment.saveError("Error: La condicion del while debe de ser booleana.", 'Local', self.fila, self.columna)