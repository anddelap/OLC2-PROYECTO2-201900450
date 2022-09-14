from Enum.typeExpression import typeExpression
from Enum.arithmeticOperation import arithmeticOperation
from Enum.Dominant import Dominant
from Environment.Environment import Environment
from Environment.Symbol import Symbol
from Abstract.Expression import Expression
import math

class Arithmetic(Expression):
    def __init__(self, leftExp: Expression, rightExp: Expression, operation: arithmeticOperation, fila, columna, PotType):
        self.leftExp = leftExp
        self.rightExp = rightExp
        self.operation = operation
        self.fila = fila
        self.columna = columna
        self.PotType = PotType
    
    def execute(self, environment: Environment)->Symbol:
        #Resolvemos la expresion de la izquierda
        leftValue = self.leftExp.execute(environment)
        #Resolvemos de la derecha
        if self.rightExp != None:
            rightValue = self.rightExp.execute(environment)
            #Obtenemos dominante
            dominant = Dominant[leftValue.getType().value][rightValue.getType().value]
            #print(self.PotType)
            if(self.operation == arithmeticOperation.PLUS):
                if(dominant == typeExpression.PSTRING):
                    return Symbol(
                        "",
                        str(leftValue.getValue()) + str(rightValue.getValue()),
                        typeExpression.PSTRING,0,0
                    )
                elif(dominant == typeExpression.STRING):
                    return Symbol(
                        "",
                        str(leftValue.getValue()) + str(rightValue.getValue()),
                        typeExpression.STRING,0,0
                    )
                elif(dominant == typeExpression.INTEGER):
                    return Symbol(
                        "",
                        int(leftValue.getValue()) + int(rightValue.getValue()),
                        typeExpression.INTEGER,0,0
                    )
                elif(dominant == typeExpression.FLOAT):
                    return Symbol(
                        "",
                        float(leftValue.getValue()) + float(rightValue.getValue()),
                        typeExpression.FLOAT,0,0
                    )
                elif(dominant == typeExpression.USIZE):
                    return Symbol(
                        "",
                        int(leftValue.getValue()) + int(rightValue.getValue()),
                        typeExpression.USIZE,0,0
                    )
                elif(dominant == typeExpression.BOOL):
                    archivo = open("Salida.txt", "a")
                    archivo.write("No es posible sumar "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue())+"\n")
                    archivo.close()
                    #archivo = open("Errores/Errores.txt", "a")
                    #archivo.write("No es posible sumar "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue())+"\n")
                    #archivo.close()
                    Environment.saveError("No es posible sumar "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue()), 'Local', self.fila, self.columna)
                elif(dominant == typeExpression.CHAR):
                    archivo = open("Salida.txt", "a")
                    archivo.write("No es posible sumar "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue())+"\n")
                    archivo.close()
                    #archivo = open("Errores/Errores.txt", "a")
                    #archivo.write("No es posible sumar "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue())+"\n")
                    #archivo.close()
                    Environment.saveError("No es posible sumar "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue()), 'Local', self.fila, self.columna)
                else: 
                    archivo = open("Salida.txt", "a")
                    archivo.write("No es posible sumar "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue())+"\n")
                    archivo.close()
                    #archivo = open("Errores/Errores.txt", "a")
                    #archivo.write("No es posible sumar "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue())+"\n")
                    #archivo.close()
                    Environment.saveError("No es posible sumar "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue()), 'Local', self.fila, self.columna)
            elif (self.operation == arithmeticOperation.MINUS):
                if(dominant == typeExpression.STRING):
                    archivo = open("Salida.txt", "a")
                    archivo.write("No es posible restar "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue())+"\n")
                    archivo.close()
                    #archivo = open("Errores/Errores.txt", "a")
                    #archivo.write("No es posible restar "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue())+"\n")
                    #archivo.close()
                    Environment.saveError("No es posible restar "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue()), 'Local', self.fila, self.columna)
                elif(dominant == typeExpression.INTEGER):
                    return Symbol(
                        "",
                        int(leftValue.getValue()) - int(rightValue.getValue()),
                        typeExpression.INTEGER,0,0
                    )
                elif(dominant == typeExpression.USIZE):
                    return Symbol(
                        "",
                        int(leftValue.getValue()) - int(rightValue.getValue()),
                        typeExpression.USIZE,0,0
                    )
                elif(dominant == typeExpression.FLOAT):
                    return Symbol(
                        "",
                        float(leftValue.getValue()) - float(rightValue.getValue()),
                        typeExpression.FLOAT,0,0
                    )
                elif(dominant == typeExpression.BOOL):
                    archivo = open("Salida.txt", "a")
                    archivo.write("No es posible restar "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue())+"\n")
                    archivo.close()
                    #archivo = open("Errores/Errores.txt", "a")
                    #archivo.write("No es posible restar "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue())+"\n")
                    #archivo.close()
                    Environment.saveError("No es posible restar "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue()), 'Local', self.fila, self.columna)  
                elif(dominant == typeExpression.CHAR):
                    archivo = open("Salida.txt", "a")
                    archivo.write("No es posible restar "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue())+"\n")
                    archivo.close()
                    #archivo = open("Errores/Errores.txt", "a")
                    #archivo.write("No es posible restar "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue())+"\n")
                    #archivo.close()
                    Environment.saveError("No es posible restar "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue()), 'Local', self.fila, self.columna)    
                else: 
                    archivo = open("Salida.txt", "a")
                    archivo.write("No es posible restar "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue())+"\n")
                    archivo.close()
                    #archivo = open("Errores/Errores.txt", "a")
                    #archivo.write("No es posible restar "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue())+"\n")
                    #archivo.close()
                    Environment.saveError("No es posible restar "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue()), 'Local', self.fila, self.columna)      
            elif (self.operation == arithmeticOperation.MULTIPLY):
                if(dominant == typeExpression.STRING):
                    archivo = open("Salida.txt", "a")
                    archivo.write("No es posible multiplicar "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue())+"\n")
                    archivo.close()
                    #archivo = open("Errores/Errores.txt", "a")
                    #archivo.write("No es posible multiplicar "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue())+"\n")
                    #archivo.close()
                    Environment.saveError("No es posible multiplicar "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue()), 'Local', self.fila, self.columna)
                elif(dominant == typeExpression.INTEGER):
                    return Symbol(
                        "",
                        int(leftValue.getValue()) * int(rightValue.getValue()),
                        typeExpression.INTEGER,0,0
                    )
                elif(dominant == typeExpression.USIZE):
                    return Symbol(
                        "",
                        int(leftValue.getValue()) * int(rightValue.getValue()),
                        typeExpression.USIZE,0,0
                    )
                elif(dominant == typeExpression.FLOAT):
                    return Symbol(
                        "",
                        float(leftValue.getValue()) * float(rightValue.getValue()),
                        typeExpression.FLOAT,0,0
                    )
                elif(dominant == typeExpression.BOOL):
                    archivo = open("Salida.txt", "a")
                    archivo.write("No es posible multiplicar "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue())+"\n")
                    archivo.close()
                    #archivo = open("Errores/Errores.txt", "a")
                    #archivo.write("No es posible multiplicar "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue())+"\n")
                    #archivo.close()
                    Environment.saveError("No es posible multiplicar "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue()), 'Local', self.fila, self.columna)
                elif(dominant == typeExpression.CHAR):
                    archivo = open("Salida.txt", "a")
                    archivo.write("No es posible multiplicar "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue())+"\n")
                    archivo.close()
                    #archivo = open("Errores/Errores.txt", "a")
                    #archivo.write("No es posible multiplicar "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue())+"\n")
                    #archivo.close()
                    Environment.saveError("No es posible multiplicar "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue()), 'Local', self.fila, self.columna)
                else: 
                    archivo = open("Salida.txt", "a")
                    archivo.write("No es posible multiplicar "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue())+"\n")
                    archivo.close()
                    #archivo = open("Errores/Errores.txt", "a")
                    #archivo.write("No es posible multiplicar "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue())+"\n")
                    #archivo.close()
                    Environment.saveError("No es posible multiplicar "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue()), 'Local', self.fila, self.columna)
            elif (self.operation == arithmeticOperation.DIV):
                if(rightValue.getValue()!=0):
                    if(dominant == typeExpression.STRING):
                        archivo = open("Salida.txt", "a")
                        archivo.write("No es posible dividir "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue())+"\n")
                        archivo.close()
                        #archivo = open("Errores/Errores.txt", "a")
                        #archivo.write("No es posible dividir "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue())+"\n")
                        #archivo.close()
                        Environment.saveError("No es posible dividir "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue()), 'Local', self.fila, self.columna)
                    elif(dominant == typeExpression.INTEGER):
                        return Symbol(
                            "",
                            math.trunc(int(leftValue.getValue()) / int(rightValue.getValue())),
                            typeExpression.INTEGER,0,0
                        )
                    elif(dominant == typeExpression.USIZE):
                        return Symbol(
                            "",
                            int(leftValue.getValue()) + int(rightValue.getValue()),
                            typeExpression.USIZE,0,0
                        )
                    elif(dominant == typeExpression.FLOAT):
                        return Symbol(
                            "",
                            float(leftValue.getValue()) / float(rightValue.getValue()),
                            typeExpression.FLOAT,0,0
                        )
                    elif(dominant == typeExpression.BOOL):
                        archivo = open("Salida.txt", "a")
                        archivo.write("No es posible dividir "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue())+"\n")
                        archivo.close()
                        #archivo = open("Errores/Errores.txt", "a")
                        #archivo.write("No es posible dividir "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue())+"\n")
                        #archivo.close()
                        Environment.saveError("No es posible dividir "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue()), 'Local', self.fila, self.columna)
                    elif(dominant == typeExpression.CHAR):
                        archivo = open("Salida.txt", "a")
                        archivo.write("No es posible dividir "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue())+"\n")
                        archivo.close()
                        #archivo = open("Errores/Errores.txt", "a")
                        #archivo.write("No es posible dividir "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue())+"\n")
                        #archivo.close()
                        Environment.saveError("No es posible dividir "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue()), 'Local', self.fila, self.columna)
                    else: 
                        archivo = open("Salida.txt", "a")
                        archivo.write("No es posible dividir "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue())+"\n")
                        archivo.close()
                        #archivo = open("Errores/Errores.txt", "a")
                        #archivo.write("No es posible dividir "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue())+"\n")
                        #archivo.close()
                        Environment.saveError("No es posible dividir "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue()), 'Local', self.fila, self.columna) 
                else:
                    archivo = open("Salida.txt", "a")
                    archivo.write("No es posible dividir "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue())+"\n")
                    archivo.close()
                    #archivo = open("Errores/Errores.txt", "a")
                    #archivo.write("No es posible dividir "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue())+"\n")
                    #archivo.close()
                    Environment.saveError("No es posible dividir "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue()), 'Local', self.fila, self.columna)
            elif (self.operation == arithmeticOperation.POTENCY):
                if(dominant == typeExpression.STRING):
                    archivo = open("Salida.txt", "a")
                    archivo.write("No es posible realizar la potencia con "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue())+"\n")
                    archivo.close()
                    #archivo = open("Errores/Errores.txt", "a")
                    #archivo.write("No es posible realizar la potencia con "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue())+"\n")
                    #archivo.close()
                    Environment.saveError("No es realizar la potencia con "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue()), 'Local', self.fila, self.columna)
                elif(dominant == typeExpression.INTEGER):
                    if (self.PotType == "i64"):
                        return Symbol(
                            "",
                            int(leftValue.getValue()) ** int(rightValue.getValue()),
                            typeExpression.INTEGER,0,0
                        )
                    else:
                        archivo = open("Salida.txt", "a")
                        archivo.write("No es posible realizar la potencia con "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue())+"\n")
                        archivo.close()
                        #archivo = open("Errores/Errores.txt", "a")
                        #archivo.write("No es posible realizar la potencia con "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue())+"\n")
                        #archivo.close()
                        Environment.saveError("No es realizar la potencia con "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue()), 'Local', self.fila, self.columna)
                elif(dominant == typeExpression.FLOAT):
                    if (self.PotType == "f64"):
                        return Symbol(
                            "",
                            float(leftValue.getValue()) ** float(rightValue.getValue()),
                            typeExpression.FLOAT,0,0
                        )
                    else:
                        archivo = open("Salida.txt", "a")
                        archivo.write("No es posible realizar la potencia con "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue())+"\n")
                        archivo.close()
                        #archivo = open("Errores/Errores.txt", "a")
                        #archivo.write("No es posible realizar la potencia con "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue())+"\n")
                        #archivo.close()
                        Environment.saveError("No es realizar la potencia con "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue()), 'Local', self.fila, self.columna)
                elif(dominant == typeExpression.BOOL):
                        archivo = open("Salida.txt", "a")
                        archivo.write("No es posible realizar la potencia con "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue())+"\n")
                        archivo.close()
                        #archivo = open("Errores/Errores.txt", "a")
                        #archivo.write("No es posible realizar la potencia con "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue())+"\n")
                        #archivo.close()
                        Environment.saveError("No es realizar la potencia con "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue()), 'Local', self.fila, self.columna)
                elif(dominant == typeExpression.CHAR):
                        archivo = open("Salida.txt", "a")
                        archivo.write("No es posible realizar la potencia con "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue())+"\n")
                        archivo.close()
                        #archivo = open("Errores/Errores.txt", "a")
                        #archivo.write("No es posible realizar la potencia con "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue())+"\n")
                        #archivo.close()
                        Environment.saveError("No es realizar la potencia con "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue()), 'Local', self.fila, self.columna)
                else: 
                        archivo = open("Salida.txt", "a")
                        archivo.write("No es posible realizar la potencia con "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue())+"\n")
                        archivo.close()
                        #archivo = open("Errores/Errores.txt", "a")
                        #archivo.write("No es posible realizar la potencia con "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue())+"\n")
                        #archivo.close()
                        Environment.saveError("No es realizar la potencia con "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue()), 'Local', self.fila, self.columna)     
            elif (self.operation == arithmeticOperation.MODULE):
                if(dominant == typeExpression.STRING):
                    archivo = open("Salida.txt", "a")
                    archivo.write("No es posible realizar la operacion modulo con "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue())+"\n")
                    archivo.close()
                    #archivo = open("Errores/Errores.txt", "a")
                    #archivo.write("No es posible realizar la operacion modulo con "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue())+"\n")
                    #archivo.close()
                    Environment.saveError("No es realizar la operacion modulo con "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue()), 'Local', self.fila, self.columna)
                elif(dominant == typeExpression.INTEGER):
                    return Symbol(
                        "",
                        int(leftValue.getValue()) % int(rightValue.getValue()),
                        typeExpression.INTEGER,0,0
                    )
                elif(dominant == typeExpression.USIZE):
                    return Symbol(
                        "",
                        int(leftValue.getValue()) % int(rightValue.getValue()),
                        typeExpression.USIZE,0,0
                    )
                elif(dominant == typeExpression.FLOAT):
                    return Symbol(
                        "",
                        float(leftValue.getValue()) % float(rightValue.getValue()),
                        typeExpression.FLOAT,0,0
                    )
                elif(dominant == typeExpression.BOOL):
                    archivo = open("Salida.txt", "a")
                    archivo.write("No es posible realizar la operacion modulo con "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue())+"\n")
                    archivo.close()
                    #archivo = open("Errores/Errores.txt", "a")
                    #archivo.write("No es posible realizar la operacion modulo con "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue())+"\n")
                    #archivo.close()
                    Environment.saveError("No es realizar la operacion modulo con "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue()), 'Local', self.fila, self.columna)
                elif(dominant == typeExpression.CHAR):
                    archivo = open("Salida.txt", "a")
                    archivo.write("No es posible realizar la operacion modulo con "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue())+"\n")
                    archivo.close()
                    #archivo = open("Errores/Errores.txt", "a")
                    #archivo.write("No es posible realizar la operacion modulo con "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue())+"\n")
                    #archivo.close()
                    Environment.saveError("No es realizar la operacion modulo con "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue()), 'Local', self.fila, self.columna)
                else: 
                    archivo = open("Salida.txt", "a")
                    archivo.write("No es posible realizar la operacion modulo con "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue())+"\n")
                    archivo.close()
                    #archivo = open("Errores/Errores.txt", "a")
                    #archivo.write("No es posible realizar la operacion modulo con "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue())+"\n")
                    #archivo.close()
                    Environment.saveError("No es realizar la operacion modulo con "+ str(leftValue.getValue()) + " y "+ str(rightValue.getValue()), 'Local', self.fila, self.columna)
        else:
            if (self.operation == arithmeticOperation.NEGATIVE):
                if(leftValue.getType()== typeExpression.INTEGER):
                    return Symbol(
                        "",
                        int(leftValue.getValue()) * int(-1),
                        typeExpression.INTEGER,0,0
                    )
                elif (leftValue.getType()== typeExpression.FLOAT):
                    return Symbol(
                        "",
                        float(leftValue.getValue()) * float(-1),
                        typeExpression.FLOAT,0,0
                    )
                else:
                    archivo = open("Salida.txt", "a")
                    archivo.write("No es posible volver a negativo con "+ str(leftValue.getValue())+"\n")
                    archivo.close()
                    #archivo = open("Errores/Errores.txt", "a")
                    #archivo.write("No es posible volver a negativo con "+ str(leftValue.getValue())+"\n")
                    #archivo.close()
                    Environment.saveError("No es posible volver a negativo con "+ str(leftValue.getValue()), 'Local', self.fila, self.columna)
        return Symbol("",0,typeExpression.INTEGER,0,0) 

        
