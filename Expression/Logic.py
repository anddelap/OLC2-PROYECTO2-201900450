from Enum.typeExpression import typeExpression
from Environment.Environment import Environment
from Environment.Symbol import Symbol
from Abstract.Expression import Expression
from Enum.logicOperation import logicOperation

class Logic(Expression):
    def __init__(self, leftExp: Expression, rightExp: Expression, operation: logicOperation, fila, columna):
        self.leftExp = leftExp
        self.rightExp = rightExp
        self.operation = operation
        self.fila = fila
        self.columna = columna
    def execute(self, environment: Environment)->Symbol:
        #Resolvemos la expresion de la izquierda
        leftValue = self.leftExp.execute(environment)
        #Environment.aumentarContadorL()
        #Obtenemos dominante
        if(self.rightExp == None):
           if (self.operation == logicOperation.NOT):
                if(leftValue.getType()==typeExpression.BOOL):
                    Environment.saveExpression("L"+str(Environment.getEtiqueta())+":")
                    Environment.aumentarContadorL()
                    Environment.saveExpression("t"+str(Environment.getContador())+" = 0;")
                    Environment.saveExpression("goto L"+str(Environment.getEtiqueta()+1)+";")
                    Environment.saveExpression("L"+str(Environment.getEtiqueta())+":")
                    Environment.aumentarContadorL()
                    Environment.saveExpression("t"+str(Environment.getContador())+" = 1;")
                    Environment.saveExpression("L"+str(Environment.getEtiqueta())+":")
                    Environment.aumentarContadorL()
                    Environment.saveExpression("if ( t"+str(Environment.getContador())+" == 1) goto L"+str(Environment.getEtiqueta())+";")
                    Environment.saveTemporal("", "", "", 0)
                    #Environment.aumentarContadorL()
                    Environment.saveExpression("goto L"+str(Environment.getEtiqueta()+1)+";")
                    return Symbol(
                        "",
                        not leftValue.getValue(),
                        typeExpression.BOOL,0,0
                    )
                else:
                    archivo = open("Salida.txt", "a")
                    archivo.write("No es posible realizar la operacion not con "+ str(leftValue.getValue()) +"\n")
                    archivo.close()
                    #archivo = open("Errores/Errores.txt", "a")
                    #archivo.write("No es posible realizar la operacion not con "+ str(leftValue.getValue()) +"\n")
                    #archivo.close()
                    Environment.saveError("No es posible realizar la operacion not con "+ str(leftValue.getValue()), 'Global', self.fila, self.columna)
        else:      
            #Resolvemos de la derecha
            #Environment.saveExpression("Hace Esto:")
            #print(str(Environment.getEtiqueta()))
            Environment.saveExpression("L"+str(Environment.getEtiqueta())+":")
            Environment.aumentarContadorL()
            Environment.aumentarContadorL()
            rightValue = self.rightExp.execute(environment)
            if (self.operation == logicOperation.AND):
                if(leftValue.getType() == typeExpression.BOOL and rightValue.getType() == typeExpression.BOOL):
                    #print("En and"+str(rightValue.getType()))
                    #print("En and"+str(leftValue.getType()))
                    Environment.saveExpression("L"+str(Environment.getEtiqueta())+":")
                    Environment.aumentarContadorL()
                    Environment.saveExpression("t"+str(Environment.getContador())+" = 1;")
                    Environment.saveExpression("goto L"+str(Environment.getEtiqueta()+1)+";")
                    Environment.saveExpression("L"+str(Environment.getEtiqueta()-2)+":"+" L"+str(Environment.getEtiqueta())+":")
                    Environment.aumentarContadorL()
                    Environment.saveExpression("t"+str(Environment.getContador())+" = 0;")
                    Environment.saveExpression("L"+str(Environment.getEtiqueta())+":")
                    Environment.aumentarContadorL()
                    Environment.saveExpression("if ( t"+str(Environment.getContador())+" == 1) goto L"+str(Environment.getEtiqueta())+";")
                    Environment.saveTemporal("", "", "", 0)
                    #Environment.aumentarContadorL()
                    Environment.saveExpression("goto L"+str(Environment.getEtiqueta()+1)+";")
                    #Environment.aumentarContadorL()
                    return Symbol(
                        "",
                        leftValue.getValue() and rightValue.getValue(),
                        typeExpression.BOOL,0,0
                    )
                else:
                    archivo = open("Salida.txt", "a")
                    archivo.write("No es posible realizar la operacion and con "+ str(leftValue.getValue()) +" y " + str(rightValue.getValue()) +"\n")
                    archivo.close()
                    #archivo = open("Errores/Errores.txt", "a")
                    #archivo.write("No es posible realizar la operacion and con "+ str(leftValue.getValue()) +" y " + str(rightValue.getValue()) +"\n")
                    #archivo.close()
                    Environment.saveError("No es posible realizar la operacion and con "+ str(leftValue.getValue()) +" y " + str(rightValue.getValue()), 'Global', self.fila, self.columna)
            elif (self.operation == logicOperation.OR):
                if(leftValue.getType() == typeExpression.BOOL and rightValue.getType() == typeExpression.BOOL):
                    Environment.saveExpression("L"+str(Environment.getEtiqueta()-2)+":"+" L"+str(Environment.getEtiqueta())+":")
                    #Environment.saveExpression("L"+str(Environment.getEtiqueta())+":")
                    Environment.aumentarContadorL()
                    Environment.saveExpression("t"+str(Environment.getContador())+" = 1;")
                    Environment.saveExpression("goto L"+str(Environment.getEtiqueta()+1)+";")
                    Environment.saveExpression("L"+str(Environment.getEtiqueta())+":")
                    Environment.aumentarContadorL()
                    Environment.saveExpression("t"+str(Environment.getContador())+" = 0;")
                    Environment.saveExpression("L"+str(Environment.getEtiqueta())+":")
                    Environment.aumentarContadorL()
                    Environment.saveExpression("if ( t"+str(Environment.getContador())+" == 1) goto L"+str(Environment.getEtiqueta())+";")
                    Environment.saveTemporal("", "", "", 0)
                    #Environment.aumentarContadorL()
                    Environment.saveExpression("goto L"+str(Environment.getEtiqueta()+1)+";")
                    #Environment.aumentarContadorL()
                    return Symbol(
                        "",
                        leftValue.getValue() or rightValue.getValue(),
                        typeExpression.BOOL,0,0
                    )
                else:
                    archivo = open("Salida.txt", "a")
                    archivo.write("No es posible realizar la operacion or con "+ str(leftValue.getValue()) +" y " + str(rightValue.getValue()) +"\n")
                    archivo.close()
                    #archivo = open("Errores/Errores.txt", "a")
                    #archivo.write("No es posible realizar la operacion or con "+ str(leftValue.getValue()) +" y " + str(rightValue.getValue()) +"\n")
                    #archivo.close()
                    Environment.saveError("No es posible realizar la operacion or con "+ str(leftValue.getValue()) +" y " + str(rightValue.getValue()), 'Global', self.fila, self.columna)
        return Symbol("",0,typeExpression.INTEGER,0,0) 
