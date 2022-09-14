from Enum.typeExpression import typeExpression
from Environment.Environment import Environment
from Environment.Symbol import Symbol
from Abstract.Expression import Expression
from Enum.nativeFunction import nativeFunction
from Expression.Array import Array
from Expression.Primitive import Primitive
import math
class NativeFunction(Expression):
    def __init__(self, Exp: Expression, Exp2: Expression,typeExp: typeExpression,operation: nativeFunction,fila,columna):
        self.Exp = Exp
        self.Exp2 = Exp2
        self.typeExp = typeExp
        self.operation = operation
        self.fila = fila
        self.columna = columna

    def execute(self, environment: Environment)->Symbol:
        Value = self.Exp.execute(environment)
        if(self.typeExp == None):
            if(self.operation == nativeFunction.TO_STRING):
                return Symbol(
                    "",
                    str(Value.getValue()),
                    typeExpression.STRING,0,0
                )
            elif(self.operation == nativeFunction.TO_OWNED):
                return Symbol(
                    "",
                    str(Value.getValue()),
                    typeExpression.STRING,0,0
                )
            elif(self.operation == nativeFunction.SQRT):
                if(Value.getType() == typeExpression.INTEGER):
                    return Symbol(
                        "",
                        math.sqrt(Value.getValue()),
                        typeExpression.FLOAT,0,0
                    )
                elif(Value.getType() == typeExpression.FLOAT):
                    return Symbol(
                        "",
                        math.sqrt(Value.getValue()),
                        typeExpression.FLOAT,0,0
                    )
                else:
                    archivo = open("Salida.txt", "a")
                    archivo.write("No es posible realizar la operacion raiz con "+ str(Value.getValue()) +"\n")
                    archivo.close()
                    #archivo = open("Errores/Errores.txt", "a")
                    #archivo.write("No es posible realizar la operacion raiz con "+ str(Value.getValue()) +"\n")
                    #archivo.close()
                    Environment.saveError("No es posible realizar la operacion raiz con "+ str(Value.getValue()), 'Local', self.fila, self.columna)
            elif(self.operation == nativeFunction.ABS):
                if(Value.getType() == typeExpression.INTEGER):
                    return Symbol(
                        "",
                        abs(Value.getValue()),
                        typeExpression.FLOAT,0,0
                    )
                elif(Value.getType() == typeExpression.FLOAT):
                    return Symbol(
                        "",
                        abs(Value.getValue()),
                        typeExpression.FLOAT,0,0
                    )
                else:
                    archivo = open("Salida.txt", "a")
                    archivo.write("No es posible realizar el numero absoluto con "+ str(Value.getValue()) +"\n")
                    archivo.close()
                    #archivo = open("Errores/Errores.txt", "a")
                    #archivo.write("No es posible realizar la operacion raiz con "+ str(Value.getValue()) +"\n")
                    #archivo.close()
                    Environment.saveError("No es posible realizar el numero absoluto con "+ str(Value.getValue()), 'Local', self.fila, self.columna)
            elif(self.operation == nativeFunction.CLONE):
                if(Value.getType() == typeExpression.STRING):
                    return Symbol(
                        "",
                        Value.getValue(),
                        typeExpression.STRING,0,0
                    )
                elif(Value.getType() == typeExpression.VECTOR):
                    return Symbol(
                        "",
                        Value.getValue(),
                        typeExpression.VECTOR,0,0
                    )
                else:
                    archivo = open("Salida.txt", "a")
                    archivo.write("Error: No es posible clonar el valor "+ str(Value.getValue()) +"\n")
                    archivo.close()
                    #archivo = open("Errores/Errores.txt", "a")
                    #archivo.write("No es posible clonar el valor "+ str(Value.getValue()) +"\n")
                    #archivo.close()
                    Environment.saveError("Error: No es posible clonar el valor "+ str(Value.getValue()), 'Local', self.fila, self.columna)
            elif(self.operation == nativeFunction.CHARS):
                if(Value.getType() == typeExpression.PSTRING):
                    lista = []
                    for value in Value.getValue():
                        lista.append(Symbol("",value,typeExpression.CHAR,0,0))
                    tempVar = Symbol("",lista,typeExpression.ARRAY,0,0)
                    tempVar.array = True
                    return tempVar
                else:
                    archivo = open("Salida.txt", "a")
                    archivo.write("Error: No es posible realizar la operacion chars con "+ str(Value.getValue()) +"\n")
                    archivo.close()
                    #archivo = open("Errores/Errores.txt", "a")
                    #archivo.write("No es posible realizar la operacion raiz con "+ str(Value.getValue()) +"\n")
                    #archivo.close()
                    Environment.saveError("Error: No es posible realizar la operacion chars con "+ str(Value.getValue()), 'Local', self.fila, self.columna)
            elif(self.operation == nativeFunction.LEN):
                if(Value.getType()==typeExpression.ARRAY or Value.getType()==typeExpression.VECTOR):
                    return Symbol(
                        "",
                        len(Value.getValue()),
                        typeExpression.INTEGER,0,0
                    )
                else:
                    archivo = open("Salida.txt", "a")
                    archivo.write("Error: Funcion len es solo para arreglos o vectores\n")
                    archivo.close()
                    #archivo = open("Errores/Errores.txt", "a")
                    #archivo.write("No es posible realizar la operacion raiz con "+ str(Value.getValue()) +"\n")
                    #archivo.close()
                    Environment.saveError("Error: Funcion len es solo para arreglos o vectores", 'Local', self.fila, self.columna)
            elif(self.operation == nativeFunction.CONTAINS):
                Value2 = self.Exp2.execute(environment)
                if(Value.getType() == typeExpression.ARRAY or Value.getType() == typeExpression.VECTOR):
                    for tempExp in Value.getValue():
                        if(tempExp.getValue() == Value2.getValue()):
                            return Symbol(
                                "",
                                True,
                                typeExpression.BOOL,0,0
                            )
                    return Symbol(
                                "",
                                False,
                                typeExpression.BOOL,0,0
                            ) 
                else:
                    archivo = open("Salida.txt", "a")
                    archivo.write("Error: Funcion len es solo para arreglos o vectores\n")
                    archivo.close()
                    #archivo = open("Errores/Errores.txt", "a")
                    #archivo.write("No es posible realizar la operacion raiz con "+ str(Value.getValue()) +"\n")
                    #archivo.close()
                    Environment.saveError("Error: Funcion len es solo para arreglos o vectores", 'Local', self.fila, self.columna)   
            elif(self.operation == nativeFunction.CAPACITY):
                if(Value.getType() == typeExpression.VECTOR):
                    if(Value.getVectorCapacity() == 0):
                        return Symbol(
                            "",
                            len(Value.getValue())+1,
                            typeExpression.INTEGER,0,0
                        )
                    else:
                        return Symbol(
                            "",
                            Value.getVectorCapacity().execute(environment).getValue(),
                            typeExpression.INTEGER,0,0
                        )
                else:
                    archivo = open("Salida.txt", "a")
                    archivo.write("Error: Funcion capacity es solo para vectores\n")
                    archivo.close()
                    #archivo = open("Errores/Errores.txt", "a")
                    #archivo.write("No es posible realizar la operacion raiz con "+ str(Value.getValue()) +"\n")
                    #archivo.close()
                    Environment.saveError("Error: Funcion capacity es solo para vectores", 'Local', self.fila, self.columna)
            """ elif(self.operation == nativeFunction.PUSH):
                if(Value.getType() == typeExpression.ARRAY):
                    Exp2 = self.Exp2.execute(environment)

                    return tempVar
                else:
                    archivo = open("Salida.txt", "a")
                    archivo.write("Error: No es posible realizar la operacion push con "+ str(Value.getValue()) +"\n")
                    archivo.close()
                    #archivo = open("Errores/Errores.txt", "a")
                    #archivo.write("No es posible realizar la operacion raiz con "+ str(Value.getValue()) +"\n")
                    #archivo.close()
                    Environment.saveError("Error: No es posible realizar la operacion push con "+ str(Value.getValue()), 'Local', self.fila, self.columna) """
            """ if (self.operation == nativeFunction.FLOAT):
                if(Value.getType() == typeExpression.INTEGER):
                    return Symbol(
                        "",
                        float(Value.getValue()),
                        typeExpression.FLOAT,0,0
                    )
                else:
                    archivo = open("Salida.txt", "a")
                    archivo.write("No es posible convertir a float con "+ str(Value.getValue()) +"\n")
                    archivo.close()
                    archivo = open("Errores/Errores.txt", "a")
                    archivo.write("No es posible convertir a float con "+ str(Value.getValue()) +"\n")
                    archivo.close()
            elif (self.operation == nativeFunction.STRING):
                print(Value)
                try:
                    if (Value.isArray()):
                        valor = self.printarray(Value)
                        return Symbol(
                            "",
                            str(valor),
                            typeExpression.STRING,0,0
                        )
                    else:
                        return Symbol(
                            "",
                            str(Value.getValue()),
                            typeExpression.STRING,0,0
                        )
                except:
                    archivo = open("Salida.txt", "a")
                    archivo.write("ERROR al convertir a string con "+ str(Value.getValue()) +"\n")
                    archivo.close()
                    archivo = open("Errores/Errores.txt", "a")
                    archivo.write("ERROR al convertir a string con "+ str(Value.getValue()) +"\n")
                    archivo.close()
            elif (self.operation == nativeFunction.TYPEOF):
                try:
                    if(Value.getType()==typeExpression.STRING):
                        return Symbol(
                        "",
                        "string",
                        typeExpression.STRING,0,0
                        )
                    elif(Value.getType()==typeExpression.INTEGER):
                        return Symbol(
                            "",
                            "int64",
                            typeExpression.STRING,0,0
                        )
                    elif(Value.getType()==typeExpression.FLOAT):
                        return Symbol(
                            "",
                            "float64",
                            typeExpression.STRING,0,0
                        )
                    elif(Value.getType()==typeExpression.BOOL):
                        return Symbol(
                            "",
                            "boolean",
                            typeExpression.STRING,0,0
                        )
                    elif(Value.getType()==typeExpression.CHAR):
                        return Symbol(
                            "",
                            "char",
                            typeExpression.STRING,0,0
                        )
                except:
                    archivo = open("Salida.txt", "a")
                    archivo.write("ERROR al obtener el tipo de "+ str(Value.getValue()) +"\n")
                    archivo.close()
                    archivo = open("Errores/Errores.txt", "a")
                    archivo.write("ERROR al obtener el tipo de "+ str(Value.getValue()) +"\n")
                    archivo.close()
            elif (self.operation == nativeFunction.LENGTH):
                if(Value.isArray()):
                    Arreglo = Value.getValue()
                    print(len(Arreglo))
                    return Symbol(
                        "",
                        len(Arreglo),
                        typeExpression.INTEGER,0,0
                    )
                else:
                    return Symbol(
                        "",
                        len(Value.getValue()),
                        typeExpression.INTEGER,0,0
                    )
                    #archivo = open("Salida.txt", "a")
                    #archivo.write("ERROR: El tamaño solo puede ser de un arreglo\n")
                    #archivo.close()
                    #archivo = open("Errores/Errores.txt", "a")
                    #archivo.write("ERROR: El tamaño solo puede ser de un arreglo\n")
                    #archivo.close()
            elif (self.operation == nativeFunction.UPPER):
                if (Value.getType()==typeExpression.STRING):
                    valor = Value.getValue()
                    return Symbol(
                        "",
                        valor.upper(),
                        typeExpression.STRING,0,0
                    )
                else:
                    archivo = open("Salida.txt", "a")
                    archivo.write("Para poner todo en mayuscula se requiere un string.\n")
                    archivo.close()
                    archivo = open("Errores/Errores.txt", "a")
                    archivo.write("Para poner todo en mayuscula se requiere un string.\n")
                    archivo.close()
            elif (self.operation == nativeFunction.LOWER): 
                if (Value.getType()==typeExpression.STRING):
                    valor = Value.getValue()
                    return Symbol(
                        "",
                        valor.lower(),
                        typeExpression.STRING,0,0
                    )
                else:
                    archivo = open("Salida.txt", "a")
                    archivo.write("Para poner todo en minuscula se requiere un string.\n")
                    archivo.close()
                    archivo = open("Errores/Errores.txt", "a")
                    archivo.write("Para poner todo en minuscula se requiere un string.\n")
                    archivo.close() """
        else:
            """ if (self.operation == nativeFunction.PARSE):
                if(Value.getType() == typeExpression.STRING and self.typeExp == typeExpression.INTEGER):
                    try:
                        return Symbol(
                            "",
                            int(Value.getValue()),
                            typeExpression.INTEGER,0,0
                        )
                    except:
                        archivo = open("Salida.txt", "a")
                        archivo.write("ERROR al convertir a int "+ str(Value.getValue()) +"\n")
                        archivo.close()
                        archivo = open("Errores/Errores.txt", "a")
                        archivo.write("ERROR al convertir a int "+ str(Value.getValue()) +"\n")
                        archivo.close()
                elif(Value.getType() == typeExpression.STRING and self.typeExp == typeExpression.FLOAT):
                    try:
                        return Symbol(
                            "",
                            float(Value.getValue()),
                            typeExpression.FLOAT,0,0
                        )
                    except:
                        archivo = open("Salida.txt", "a")
                        archivo.write("ERROR al convertir a float "+ str(Value.getValue()) +"\n")
                        archivo.close()
                        archivo = open("Errores/Errores.txt", "a")
                        archivo.write("ERROR al convertir a float "+ str(Value.getValue()) +"\n")
                        archivo.close()
            elif (self.operation == nativeFunction.TRUNC):
                print(self.typeExp)
                if(Value.getType() == typeExpression.FLOAT and self.typeExp == typeExpression.INTEGER):
                    return Symbol(
                        "",
                        math.trunc(float(Value.getValue())),
                        typeExpression.INTEGER,0,0
                    )
                else:
                    archivo = open("Salida.txt", "a")
                    archivo.write("No es posible truncar con "+ str(Value.getValue()) +"\n")
                    archivo.close()
                    archivo = open("Errores/Errores.txt", "a")
                    archivo.write("No es posible truncar con "+ str(Value.getValue()) +"\n")
                    archivo.close() """
        return Symbol("",0,typeExpression.INTEGER,0,0) 
    def printarray(self, expression:Symbol):
            valor = "["
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