from Enum.typeExpression import typeExpression
from Environment.Environment import Environment
from Environment.Symbol import Symbol
from Abstract.Expression import Expression
import math

class Casteo(Expression):
    def __init__(self, Exp: Expression, typeExp: typeExpression, fila, columna):
        self.Exp = Exp
        self.typeExp = typeExp
        self.fila = fila
        self.columna = columna

    def execute(self, environment: Environment)->Symbol:
        Value = self.Exp.execute(environment)
        #print(self.typeExp)
        if(self.typeExp == typeExpression.INTEGER):
            if(Value.getType() == typeExpression.FLOAT):
                return Symbol(
                        "",
                        math.trunc(float(Value.getValue())),
                        typeExpression.INTEGER,0,0
                    )
            elif(Value.getType() == typeExpression.USIZE):
                return Symbol(
                        "",
                        int(Value.getValue()),
                        typeExpression.INTEGER,0,0
                    )
            elif(Value.getType() == typeExpression.INTEGER):
                return Symbol(
                        "",
                        int(Value.getValue()),
                        typeExpression.INTEGER,0,0
                    )
            else:
                ruta = "Salida.txt"
                archivo = open(ruta, "a")
                archivo.write("Error: No se puede castear a entero\n")
                archivo.close()
                #archivo = open("Errores/Errores.txt", "a")
                #archivo.write("Error: No se puede castear a entero\n")
                #archivo.close()
                Environment.saveError("Error: No se puede castear a entero",'Local', self.fila, self.columna)
        elif(self.typeExp == typeExpression.FLOAT):
            if(Value.getType() == typeExpression.INTEGER):
                return Symbol(
                        "",
                        float(Value.getValue()),
                        typeExpression.FLOAT,0,0
                    )
            else:
                ruta = "Salida.txt"
                archivo = open(ruta, "a")
                archivo.write("Error: No se puede castear a float\n")
                archivo.close()
                #archivo = open("Errores/Errores.txt", "a")
                #archivo.write("Error: No se puede castear a entero\n")
                #archivo.close()
                Environment.saveError("Error: No se puede castear a float",'Local', self.fila, self.columna)
        elif(self.typeExp == typeExpression.PSTRING):
            return Symbol(
                "",
                str(Value.getValue()),
                typeExpression.PSTRING,0,0
            )
        elif(self.typeExp == typeExpression.STRING):
            return Symbol(
                "",
                str(Value.getValue()),
                typeExpression.STRING,0,0
            )    
        elif(self.typeExp == typeExpression.CHAR):
            if(Value.getType() == typeExpression.INTEGER):
                return Symbol(
                    "",
                    chr(Value.getValue()),
                    typeExpression.CHAR,0,0
                )
            else:
                ruta = "Salida.txt"
                archivo = open(ruta, "a")
                archivo.write("Error: No se puede castear a char\n")
                archivo.close()
                #archivo = open("Errores/Errores.txt", "a")
                #archivo.write("Error: No se puede castear a entero\n")
                #archivo.close()
                Environment.saveError("Error: No se puede castear a char",'Local', self.fila, self.columna)
        elif(self.typeExp == typeExpression.USIZE):
            if(Value.getType() == typeExpression.INTEGER):
                return Symbol(
                        "",
                        int(Value.getValue()),
                        typeExpression.USIZE,0,0
                    )
            else:
                ruta = "Salida.txt"
                archivo = open(ruta, "a")
                archivo.write("Error: No se puede castear a usize\n")
                archivo.close()
                #archivo = open("Errores/Errores.txt", "a")
                #archivo.write("Error: No se puede castear a entero
                Environment.saveError("Error: No se puede castear a usize",'Local', self.fila, self.columna)
        else: 
            ruta = "Salida.txt"
            archivo = open(ruta, "a")
            archivo.write("Error: No se puede castear con ese tipo "+"\n")
            archivo.close()
            #archivo = open("Errores/Errores.txt", "a")
            #archivo.write("Error: No se puede castear a "+str(self.typeExp)+"\n")
            #archivo.close()
            Environment.saveError("Error: No se puede castear con ese tipo",'Local', self.fila, self.columna)
        return Symbol("",0,typeExpression.INTEGER,0,0) 
        