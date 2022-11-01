from turtle import st
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
                # Falta imprmir el primer string
                for char in formato.getValue():
                    Environment.saveExpression("printf(\"%c\","+str(ord(char))+");")
                for expression in range(1,len(self.expression)):
                    tempExp = self.expression[expression].execute(environment)
                    find = False
                    aux = str(tempExp.getValue())
                    for temp in Environment.getTemporales():
                        if len(temp) == 5:
                            if (str(tempExp.getValue()) == str(temp[4])):
                                aux=str(temp[0])
                                find = True
                    if(find == False):
                        if(tempExp.getType()==typeExpression.INTEGER):
                            Environment.saveExpression("printf(\"%d\",(int)"+str(tempExp.getValue())+");")
                        elif(tempExp.getType()==typeExpression.FLOAT):
                            Environment.saveExpression("printf(\"%f\","+str(tempExp.getValue())+");")
                        elif(tempExp.getType()==typeExpression.CHAR):
                            Environment.saveExpression("printf(\"%c\","+str(ord(tempExp.getValue()))+");")
                        elif(tempExp.getType()==typeExpression.BOOL):
                            if(tempExp.getValue() == True):
                                Environment.saveExpression("printf(\"%d\",(int)"+str(0)+");")
                            else:
                                Environment.saveExpression("printf(\"%d\",(int)"+str(1)+");")
                        elif(tempExp.getType() == typeExpression.PSTRING or tempExp.getType() == typeExpression.STRING):
                            for e in tempExp.getValue():
                                Environment.saveExpression("printf(\"%c\","+str(ord(e))+");")
                            #archivo = open("Salida.txt", "a")
                            #archivo.write(str(tempExp.getValue())+"\n")
                            #archivo.close() 
                    else:  
                        if(tempExp.getType()==typeExpression.INTEGER):
                            Environment.saveExpression("printf(\"%d\",(int)"+aux+");")
                            find = True
                        elif(tempExp.getType()==typeExpression.FLOAT):
                            Environment.saveExpression("printf(\"%f\","+aux+");")
                            find = True
                        elif(tempExp.getType()==typeExpression.CHAR):
                            Environment.saveExpression("printf(\"%c\","+aux+");")
                            find = True
                        elif(tempExp.getType()==typeExpression.BOOL):
                            if(tempExp.getValue() == True):
                                Environment.saveExpression("printf(\"%d\",(int)"+aux+");")
                                find = True
                            else:
                                Environment.saveExpression("printf(\"%d\",(int)"+aux+");")
                                find = True
                        elif(tempExp.getType() == typeExpression.PSTRING or tempExp.getType() == typeExpression.STRING):
                            for e in tempExp.getValue():
                                Environment.saveExpression("printf(\"%c\","+str(ord(e))+");")
                            #archivo = open("Salida.txt", "a")
                            #archivo.write(str(tempExp.getValue())+"\n")
                            #archivo.close() 
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
                                    #valor = self.printarray(tempExp)
                                    self.printarray2(tempExp)
                                    #salida.append(str(valor))
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
                """ for e in exps:
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
                            Environment.saveExpression("printf(\"%f\","+str(e[0])+");") """
                                   
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
            if(tempExp.getType() == typeExpression.PSTRING or tempExp.getType() == typeExpression.STRING):
                for e in tempExp.getValue():
                    Environment.saveExpression("printf(\"%c\","+str(ord(e))+");")
                #archivo = open("Salida.txt", "a")
                #archivo.write(str(tempExp.getValue())+"\n")
                #archivo.close()   
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
    
    def printarray2(self, expression:Symbol):
        for i in range(0,len(expression.getValue())):
            if expression.getValue()[i].isArray():
                self.printarray2(expression.getValue()[i])
            else:
                if(expression.getValue()[i].getType()==typeExpression.INTEGER):
                    Environment.saveExpression("printf(\"%d\",(int)"+str(expression.getValue()[i].getValue())+");")
                elif(expression.getValue()[i].getType()==typeExpression.FLOAT):
                    Environment.saveExpression("printf(\"%f\","+str(expression.getValue()[i].getValue())+");")
                elif(expression.getValue()[i].getType()==typeExpression.CHAR):
                    Environment.saveExpression("printf(\"%c\","+str(ord(expression.getValue()[i].getValue()))+");")
                elif(expression.getValue()[i].getType()==typeExpression.BOOL):
                    if(expression.getValue()[i].getValue() == True):
                        Environment.saveExpression("printf(\"%d\",(int)"+str(0)+");")
                    else:
                        Environment.saveExpression("printf(\"%d\",(int)"+str(1)+");")
                elif(expression.getValue()[i].getType() == typeExpression.PSTRING or expression.getValue()[i].getType() == typeExpression.STRING):
                    for e in expression.getValue()[i].getValue():
                        Environment.saveExpression("printf(\"%c\","+str(ord(e))+");")
    
    def getCantLLaves(self, expression):
        cant = 0
        for i in range(0,len(expression)):
            if i != len(expression)-1:
                if (expression[i] == "{" and expression[i+1] == "}") or (expression[i] == "{" and expression[i+1] == ":" and expression[i+2] == "?" and expression[i+3] == "}"):
                    cant += 1
        return cant
        
