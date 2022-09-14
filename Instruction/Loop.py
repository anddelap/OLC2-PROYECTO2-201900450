from Expression.transSen import transSen
from Enum.transferSen import trasnferSen
from Enum.typeExpression import typeExpression
from Environment.Symbol import Symbol
from Environment.Environment import Environment
from Abstract.Instruction import Instruction
from Abstract.Expression import Expression

class Loop(Instruction):
    def __init__(self, block, fila, columna) -> None:
        self.block = block
        self.transfer = False
        self.fila = fila
        self.columna = columna

    def execute(self, environment: Environment):
        transfer = ""
        while(True):
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
            if(transfer == "break"):
                break
            elif(transfer == "continue"):
                continue   