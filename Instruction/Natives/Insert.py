from Enum.typeExpression import typeExpression
from Environment.Symbol import Symbol
from Environment.Environment import Environment
from Abstract.Instruction import Instruction
from Abstract.Expression import Expression

class Insert(Instruction):
    def __init__(self,  Exp: Expression, Exp1: Expression, Exp2: Expression,fila,columna)-> None:
        self.Exp = Exp
        self.Exp1 = Exp1
        self.Exp2 = Exp2
        self.fila = fila
        self.columna = columna
    def execute(self, environment: Environment):
        List = self.Exp.execute(environment)
        position = self.Exp1.execute(environment)
        tempValue = self.Exp2.execute(environment)
        if(List.getType()==typeExpression.VECTOR ):
            if(List.isMutable):
                if(position.getType()==typeExpression.INTEGER):
                    List.getValue().insert(position.getValue(),tempValue)
                    pointer=""
                    for temp in Environment.getTemporales(): 
                        if(isinstance(temp, list)):
                            if(len(temp) == 3):
                                if(temp[0] == self.Exp.id):
                                    pointer = temp[2]
                                    break
                    pointers =self.arrayToC3D(List)
                    Environment.saveTemporal(pointer,"","",str(-100000))
                    Environment.saveTemporal("H","","",0)
                    Environment.saveExpression("stack[(int)t"+str(Environment.getContador()-2)+"] = t"+str(Environment.getContador()-1)+";")
                    #Environment.saveExpression("heap[(int)H] = "+str(len(tempArray.getValue()))+";")
                    self.arraytoHeap(pointers)
                else:
                    archivo = open("Salida.txt", "a")
                    archivo.write("Error: la posicion debe de ser Integer\n")
                    archivo.close()
                    Environment.saveError("Error: la posicion debe de ser Integer", 'Local', self.fila, self.columna)
            else:
                archivo = open("Salida.txt", "a")
                archivo.write("Error: No se puede hacer push en un vector no mutable\n")
                archivo.close()
                Environment.saveError("Error: No se puede hacer push en un vector no mutable", 'Local', self.fila, self.columna)
        else:
            archivo = open("Salida.txt", "a")
            archivo.write("Error: push es solo para vectores\n")
            archivo.close()
            Environment.saveError("Error: push es solo para vectores", 'Local', self.fila, self.columna)
    
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