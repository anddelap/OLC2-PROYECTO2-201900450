from Enum.typeExpression import typeExpression
from Environment.Symbol import Symbol
from Abstract.Instruction import Instruction
from Abstract.Expression import Expression
from Environment.Environment import Environment
Salida =[]
class Println(Instruction):
    def __init__(self, expression: Expression, fila, columna)-> None:
        self.expression = expression
        self.transfer = False
        self.fila = fila
        self.columna = columna
    def execute(self, environment: Environment):
        if(isinstance(self.expression,list)):
            salida=[]
            formato = self.expression[0].execute(environment)
            cantllaves = self.getCantLLaves(formato.getValue())
            cantExps = len(self.expression)-1
            if cantllaves == cantExps:
                i = 0
                exps = []
                for expression in range(1,len(self.expression)):
                    tempExp = self.expression[expression].execute(environment)
                    for j in range(i,len(formato.getValue())):
                        if(j != len(formato.getValue())):
                            if formato.getValue()[j] == "{" and formato.getValue()[j+1] == "}":
                                if tempExp.isArray():
                                    archivo = open("Salida.txt", "a")
                                    archivo.write("Error: {} no puede ser utilizado con arreglos o vectores\n")
                                    archivo.close()
                                    Environment.saveError("Error: {} no puede ser utilizado con arreglos o vectores", 'Local', self.fila, self.columna)
                                    salida.append("Error")
                                    i += 4
                                    break
                                else:
                                    exps.append([tempExp.getValue(),tempExp.getType()])
                                    salida.append(str(tempExp.getValue()))
                                    i += 2
                                    break
                            elif formato.getValue()[j] == "{" and formato.getValue()[j+1] == ":" and formato.getValue()[j+2] == "?" and formato.getValue()[j+3] == "}":
                                if tempExp.isArray():
                                    valor = self.printarray(tempExp)
                                    salida.append(str(valor))
                                    i += 4
                                    break
                                else:
                                    archivo = open("Salida.txt", "a")
                                    archivo.write("Error: {:?} solo puede ser utilizado con arreglos o vectores\n")
                                    archivo.close()
                                    Environment.saveError("Error: {:?} solo puede ser utilizado con arreglos o vectores", 'Local', self.fila, self.columna)
                                    salida.append("Error")
                                    i += 4
                                    break
                            else:
                                salida.append(formato.getValue()[j])
                                i += 1
                        else:
                            salida.append(formato.getValue()[j])
                            i += 1
                for e in exps:
                    find = False
                    for temp in Environment.getTemporales():
                        if len(temp) == 5:
                            if str(e[0]) == temp[4]:
                                if(e[1]==typeExpression.INTEGER):
                                    Environment.saveExpression("printf(\"%d\",(int)"+temp[0]+");")
                                    find = True
                                elif(e[1]==typeExpression.FLOAT):
                                    Environment.saveExpression("printf(\"%f\","+temp[0]+");")
                                    find = True
                    if(find == False):
                        if(e[1]==typeExpression.INTEGER):
                            Environment.saveExpression("printf(\"%d\",(int)"+str(e[0])+");")
                        elif(e[1]==typeExpression.FLOAT):
                            Environment.saveExpression("printf(\"%f\","+str(e[0])+");")
                                   
                if(i != len(formato.getValue())):
                    for j in range(i,len(formato.getValue())):
                        salida.append(formato.getValue()[j])
                #exit=""
                #archivo = open("Salida.txt", "a")
                #archivo.write(exit.join(salida)+"\n")
                #archivo.close()
                """ for expression in range(1,len(self.expression)):
                    tempExp = self.expression[expression].execute(environment)
                    print(tempExp.getValue()) """
            else:
                archivo = open("Salida.txt", "a")
                archivo.write("Error: la cantidad de {} y de {:?} en el formato y de expresiones debe ser igual\n")
                archivo.close()
                Environment.saveError("Error: la cantidad de {} y de {:?} en el formato y de expresiones debe ser igual", 'Local', self.fila, self.columna)

        else:
            tempExp = self.expression.execute(environment)
            if(tempExp.getType() == typeExpression.PSTRING):
                archivo = open("Salida.txt", "a")
                archivo.write(str(tempExp.getValue())+"\n")
                archivo.close()
            elif(tempExp.getType() == typeExpression.STRING):
                archivo = open("Salida.txt", "a")
                archivo.write(str(tempExp.getValue())+"\n")
                archivo.close()   
            else:
                archivo = open("Salida.txt", "a")
                archivo.write("Error: Esta impresion es solo para strings\n")
                archivo.close()
                Environment.saveError("Error: Esta impresion es solo para strings", 'Local', self.fila, self.columna)
    def printarray(self, expression:Symbol):
        valor = "["
        if(len(expression.getValue())==0):
            valor+="]"
        else:
            for i in range(0,len(expression.getValue())):
                if i < len(expression.getValue())-1:
                    if expression.getValue()[i].isArray():
                        valor += self.printarray(expression.getValue()[i])+","
                    else:
                        valor+=str(expression.getValue()[i].value)+","
                if  i == len(expression.getValue())-1:
                    if expression.getValue()[i].isArray():
                        a = self.printarray(expression.getValue()[i])
                        valor +=  a+"]"
                    else:
                        valor+=str(expression.getValue()[i].value)+"]"
        return valor
    
    def getCantLLaves(self, expression):
        cant = 0
        for i in range(0,len(expression)):
            if i != len(expression)-1:
                if (expression[i] == "{" and expression[i+1] == "}") or (expression[i] == "{" and expression[i+1] == ":" and expression[i+2] == "?" and expression[i+3] == "}"):
                    cant += 1
        return cant
        
