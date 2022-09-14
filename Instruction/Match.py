from Enum.typeExpression import typeExpression
from Environment.Symbol import Symbol
from Environment.Environment import Environment
from Abstract.Instruction import Instruction
from Abstract.Expression import Expression

class Match(Instruction):
    def  __init__(self, Exp: Expression, options,fila,columna)-> None:
        self.Exp = Exp
        self.options = options
        self.fila = fila
        self.columna = columna
    def execute(self, environment: Environment):
        tempValue = self.Exp.execute(environment)
        for option in self.options:
            if(isinstance(option[0],list)):
                for op in option[0]:
                    tempOption = op.execute(environment)
                    if(tempOption.getType() == tempValue.getType()):
                        if(tempOption.getValue() == tempValue.getValue()):
                            if(isinstance(option[1],list)):
                                for inst in option[1]:
                                    inst.execute(environment)
                            else:
                                option[1].execute(environment)
                    else:
                        archivo = open("Salida.txt", "a")
                        archivo.write("Error: Los tipos en la lista de coicidencias no coinciden\n")
                        archivo.close()
                        Environment.saveError("Error: Los tipos en la lista de coicidencias no coinciden", 'Local', self.fila, self.columna)
                        break
                        
            else:
                tempOption = option[0].execute(environment)
                if(tempOption.getType() == tempValue.getType()):
                    if(option[0].execute(environment).getValue() == tempValue.getValue()):
                        if(isinstance(option[1],list)):
                            for inst in option[1]:
                                inst.execute(environment)
                        else:
                            option[1].execute(environment)
                else:
                        archivo = open("Salida.txt", "a")
                        archivo.write("Error: Los tipos no coinciden\n")
                        archivo.close()
                        Environment.saveError("Error: Los tipos no coinciden", 'Local', self.fila, self.columna)
                        break

