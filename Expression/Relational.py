from Enum.typeExpression import typeExpression
from Environment.Environment import Environment
from Environment.Symbol import Symbol
from Abstract.Expression import Expression
from Enum.relationalOperation import relationalOperation
class Relational(Expression):
    def __init__(self, leftExp: Expression, rightExp: Expression, operation: relationalOperation, fila, columna):
        self.leftExp = leftExp
        self.rightExp = rightExp
        self.operation = operation
        self.fila = fila
        self.columna = columna
    
    def execute(self, environment: Environment)->Symbol:
        #Resolvemos la expresion de la izquierda
        leftValue = self.leftExp.execute(environment)
        #Resolvemos de la derecha
        rightValue = self.rightExp.execute(environment)
        if(self.operation==relationalOperation.MAYOR):
            if(leftValue.getType()== typeExpression.STRING and rightValue.getType()== typeExpression.STRING):
                return Symbol(
                    "",
                    len(leftValue.getValue()) > len(rightValue.getValue()),
                    typeExpression.BOOL,0,0
                )
            elif(leftValue.getType()== typeExpression.INTEGER and rightValue.getType()== typeExpression.FLOAT):
                return Symbol(
                    "",
                    float(leftValue.getValue()) > rightValue.getValue(),
                    typeExpression.BOOL,0,0
                )
            elif(leftValue.getType()== typeExpression.FLOAT and rightValue.getType()== typeExpression.INTEGER):
                return Symbol(
                    "",
                    leftValue.getValue() > float(rightValue.getValue()),
                    typeExpression.BOOL,0,0
                )
            elif(leftValue.getType()== typeExpression.FLOAT and rightValue.getType()== typeExpression.FLOAT):
                return Symbol(
                    "",
                    leftValue.getValue() > rightValue.getValue(),
                    typeExpression.BOOL,0,0
                )
            elif(leftValue.getType()== typeExpression.INTEGER and rightValue.getType()== typeExpression.INTEGER):
                return Symbol(
                    "",
                    leftValue.getValue() > rightValue.getValue(),
                    typeExpression.BOOL,0,0
                )
            elif(leftValue.getType()== typeExpression.INTEGER and rightValue.getType()== typeExpression.USIZE):
                return Symbol(
                    "",
                    leftValue.getValue() > rightValue.getValue(),
                    typeExpression.BOOL,0,0
                )
            elif(leftValue.getType()== typeExpression.USIZE and rightValue.getType()== typeExpression.INTEGER):
                return Symbol(
                    "",
                    leftValue.getValue() > rightValue.getValue(),
                    typeExpression.BOOL,0,0
                )
            else:
                archivo = open("Salida.txt", "a")
                archivo.write("Error: No se puede relacionar "+str(leftValue.getValue())+" > "+str(rightValue.getValue())+"\n")
                archivo.close()
                #archivo = open("Errores/Errores.txt", "a")
                #archivo.write("Error: No se puede relacionar "+str(leftValue.getValue())+" > "+str(rightValue.getValue())+"\n")
                #archivo.close()
                Environment.saveError("Error: No se puede relacionar "+str(leftValue.getValue())+" > "+str(rightValue.getValue()), 'Global', self.fila, self.columna)
        elif (self.operation==relationalOperation.MENOR):
            if(leftValue.getType()== typeExpression.STRING and rightValue.getType()== typeExpression.STRING):
                    return Symbol(
                    "",
                    len(leftValue.getValue()) < len(rightValue.getValue()),
                    typeExpression.BOOL,0,0
                )
            elif(leftValue.getType()== typeExpression.INTEGER and rightValue.getType()== typeExpression.FLOAT):
                return Symbol(
                    "",
                    float(leftValue.getValue()) < rightValue.getValue(),
                    typeExpression.BOOL,0,0
                )
            elif(leftValue.getType()== typeExpression.FLOAT and rightValue.getType()== typeExpression.INTEGER):
                return Symbol(
                    "",
                    leftValue.getValue() < float(rightValue.getValue()),
                    typeExpression.BOOL,0,0
                )
            elif(leftValue.getType()== typeExpression.FLOAT and rightValue.getType()== typeExpression.FLOAT):
                return Symbol(
                    "",
                    leftValue.getValue() < rightValue.getValue(),
                    typeExpression.BOOL,0,0
                )
            elif(leftValue.getType()== typeExpression.INTEGER and rightValue.getType()== typeExpression.INTEGER):
                return Symbol(
                    "",
                    leftValue.getValue() < rightValue.getValue(),
                    typeExpression.BOOL,0,0
                )
            elif(leftValue.getType()== typeExpression.INTEGER and rightValue.getType()== typeExpression.USIZE):
                return Symbol(
                    "",
                    leftValue.getValue() < rightValue.getValue(),
                    typeExpression.BOOL,0,0
                )
            elif(leftValue.getType()== typeExpression.USIZE and rightValue.getType()== typeExpression.INTEGER):
                return Symbol(
                    "",
                    leftValue.getValue() < rightValue.getValue(),
                    typeExpression.BOOL,0,0
                )
            else:
                archivo = open("Salida.txt", "a")
                archivo.write("Error: No se puede relacionar "+str(leftValue.getValue())+" < "+str(rightValue.getValue())+"\n")
                archivo.close()
                #archivo = open("Errores/Errores.txt", "a")
                #archivo.write("Error: No se puede relacionar "+str(leftValue.getValue())+" < "+str(rightValue.getValue())+"\n")
                #archivo.close()
                Environment.saveError("Error: No se puede relacionar "+str(leftValue.getValue())+" < "+str(rightValue.getValue()), 'Global', self.fila, self.columna)
        elif (self.operation==relationalOperation.MAYORIGUAL):
            if(leftValue.getType()== typeExpression.STRING and rightValue.getType()== typeExpression.STRING):
                    return Symbol(
                    "",
                    len(leftValue.getValue()) >= len(rightValue.getValue()),
                    typeExpression.BOOL,0,0
                )
            elif(leftValue.getType()== typeExpression.INTEGER and rightValue.getType()== typeExpression.FLOAT):
                return Symbol(
                    "",
                    float(leftValue.getValue()) >= rightValue.getValue(),
                    typeExpression.BOOL,0,0
                )
            elif(leftValue.getType()== typeExpression.FLOAT and rightValue.getType()== typeExpression.INTEGER):
                return Symbol(
                    "",
                    leftValue.getValue() >= float(rightValue.getValue()),
                    typeExpression.BOOL,0,0
                )
            elif(leftValue.getType()== typeExpression.FLOAT and rightValue.getType()== typeExpression.FLOAT):
                return Symbol(
                    "",
                    leftValue.getValue() >= rightValue.getValue(),
                    typeExpression.BOOL,0,0
                )
            elif(leftValue.getType()== typeExpression.INTEGER and rightValue.getType()== typeExpression.INTEGER):
                return Symbol(
                    "",
                    leftValue.getValue() >= rightValue.getValue(),
                    typeExpression.BOOL,0,0
                )
            elif(leftValue.getType()== typeExpression.INTEGER and rightValue.getType()== typeExpression.USIZE):
                return Symbol(
                    "",
                    leftValue.getValue() >= rightValue.getValue(),
                    typeExpression.BOOL,0,0
                )
            elif(leftValue.getType()== typeExpression.USIZE and rightValue.getType()== typeExpression.INTEGER):
                return Symbol(
                    "",
                    leftValue.getValue() >= rightValue.getValue(),
                    typeExpression.BOOL,0,0
                )
            else:
                archivo = open("Salida.txt", "a")
                archivo.write("Error: No se puede relacionar "+str(leftValue.getValue())+" >= "+str(rightValue.getValue())+"\n")
                archivo.close()
                #archivo = open("Errores/Errores.txt", "a")
                #archivo.write("Error: No se puede relacionar "+str(leftValue.getValue())+" >= "+str(rightValue.getValue())+"\n")
                #archivo.close()
                Environment.saveError("Error: No se puede relacionar "+str(leftValue.getValue())+" >= "+str(rightValue.getValue()), 'Global', self.fila, self.columna)
        elif (self.operation==relationalOperation.MENORIGUAL):
            if(leftValue.getType()== typeExpression.STRING and rightValue.getType()== typeExpression.STRING):
                    return Symbol(
                    "",
                    len(leftValue.getValue()) <= len(rightValue.getValue()),
                    typeExpression.BOOL,0,0
                )
            elif(leftValue.getType()== typeExpression.INTEGER and rightValue.getType()== typeExpression.FLOAT):
                return Symbol(
                    "",
                    float(leftValue.getValue()) <= rightValue.getValue(),
                    typeExpression.BOOL,0,0
                )
            elif(leftValue.getType()== typeExpression.FLOAT and rightValue.getType()== typeExpression.INTEGER):
                return Symbol(
                    "",
                    leftValue.getValue() <= float(rightValue.getValue()),
                    typeExpression.BOOL,0,0
                )
            elif(leftValue.getType()== typeExpression.FLOAT and rightValue.getType()== typeExpression.FLOAT):
                return Symbol(
                    "",
                    leftValue.getValue() <= rightValue.getValue(),
                    typeExpression.BOOL,0,0
                )
            elif(leftValue.getType()== typeExpression.INTEGER and rightValue.getType()== typeExpression.INTEGER):
                return Symbol(
                    "",
                    leftValue.getValue() <= rightValue.getValue(),
                    typeExpression.BOOL,0,0
                )
            elif(leftValue.getType()== typeExpression.INTEGER and rightValue.getType()== typeExpression.USIZE):
                return Symbol(
                    "",
                    leftValue.getValue() <= rightValue.getValue(),
                    typeExpression.BOOL,0,0
                )
            elif(leftValue.getType()== typeExpression.USIZE and rightValue.getType()== typeExpression.INTEGER):
                return Symbol(
                    "",
                    leftValue.getValue() <= rightValue.getValue(),
                    typeExpression.BOOL,0,0
                )
            else:
                archivo = open("Salida.txt", "a")
                archivo.write("Error: No se puede relacionar "+str(leftValue.getValue())+" <= "+str(rightValue.getValue())+"\n")
                archivo.close()
                #archivo = open("Errores/Errores.txt", "a")
                #archivo.write("Error: No se puede relacionar "+str(leftValue.getValue())+" <= "+str(rightValue.getValue())+"\n")
                #archivo.close()
                Environment.saveError("Error: No se puede relacionar "+str(leftValue.getValue())+" <= "+str(rightValue.getValue()), 'Global', self.fila, self.columna)
        elif (self.operation==relationalOperation.IGUALIGUAL):
            if(leftValue.getType()== typeExpression.STRING and rightValue.getType()== typeExpression.STRING):
                    return Symbol(
                    "",
                    leftValue.getValue() == rightValue.getValue(),
                    typeExpression.BOOL,0,0
                )
            elif(leftValue.getType()== typeExpression.INTEGER and rightValue.getType()== typeExpression.FLOAT):
                return Symbol(
                    "",
                    float(leftValue.getValue()) == rightValue.getValue(),
                    typeExpression.BOOL,0,0
                )
            elif(leftValue.getType()== typeExpression.FLOAT and rightValue.getType()== typeExpression.INTEGER):
                return Symbol(
                    "",
                    leftValue.getValue() == float(rightValue.getValue()),
                    typeExpression.BOOL,0,0
                )
            elif(leftValue.getType()== typeExpression.FLOAT and rightValue.getType()== typeExpression.FLOAT):
                return Symbol(
                    "",
                    leftValue.getValue() == rightValue.getValue(),
                    typeExpression.BOOL,0,0
                )
            elif(leftValue.getType()== typeExpression.INTEGER and rightValue.getType()== typeExpression.INTEGER):
                return Symbol(
                    "",
                    leftValue.getValue() == rightValue.getValue(),
                    typeExpression.BOOL,0,0
                )
            elif(leftValue.getType()== typeExpression.BOOL and rightValue.getType()== typeExpression.BOOL):
                return Symbol(
                    "",
                    leftValue.getValue() == rightValue.getValue(),
                    typeExpression.BOOL,0,0
                )
            elif(leftValue.getType()== typeExpression.STRING and rightValue.getType()== typeExpression.BOOL):
                return Symbol(
                    "",
                    leftValue.getValue() == str(rightValue.getValue()),
                    typeExpression.BOOL,0,0
                )
            elif(leftValue.getType()== typeExpression.BOOL and rightValue.getType()== typeExpression.STRING):
                return Symbol(
                    "",
                    str(leftValue.getValue()) == rightValue.getValue(),
                    typeExpression.BOOL,0,0
                )
            elif(leftValue.getType()== typeExpression.CHAR and rightValue.getType()== typeExpression.CHAR):
                return Symbol(
                    "",
                    leftValue.getValue() == rightValue.getValue(),
                    typeExpression.BOOL,0,0
                )
            elif(leftValue.getType()== typeExpression.INTEGER and rightValue.getType()== typeExpression.USIZE):
                return Symbol(
                    "",
                    leftValue.getValue() == rightValue.getValue(),
                    typeExpression.BOOL,0,0
                )
            elif(leftValue.getType()== typeExpression.USIZE and rightValue.getType()== typeExpression.INTEGER):
                return Symbol(
                    "",
                    leftValue.getValue() == rightValue.getValue(),
                    typeExpression.BOOL,0,0
                )
            else:
                archivo = open("Salida.txt", "a")
                archivo.write("Error: No se puede relacionar "+str(leftValue.getValue())+" == "+str(rightValue.getValue())+"\n")
                archivo.close()
                #archivo = open("Errores/Errores.txt", "a")
                #archivo.write("Error: No se puede relacionar "+str(leftValue.getValue())+" == "+str(rightValue.getValue())+"\n")
                #archivo.close()
                Environment.saveError("Error: No se puede relacionar "+str(leftValue.getValue())+" == "+str(rightValue.getValue()), 'Global', self.fila, self.columna)
        elif (self.operation==relationalOperation.DIFERENTE):
            if(leftValue.getType()== typeExpression.STRING and rightValue.getType()== typeExpression.STRING):
                    return Symbol(
                    "",
                    leftValue.getValue() != rightValue.getValue(),
                    typeExpression.BOOL,0,0
                )
            elif(leftValue.getType()== typeExpression.INTEGER and rightValue.getType()== typeExpression.FLOAT):
                return Symbol(
                    "",
                    float(leftValue.getValue()) != rightValue.getValue(),
                    typeExpression.BOOL,0,0
                )
            elif(leftValue.getType()== typeExpression.FLOAT and rightValue.getType()== typeExpression.INTEGER):
                return Symbol(
                    "",
                    leftValue.getValue() != float(rightValue.getValue()),
                    typeExpression.BOOL,0,0
                )
            elif(leftValue.getType()== typeExpression.FLOAT and rightValue.getType()== typeExpression.FLOAT):
                return Symbol(
                    "",
                    leftValue.getValue() != rightValue.getValue(),
                    typeExpression.BOOL,0,0
                )
            elif(leftValue.getType()== typeExpression.INTEGER and rightValue.getType()== typeExpression.INTEGER):
                return Symbol(
                    "",
                    leftValue.getValue() != rightValue.getValue(),
                    typeExpression.BOOL,0,0
                )
            elif(leftValue.getType()== typeExpression.BOOL and rightValue.getType()== typeExpression.BOOL):
                return Symbol(
                    "",
                    leftValue.getValue() != rightValue.getValue(),
                    typeExpression.BOOL,0,0
                )
            elif(leftValue.getType()== typeExpression.STRING and rightValue.getType()== typeExpression.BOOL):
                return Symbol(
                    "",
                    leftValue.getValue() != str(rightValue.getValue()),
                    typeExpression.BOOL,0,0
                )
            elif(leftValue.getType()== typeExpression.BOOL and rightValue.getType()== typeExpression.STRING):
                return Symbol(
                    "",
                    str(leftValue.getValue()) != rightValue.getValue(),
                    typeExpression.BOOL,0,0
                )
            elif(leftValue.getType()== typeExpression.CHAR and rightValue.getType()== typeExpression.CHAR):
                return Symbol(
                    "",
                    leftValue.getValue() != rightValue.getValue(),
                    typeExpression.BOOL,0,0
                )
            elif(leftValue.getType()== typeExpression.INTEGER and rightValue.getType()== typeExpression.USIZE):
                return Symbol(
                    "",
                    leftValue.getValue() != rightValue.getValue(),
                    typeExpression.BOOL,0,0
                )
            elif(leftValue.getType()== typeExpression.USIZE and rightValue.getType()== typeExpression.INTEGER):
                return Symbol(
                    "",
                    leftValue.getValue() != rightValue.getValue(),
                    typeExpression.BOOL,0,0
                )
            else:
                archivo = open("Salida.txt", "a")
                archivo.write("Error: No se puede relacionar "+str(leftValue.getValue())+" != "+str(rightValue.getValue())+"\n")
                archivo.close()  
                #archivo = open("Errores/Errores.txt", "a")
                #archivo.write("Error: No se puede relacionar "+str(leftValue.getValue())+" != "+str(rightValue.getValue())+"\n")
                #archivo.close()
                Environment.saveError("Error: No se puede relacionar "+str(leftValue.getValue())+" != "+str(rightValue.getValue()), 'Global', self.fila, self.columna)  
