from Enum.typeExpression import typeExpression
from Environment.Environment import Environment
from Environment.Symbol import Symbol
from Abstract.Expression import Expression
from Enum.nativeFunction import nativeFunction
from Expression.Array import Array
from Expression.Primitive import Primitive

class ArrayAccess(Expression):
    def __init__(self, id: str, indexArray, fila, columna) -> None:
        self.id = id
        self.indexArray = indexArray
        self.fila = fila
        self.columna = columna
    
    def execute(self, environment: Environment) -> Symbol:
        List = environment.getVariable(self.id)
        todosInt = True
        if(List.getType() == typeExpression.ARRAY or List.getType() == typeExpression.VECTOR):
            #print(self.indexArray)
            #print( self.indexArray)
            """ for index in self.indexArray:
                if(index.execute(environment).getType() == typeExpression.INTEGER or index.execute(environment).getType() == typeExpression.USIZE):
                    todosInt = True
                else:
                    todosInt = False
                    break  """ 
            if(len(self.indexArray) == 1):
                tempIndex = self.indexArray[0].execute(environment)
                aux=str(tempIndex.getValue())
                for temp in Environment.getTemporales():
                    if len(temp) == 5:
                        if str(tempIndex.getValue()) == str(temp[4]):
                            aux = temp[0]
                            change = True
                Environment.saveExpression("if("+aux+" < 0) goto L"+str(Environment.getEtiqueta())+";")
                Environment.saveExpression("if("+aux+" > "+str(len(List.getValue())-1)+") goto L"+str(Environment.getEtiqueta())+";")
                Environment.saveExpression("goto L"+str(Environment.getEtiqueta()+1)+";")
                Environment.saveExpression("L"+str(Environment.getEtiqueta())+":")
                Environment.aumentarContadorL()
                Environment.saveExpression("printf(\"%c\", 66);")
                Environment.saveExpression("printf(\"%c\", 111);")
                Environment.saveExpression("printf(\"%c\", 117);")
                Environment.saveExpression("printf(\"%c\", 110);")
                Environment.saveExpression("printf(\"%c\", 100);")
                Environment.saveExpression("printf(\"%c\", 115);")
                Environment.saveExpression("printf(\"%c\", 69);")
                Environment.saveExpression("printf(\"%c\", 114);")
                Environment.saveExpression("printf(\"%c\", 114);")
                Environment.saveExpression("printf(\"%c\", 111);")
                Environment.saveExpression("printf(\"%c\", 114);")
                Environment.saveExpression("goto L"+str(Environment.getEtiqueta()+1)+";")
                Environment.saveExpression("L"+str(Environment.getEtiqueta())+":")
                Environment.aumentarContadorL()
                if(todosInt):
                    try:
                        #Environment.saveTemporal(tempIndex.getValue(),"","",tempIndex.getValue())
                        return List.getValue()[tempIndex.getValue()]
                    except:
                        #ruta = "Salida.txt"
                        #archivo = open(ruta, "a")
                        #archivo.write("Error: Index fuera del rango del arreglo\n")
                        #archivo.close()
                        #archivo = open("Errores/Errores.txt", "a")
                        #archivo.write("Error: Index fuera del rango del arreglo\n")
                        #archivo.close()
                        #return Symbol('',0,typeExpression.INTEGER,0,0)
                        Environment.saveError("Error: Index fuera del rango del arreglo", 'Local', self.fila, self.columna)
                else:
                    archivo = open("Salida.txt", "a")
                    archivo.write("Error: El indice debe ser un integer\n")
                    archivo.close()
                    Environment.saveError("Error: El indice debe ser un integer", 'Local', self.fila, self.columna)
            elif(len(self.indexArray) == 2):
                tempIndex = self.indexArray[0].execute(environment)
                aux=str(tempIndex.getValue())
                for temp in Environment.getTemporales():
                    if len(temp) == 5:
                        if str(tempIndex.getValue()) == str(temp[4]):
                            aux = temp[0]
                            change = True
                Environment.saveExpression("if("+aux+" < 0) goto L"+str(Environment.getEtiqueta())+";")
                Environment.saveExpression("if("+aux+" > "+str(len(List.getValue())-1)+") goto L"+str(Environment.getEtiqueta())+";")
                Environment.saveExpression("goto L"+str(Environment.getEtiqueta()+1)+";")
                Environment.saveExpression("L"+str(Environment.getEtiqueta())+":")
                Environment.aumentarContadorL()
                Environment.saveExpression("printf(\"%c\", 66);")
                Environment.saveExpression("printf(\"%c\", 111);")
                Environment.saveExpression("printf(\"%c\", 117);")
                Environment.saveExpression("printf(\"%c\", 110);")
                Environment.saveExpression("printf(\"%c\", 100);")
                Environment.saveExpression("printf(\"%c\", 115);")
                Environment.saveExpression("printf(\"%c\", 69);")
                Environment.saveExpression("printf(\"%c\", 114);")
                Environment.saveExpression("printf(\"%c\", 114);")
                Environment.saveExpression("printf(\"%c\", 111);")
                Environment.saveExpression("printf(\"%c\", 114);")
                Environment.saveExpression("goto L"+str(Environment.getEtiqueta()+3)+";")
                Environment.saveExpression("L"+str(Environment.getEtiqueta())+":")
                Environment.aumentarContadorL()
                tempIndex2 = self.indexArray[1].execute(environment)
                aux=str(tempIndex2.getValue())
                for temp in Environment.getTemporales():
                    if len(temp) == 5:
                        if str(tempIndex2.getValue()) == str(temp[4]):
                            aux = temp[0]
                            change = True
                Environment.saveExpression("if("+aux+" < 0) goto L"+str(Environment.getEtiqueta())+";")
                Environment.saveExpression("if("+aux+" > "+str(len(List.getValue()[tempIndex.getValue()].getValue())-1)+") goto L"+str(Environment.getEtiqueta())+";")
                Environment.saveExpression("goto L"+str(Environment.getEtiqueta()+1)+";")
                Environment.saveExpression("L"+str(Environment.getEtiqueta())+":")
                Environment.aumentarContadorL()
                Environment.saveExpression("printf(\"%c\", 66);")
                Environment.saveExpression("printf(\"%c\", 111);")
                Environment.saveExpression("printf(\"%c\", 117);")
                Environment.saveExpression("printf(\"%c\", 110);")
                Environment.saveExpression("printf(\"%c\", 100);")
                Environment.saveExpression("printf(\"%c\", 115);")
                Environment.saveExpression("printf(\"%c\", 69);")
                Environment.saveExpression("printf(\"%c\", 114);")
                Environment.saveExpression("printf(\"%c\", 114);")
                Environment.saveExpression("printf(\"%c\", 111);")
                Environment.saveExpression("printf(\"%c\", 114);")
                Environment.saveExpression("goto L"+str(Environment.getEtiqueta()+1)+";")
                Environment.saveExpression("L"+str(Environment.getEtiqueta())+":")
                Environment.aumentarContadorL()
                if(todosInt):
                    UsedList = List.getValue()[tempIndex.getValue()]
                    if(UsedList.getType() == typeExpression.ARRAY or UsedList.getType() == typeExpression.VECTOR):
                        try:
                            return UsedList.getValue()[tempIndex2.getValue()]
                        except:
                            #ruta = "Salida.txt"
                            #archivo = open(ruta, "a")
                            #archivo.write("Error: Index fuera del rango del arreglo\n")
                            #archivo.close()
                            #archivo = open("Errores/Errores.txt", "a")
                            #archivo.write("Error: Index fuera del rango del arreglo\n")
                            #archivo.close()
                            #return Symbol('',0,typeExpression.INTEGER,0,0)
                            Environment.saveError("Error: Index fuera del rango del arreglo", 'Local', self.fila, self.columna)
                    else:
                        archivo = open("Salida.txt", "a")
                        archivo.write("Error: Solo se puede ingresar a un array o vector\n")
                        archivo.close()
                        Environment.saveError("Error: Solo se puede ingresar a un array o vector", 'Local', self.fila, self.columna)
                else:
                    archivo = open("Salida.txt", "a")
                    archivo.write("Error: Los indices deben ser integer\n")
                    archivo.close()
                    Environment.saveError("Error: Los indices deben ser integer", 'Local', self.fila, self.columna)
            elif (len(self.indexArray) == 3):
                tempIndex = self.indexArray[0].execute(environment)
                aux=str(tempIndex.getValue())
                for temp in Environment.getTemporales():
                    if len(temp) == 5:
                        if str(tempIndex.getValue()) == str(temp[4]):
                            aux = temp[0]
                            change = True
                Environment.saveExpression("if("+aux+" < 0) goto L"+str(Environment.getEtiqueta())+";")
                Environment.saveExpression("if("+aux+" > "+str(len(List.getValue())-1)+") goto L"+str(Environment.getEtiqueta())+";")
                Environment.saveExpression("goto L"+str(Environment.getEtiqueta()+1)+";")
                Environment.saveExpression("L"+str(Environment.getEtiqueta())+":")
                Environment.aumentarContadorL()
                Environment.saveExpression("printf(\"%c\", 66);")
                Environment.saveExpression("printf(\"%c\", 111);")
                Environment.saveExpression("printf(\"%c\", 117);")
                Environment.saveExpression("printf(\"%c\", 110);")
                Environment.saveExpression("printf(\"%c\", 100);")
                Environment.saveExpression("printf(\"%c\", 115);")
                Environment.saveExpression("printf(\"%c\", 69);")
                Environment.saveExpression("printf(\"%c\", 114);")
                Environment.saveExpression("printf(\"%c\", 114);")
                Environment.saveExpression("printf(\"%c\", 111);")
                Environment.saveExpression("printf(\"%c\", 114);")
                Environment.saveExpression("goto L"+str(Environment.getEtiqueta()+5)+";")
                Environment.saveExpression("L"+str(Environment.getEtiqueta())+":")
                Environment.aumentarContadorL()
                tempIndex2 = self.indexArray[1].execute(environment)
                aux=str(tempIndex2.getValue())
                for temp in Environment.getTemporales():
                    if len(temp) == 5:
                        if str(tempIndex2.getValue()) == str(temp[4]):
                            aux = temp[0]
                            change = True
                Environment.saveExpression("if("+aux+" < 0) goto L"+str(Environment.getEtiqueta())+";")
                Environment.saveExpression("if("+aux+" > "+str(len(List.getValue()[tempIndex.getValue()].getValue())-1)+") goto L"+str(Environment.getEtiqueta())+";")
                Environment.saveExpression("goto L"+str(Environment.getEtiqueta()+1)+";")
                Environment.saveExpression("L"+str(Environment.getEtiqueta())+":")
                Environment.aumentarContadorL()
                Environment.saveExpression("printf(\"%c\", 66);")
                Environment.saveExpression("printf(\"%c\", 111);")
                Environment.saveExpression("printf(\"%c\", 117);")
                Environment.saveExpression("printf(\"%c\", 110);")
                Environment.saveExpression("printf(\"%c\", 100);")
                Environment.saveExpression("printf(\"%c\", 115);")
                Environment.saveExpression("printf(\"%c\", 69);")
                Environment.saveExpression("printf(\"%c\", 114);")
                Environment.saveExpression("printf(\"%c\", 114);")
                Environment.saveExpression("printf(\"%c\", 111);")
                Environment.saveExpression("printf(\"%c\", 114);")
                Environment.saveExpression("goto L"+str(Environment.getEtiqueta()+3)+";")
                Environment.saveExpression("L"+str(Environment.getEtiqueta())+":")
                Environment.aumentarContadorL()
                tempIndex3 = self.indexArray[2].execute(environment)
                aux=str(tempIndex3.getValue())
                for temp in Environment.getTemporales():
                    if len(temp) == 5:
                        if str(tempIndex3.getValue()) == str(temp[4]):
                            aux = temp[0]
                            change = True
                Environment.saveExpression("if("+aux+" < 0) goto L"+str(Environment.getEtiqueta())+";")
                Environment.saveExpression("if("+aux+" > "+str(len(List.getValue()[tempIndex.getValue()].getValue()[tempIndex2.getValue()].getValue())-1)+") goto L"+str(Environment.getEtiqueta())+";")
                Environment.saveExpression("goto L"+str(Environment.getEtiqueta()+1)+";")
                Environment.saveExpression("L"+str(Environment.getEtiqueta())+":")
                Environment.aumentarContadorL()
                Environment.saveExpression("printf(\"%c\", 66);")
                Environment.saveExpression("printf(\"%c\", 111);")
                Environment.saveExpression("printf(\"%c\", 117);")
                Environment.saveExpression("printf(\"%c\", 110);")
                Environment.saveExpression("printf(\"%c\", 100);")
                Environment.saveExpression("printf(\"%c\", 115);")
                Environment.saveExpression("printf(\"%c\", 69);")
                Environment.saveExpression("printf(\"%c\", 114);")
                Environment.saveExpression("printf(\"%c\", 114);")
                Environment.saveExpression("printf(\"%c\", 111);")
                Environment.saveExpression("printf(\"%c\", 114);")
                Environment.saveExpression("goto L"+str(Environment.getEtiqueta()+1)+";")
                Environment.saveExpression("L"+str(Environment.getEtiqueta())+":")
                Environment.aumentarContadorL()
                if(todosInt):
                    UsedList = List.getValue()[tempIndex.getValue()].getValue()[tempIndex2.getValue()]
                    if(UsedList.getType() == typeExpression.ARRAY or UsedList.getType() == typeExpression.VECTOR):
                        try:
                            return UsedList.getValue()[tempIndex3.getValue()]
                        except:
                            #ruta = "Salida.txt"
                            #archivo = open(ruta, "a")
                            #archivo.write("Error: Index fuera del rango del arreglo\n")
                            #archivo.close()
                            #archivo = open("Errores/Errores.txt", "a")
                            #archivo.write("Error: Index fuera del rango del arreglo\n")
                            #archivo.close()
                            #return Symbol('',0,typeExpression.INTEGER,0,0)
                            Environment.saveError("Error: Index fuera del rango del arreglo", 'Local', self.fila, self.columna)
                    else:
                        archivo = open("Salida.txt", "a")
                        archivo.write("Error: Solo se puede ingresar a un array o vector\n")
                        archivo.close()
                        Environment.saveError("Error: Solo se puede ingresar a un array o vector", 'Local', self.fila, self.columna)
                else:
                    archivo = open("Salida.txt", "a")
                    archivo.write("Error: Los indices deben ser integer\n")
                    archivo.close()
                    Environment.saveError("Error: Los indices deben ser integer", 'Local', self.fila, self.columna)
            elif(len(self.indexArray) == 4):
                tempIndex = self.indexArray[0].execute(environment)
                aux=str(tempIndex.getValue())
                for temp in Environment.getTemporales():
                    if len(temp) == 5:
                        if str(tempIndex.getValue()) == str(temp[4]):
                            aux = temp[0]
                            change = True
                Environment.saveExpression("if("+aux+" < 0) goto L"+str(Environment.getEtiqueta())+";")
                Environment.saveExpression("if("+aux+" > "+str(len(List.getValue())-1)+") goto L"+str(Environment.getEtiqueta())+";")
                Environment.saveExpression("goto L"+str(Environment.getEtiqueta()+1)+";")
                Environment.saveExpression("L"+str(Environment.getEtiqueta())+":")
                Environment.aumentarContadorL()
                Environment.saveExpression("printf(\"%c\", 66);")
                Environment.saveExpression("printf(\"%c\", 111);")
                Environment.saveExpression("printf(\"%c\", 117);")
                Environment.saveExpression("printf(\"%c\", 110);")
                Environment.saveExpression("printf(\"%c\", 100);")
                Environment.saveExpression("printf(\"%c\", 115);")
                Environment.saveExpression("printf(\"%c\", 69);")
                Environment.saveExpression("printf(\"%c\", 114);")
                Environment.saveExpression("printf(\"%c\", 114);")
                Environment.saveExpression("printf(\"%c\", 111);")
                Environment.saveExpression("printf(\"%c\", 114);")
                Environment.saveExpression("goto L"+str(Environment.getEtiqueta()+7)+";")
                Environment.saveExpression("L"+str(Environment.getEtiqueta())+":")
                Environment.aumentarContadorL()
                tempIndex2 = self.indexArray[1].execute(environment)
                aux=str(tempIndex2.getValue())
                for temp in Environment.getTemporales():
                    if len(temp) == 5:
                        if str(tempIndex2.getValue()) == str(temp[4]):
                            aux = temp[0]
                            change = True
                Environment.saveExpression("if("+aux+" < 0) goto L"+str(Environment.getEtiqueta())+";")
                Environment.saveExpression("if("+aux+" > "+str(len(List.getValue()[tempIndex.getValue()].getValue())-1)+") goto L"+str(Environment.getEtiqueta())+";")
                Environment.saveExpression("goto L"+str(Environment.getEtiqueta()+1)+";")
                Environment.saveExpression("L"+str(Environment.getEtiqueta())+":")
                Environment.aumentarContadorL()
                Environment.saveExpression("printf(\"%c\", 66);")
                Environment.saveExpression("printf(\"%c\", 111);")
                Environment.saveExpression("printf(\"%c\", 117);")
                Environment.saveExpression("printf(\"%c\", 110);")
                Environment.saveExpression("printf(\"%c\", 100);")
                Environment.saveExpression("printf(\"%c\", 115);")
                Environment.saveExpression("printf(\"%c\", 69);")
                Environment.saveExpression("printf(\"%c\", 114);")
                Environment.saveExpression("printf(\"%c\", 114);")
                Environment.saveExpression("printf(\"%c\", 111);")
                Environment.saveExpression("printf(\"%c\", 114);")
                Environment.saveExpression("goto L"+str(Environment.getEtiqueta()+5)+";")
                Environment.saveExpression("L"+str(Environment.getEtiqueta())+":")
                Environment.aumentarContadorL()
                tempIndex3 = self.indexArray[2].execute(environment)
                aux=str(tempIndex3.getValue())
                for temp in Environment.getTemporales():
                    if len(temp) == 5:
                        if str(tempIndex3.getValue()) == str(temp[4]):
                            aux = temp[0]
                            change = True
                Environment.saveExpression("if("+aux+" < 0) goto L"+str(Environment.getEtiqueta())+";")
                Environment.saveExpression("if("+aux+" > "+str(len(List.getValue()[tempIndex.getValue()].getValue()[tempIndex2.getValue()].getValue())-1)+") goto L"+str(Environment.getEtiqueta())+";")
                Environment.saveExpression("goto L"+str(Environment.getEtiqueta()+1)+";")
                Environment.saveExpression("L"+str(Environment.getEtiqueta())+":")
                Environment.aumentarContadorL()
                Environment.saveExpression("printf(\"%c\", 66);")
                Environment.saveExpression("printf(\"%c\", 111);")
                Environment.saveExpression("printf(\"%c\", 117);")
                Environment.saveExpression("printf(\"%c\", 110);")
                Environment.saveExpression("printf(\"%c\", 100);")
                Environment.saveExpression("printf(\"%c\", 115);")
                Environment.saveExpression("printf(\"%c\", 69);")
                Environment.saveExpression("printf(\"%c\", 114);")
                Environment.saveExpression("printf(\"%c\", 114);")
                Environment.saveExpression("printf(\"%c\", 111);")
                Environment.saveExpression("printf(\"%c\", 114);")
                Environment.saveExpression("goto L"+str(Environment.getEtiqueta()+3)+";")
                Environment.saveExpression("L"+str(Environment.getEtiqueta())+":")
                Environment.aumentarContadorL()
                tempIndex4 = self.indexArray[3].execute(environment)
                aux=str(tempIndex4.getValue())
                for temp in Environment.getTemporales():
                    if len(temp) == 5:
                        if str(tempIndex4.getValue()) == str(temp[4]):
                            aux = temp[0]
                            change = True
                Environment.saveExpression("if("+aux+" < 0) goto L"+str(Environment.getEtiqueta())+";")
                Environment.saveExpression("if("+aux+" > "+str(len(List.getValue()[tempIndex.getValue()].getValue()[tempIndex2.getValue()].getValue()[tempIndex3.getValue()].getValue())-1)+") goto L"+str(Environment.getEtiqueta())+";")
                Environment.saveExpression("goto L"+str(Environment.getEtiqueta()+1)+";")
                Environment.saveExpression("L"+str(Environment.getEtiqueta())+":")
                Environment.aumentarContadorL()
                Environment.saveExpression("printf(\"%c\", 66);")
                Environment.saveExpression("printf(\"%c\", 111);")
                Environment.saveExpression("printf(\"%c\", 117);")
                Environment.saveExpression("printf(\"%c\", 110);")
                Environment.saveExpression("printf(\"%c\", 100);")
                Environment.saveExpression("printf(\"%c\", 115);")
                Environment.saveExpression("printf(\"%c\", 69);")
                Environment.saveExpression("printf(\"%c\", 114);")
                Environment.saveExpression("printf(\"%c\", 114);")
                Environment.saveExpression("printf(\"%c\", 111);")
                Environment.saveExpression("printf(\"%c\", 114);")
                Environment.saveExpression("goto L"+str(Environment.getEtiqueta()+1)+";")
                Environment.saveExpression("L"+str(Environment.getEtiqueta())+":")
                Environment.aumentarContadorL()
                if(todosInt):
                    UsedList = List.getValue()[tempIndex.getValue()].getValue()[tempIndex2.getValue()].getValue()[tempIndex3.getValue()]
                    if(UsedList.getType() == typeExpression.ARRAY or UsedList.getType() == typeExpression.VECTOR):
                        try:
                            return UsedList.getValue()[tempIndex4.getValue()]
                        except:
                            #ruta = "Salida.txt"
                            #archivo = open(ruta, "a")
                            #archivo.write("Error: Index fuera del rango del arreglo\n")
                            #archivo.close()
                            #archivo = open("Errores/Errores.txt", "a")
                            #archivo.write("Error: Index fuera del rango del arreglo\n")
                            #archivo.close()
                            #return Symbol('',0,typeExpression.INTEGER,0,0)
                            Environment.saveError("Error: Index fuera del rango del arreglo", 'Local', self.fila, self.columna)
                    else:
                        archivo = open("Salida.txt", "a")
                        archivo.write("Error: Solo se puede ingresar a un array o vector\n")
                        archivo.close()
                        Environment.saveError("Error: Solo se puede ingresar a un array o vector", 'Local', self.fila, self.columna)
                else:
                    archivo = open("Salida.txt", "a")
                    archivo.write("Error: Los indices deben ser integer\n")
                    archivo.close()
                    Environment.saveError("Error: Los indices deben ser integer", 'Local', self.fila, self.columna)
            elif(len(self.indexArray) == 5):
                tempIndex = self.indexArray[0].execute(environment)
                aux=str(tempIndex.getValue())
                for temp in Environment.getTemporales():
                    if len(temp) == 5:
                        if str(tempIndex.getValue()) == str(temp[4]):
                            aux = temp[0]
                            change = True
                Environment.saveExpression("if("+aux+" < 0) goto L"+str(Environment.getEtiqueta())+";")
                Environment.saveExpression("if("+aux+" > "+str(len(List.getValue())-1)+") goto L"+str(Environment.getEtiqueta())+";")
                Environment.saveExpression("goto L"+str(Environment.getEtiqueta()+1)+";")
                Environment.saveExpression("L"+str(Environment.getEtiqueta())+":")
                Environment.aumentarContadorL()
                Environment.saveExpression("printf(\"%c\", 66);")
                Environment.saveExpression("printf(\"%c\", 111);")
                Environment.saveExpression("printf(\"%c\", 117);")
                Environment.saveExpression("printf(\"%c\", 110);")
                Environment.saveExpression("printf(\"%c\", 100);")
                Environment.saveExpression("printf(\"%c\", 115);")
                Environment.saveExpression("printf(\"%c\", 69);")
                Environment.saveExpression("printf(\"%c\", 114);")
                Environment.saveExpression("printf(\"%c\", 114);")
                Environment.saveExpression("printf(\"%c\", 111);")
                Environment.saveExpression("printf(\"%c\", 114);")
                Environment.saveExpression("goto L"+str(Environment.getEtiqueta()+9)+";")
                Environment.saveExpression("L"+str(Environment.getEtiqueta())+":")
                Environment.aumentarContadorL()
                tempIndex2 = self.indexArray[1].execute(environment)
                aux=str(tempIndex2.getValue())
                for temp in Environment.getTemporales():
                    if len(temp) == 5:
                        if str(tempIndex2.getValue()) == str(temp[4]):
                            aux = temp[0]
                            change = True
                Environment.saveExpression("if("+aux+" < 0) goto L"+str(Environment.getEtiqueta())+";")
                Environment.saveExpression("if("+aux+" > "+str(len(List.getValue()[tempIndex.getValue()].getValue())-1)+") goto L"+str(Environment.getEtiqueta())+";")
                Environment.saveExpression("goto L"+str(Environment.getEtiqueta()+1)+";")
                Environment.saveExpression("L"+str(Environment.getEtiqueta())+":")
                Environment.aumentarContadorL()
                Environment.saveExpression("printf(\"%c\", 66);")
                Environment.saveExpression("printf(\"%c\", 111);")
                Environment.saveExpression("printf(\"%c\", 117);")
                Environment.saveExpression("printf(\"%c\", 110);")
                Environment.saveExpression("printf(\"%c\", 100);")
                Environment.saveExpression("printf(\"%c\", 115);")
                Environment.saveExpression("printf(\"%c\", 69);")
                Environment.saveExpression("printf(\"%c\", 114);")
                Environment.saveExpression("printf(\"%c\", 114);")
                Environment.saveExpression("printf(\"%c\", 111);")
                Environment.saveExpression("printf(\"%c\", 114);")
                Environment.saveExpression("goto L"+str(Environment.getEtiqueta()+7)+";")
                Environment.saveExpression("L"+str(Environment.getEtiqueta())+":")
                Environment.aumentarContadorL()
                tempIndex3 = self.indexArray[2].execute(environment)
                aux=str(tempIndex3.getValue())
                for temp in Environment.getTemporales():
                    if len(temp) == 5:
                        if str(tempIndex3.getValue()) == str(temp[4]):
                            aux = temp[0]
                            change = True
                Environment.saveExpression("if("+aux+" < 0) goto L"+str(Environment.getEtiqueta())+";")
                Environment.saveExpression("if("+aux+" > "+str(len(List.getValue()[tempIndex.getValue()].getValue()[tempIndex2.getValue()].getValue())-1)+") goto L"+str(Environment.getEtiqueta())+";")
                Environment.saveExpression("goto L"+str(Environment.getEtiqueta()+1)+";")
                Environment.saveExpression("L"+str(Environment.getEtiqueta())+":")
                Environment.aumentarContadorL()
                Environment.saveExpression("printf(\"%c\", 66);")
                Environment.saveExpression("printf(\"%c\", 111);")
                Environment.saveExpression("printf(\"%c\", 117);")
                Environment.saveExpression("printf(\"%c\", 110);")
                Environment.saveExpression("printf(\"%c\", 100);")
                Environment.saveExpression("printf(\"%c\", 115);")
                Environment.saveExpression("printf(\"%c\", 69);")
                Environment.saveExpression("printf(\"%c\", 114);")
                Environment.saveExpression("printf(\"%c\", 114);")
                Environment.saveExpression("printf(\"%c\", 111);")
                Environment.saveExpression("printf(\"%c\", 114);")
                Environment.saveExpression("goto L"+str(Environment.getEtiqueta()+5)+";")
                Environment.saveExpression("L"+str(Environment.getEtiqueta())+":")
                Environment.aumentarContadorL()
                tempIndex4 = self.indexArray[3].execute(environment)
                aux=str(tempIndex4.getValue())
                for temp in Environment.getTemporales():
                    if len(temp) == 5:
                        if str(tempIndex4.getValue()) == str(temp[4]):
                            aux = temp[0]
                            change = True
                Environment.saveExpression("if("+aux+" < 0) goto L"+str(Environment.getEtiqueta())+";")
                Environment.saveExpression("if("+aux+" > "+str(len(List.getValue()[tempIndex.getValue()].getValue()[tempIndex2.getValue()].getValue()[tempIndex3.getValue()].getValue())-1)+") goto L"+str(Environment.getEtiqueta())+";")
                Environment.saveExpression("goto L"+str(Environment.getEtiqueta()+1)+";")
                Environment.saveExpression("L"+str(Environment.getEtiqueta())+":")
                Environment.aumentarContadorL()
                Environment.saveExpression("printf(\"%c\", 66);")
                Environment.saveExpression("printf(\"%c\", 111);")
                Environment.saveExpression("printf(\"%c\", 117);")
                Environment.saveExpression("printf(\"%c\", 110);")
                Environment.saveExpression("printf(\"%c\", 100);")
                Environment.saveExpression("printf(\"%c\", 115);")
                Environment.saveExpression("printf(\"%c\", 69);")
                Environment.saveExpression("printf(\"%c\", 114);")
                Environment.saveExpression("printf(\"%c\", 114);")
                Environment.saveExpression("printf(\"%c\", 111);")
                Environment.saveExpression("printf(\"%c\", 114);")
                Environment.saveExpression("goto L"+str(Environment.getEtiqueta()+3)+";")
                Environment.saveExpression("L"+str(Environment.getEtiqueta())+":")
                Environment.aumentarContadorL()
                tempIndex5 = self.indexArray[4].execute(environment)
                aux=str(tempIndex5.getValue())
                for temp in Environment.getTemporales():
                    if len(temp) == 5:
                        if str(tempIndex5.getValue()) == str(temp[4]):
                            aux = temp[0]
                            change = True
                Environment.saveExpression("if("+aux+" < 0) goto L"+str(Environment.getEtiqueta())+";")
                Environment.saveExpression("if("+aux+" > "+str(len(List.getValue()[tempIndex.getValue()].getValue()[tempIndex2.getValue()].getValue()[tempIndex3.getValue()].getValue()[tempIndex4.getValue()].getValue())-1)+") goto L"+str(Environment.getEtiqueta())+";")
                Environment.saveExpression("goto L"+str(Environment.getEtiqueta()+1)+";")
                Environment.saveExpression("L"+str(Environment.getEtiqueta())+":")
                Environment.aumentarContadorL()
                Environment.saveExpression("printf(\"%c\", 66);")
                Environment.saveExpression("printf(\"%c\", 111);")
                Environment.saveExpression("printf(\"%c\", 117);")
                Environment.saveExpression("printf(\"%c\", 110);")
                Environment.saveExpression("printf(\"%c\", 100);")
                Environment.saveExpression("printf(\"%c\", 115);")
                Environment.saveExpression("printf(\"%c\", 69);")
                Environment.saveExpression("printf(\"%c\", 114);")
                Environment.saveExpression("printf(\"%c\", 114);")
                Environment.saveExpression("printf(\"%c\", 111);")
                Environment.saveExpression("printf(\"%c\", 114);")
                Environment.saveExpression("goto L"+str(Environment.getEtiqueta()+1)+";")
                Environment.saveExpression("L"+str(Environment.getEtiqueta())+":")
                Environment.aumentarContadorL()
                if(todosInt):
                    UsedList = List.getValue()[tempIndex.getValue()].getValue()[tempIndex2.getValue()].getValue()[tempIndex3.getValue()].getValue()[tempIndex4.getValue()]
                    if(UsedList.getType() == typeExpression.ARRAY or UsedList.getType() == typeExpression.VECTOR):
                        try:
                            return UsedList.getValue()[tempIndex5.getValue()]
                        except:
                            #ruta = "Salida.txt"
                            #archivo = open(ruta, "a")
                            #archivo.write("Error: Index fuera del rango del arreglo\n")
                            #archivo.close()
                            #archivo = open("Errores/Errores.txt", "a")
                            #archivo.write("Error: Index fuera del rango del arreglo\n")
                            #archivo.close()
                            #return Symbol('',0,typeExpression.INTEGER,0,0)
                            Environment.saveError("Error: Index fuera del rango del arreglo", 'Local', self.fila, self.columna)
                    else:
                        archivo = open("Salida.txt", "a")
                        archivo.write("Error: Solo se puede ingresar a un array o vector\n")
                        archivo.close()
                        Environment.saveError("Error: Solo se puede ingresar a un array o vector", 'Local', self.fila, self.columna)
                else:
                    archivo = open("Salida.txt", "a")
                    archivo.write("Error: Los indices deben ser integer\n")
                    archivo.close()
                    Environment.saveError("Error: Los indices deben ser integer", 'Local', self.fila, self.columna)
            elif(len(self.indexArray) == 6):
                tempIndex = self.indexArray[0].execute(environment)
                tempIndex2 = self.indexArray[1].execute(environment)
                tempIndex3 = self.indexArray[2].execute(environment)
                tempIndex4 = self.indexArray[3].execute(environment)
                tempIndex5 = self.indexArray[4].execute(environment)
                tempIndex6 = self.indexArray[5].execute(environment)
                if(todosInt):
                    UsedList = List.getValue()[tempIndex.getValue()].getValue()[tempIndex2.getValue()].getValue()[tempIndex3.getValue()].getValue()[tempIndex4.getValue()].getValue()[tempIndex5.getValue()]
                    if(UsedList.getType() == typeExpression.ARRAY or UsedList.getType() == typeExpression.VECTOR):
                        try:
                            return UsedList.getValue()[tempIndex6.getValue()]
                        except:
                            ruta = "Salida.txt"
                            archivo = open(ruta, "a")
                            archivo.write("Error: Index fuera del rango del arreglo\n")
                            archivo.close()
                            #archivo = open("Errores/Errores.txt", "a")
                            #archivo.write("Error: Index fuera del rango del arreglo\n")
                            #archivo.close()
                            #return Symbol('',0,typeExpression.INTEGER,0,0)
                            Environment.saveError("Error: Index fuera del rango del arreglo", 'Local', self.fila, self.columna)
                    else:
                        archivo = open("Salida.txt", "a")
                        archivo.write("Error: Solo se puede ingresar a un array o vector\n")
                        archivo.close()
                        Environment.saveError("Error: Solo se puede ingresar a un array o vector", 'Local', self.fila, self.columna)
                else:
                    archivo = open("Salida.txt", "a")
                    archivo.write("Error: Los indices deben ser integer\n")
                    archivo.close()
                    Environment.saveError("Error: Los indices deben ser integer", 'Local', self.fila, self.columna)
            elif(len(self.indexArray) == 7):
                tempIndex = self.indexArray[0].execute(environment)
                tempIndex2 = self.indexArray[1].execute(environment)
                tempIndex3 = self.indexArray[2].execute(environment)
                tempIndex4 = self.indexArray[3].execute(environment)
                tempIndex5 = self.indexArray[4].execute(environment)
                tempIndex6 = self.indexArray[5].execute(environment)
                tempIndex7 = self.indexArray[6].execute(environment)
                if(todosInt):
                    UsedList = List.getValue()[tempIndex.getValue()].getValue()[tempIndex2.getValue()].getValue()[tempIndex3.getValue()].getValue()[tempIndex4.getValue()].getValue()[tempIndex5.getValue()].getValue()[tempIndex6.getValue()]
                    if(UsedList.getType() == typeExpression.ARRAY or UsedList.getType() == typeExpression.VECTOR):
                        try:
                            return UsedList.getValue()[tempIndex7.getValue()]
                        except:
                            ruta = "Salida.txt"
                            archivo = open(ruta, "a")
                            archivo.write("Error: Index fuera del rango del arreglo\n")
                            archivo.close()
                            #archivo = open("Errores/Errores.txt", "a")
                            #archivo.write("Error: Index fuera del rango del arreglo\n")
                            #archivo.close()
                            #return Symbol('',0,typeExpression.INTEGER,0,0)
                            Environment.saveError("Error: Index fuera del rango del arreglo", 'Local', self.fila, self.columna)
                    else:
                        archivo = open("Salida.txt", "a")
                        archivo.write("Error: Solo se puede ingresar a un array o vector\n")
                        archivo.close()
                        Environment.saveError("Error: Solo se puede ingresar a un array o vector", 'Local', self.fila, self.columna)
                else:
                    archivo = open("Salida.txt", "a")
                    archivo.write("Error: Los indices deben ser integer\n")
                    archivo.close()
                    Environment.saveError("Error: Los indices deben ser integer", 'Local', self.fila, self.columna)
            elif(len(self.indexArray) == 8):
                tempIndex = self.indexArray[0].execute(environment)
                tempIndex2 = self.indexArray[1].execute(environment)
                tempIndex3 = self.indexArray[2].execute(environment)
                tempIndex4 = self.indexArray[3].execute(environment)
                tempIndex5 = self.indexArray[4].execute(environment)
                tempIndex6 = self.indexArray[5].execute(environment)
                tempIndex7 = self.indexArray[6].execute(environment)
                tempIndex8 = self.indexArray[7].execute(environment)
                if(todosInt):
                    UsedList = List.getValue()[tempIndex.getValue()].getValue()[tempIndex2.getValue()].getValue()[tempIndex3.getValue()].getValue()[tempIndex4.getValue()].getValue()[tempIndex5.getValue()].getValue()[tempIndex6.getValue()].getValue()[tempIndex7.getValue()]
                    if(UsedList.getType() == typeExpression.ARRAY or UsedList.getType() == typeExpression.VECTOR):
                        try:
                            return UsedList.getValue()[tempIndex8.getValue()]
                        except:
                            ruta = "Salida.txt"
                            archivo = open(ruta, "a")
                            archivo.write("Error: Index fuera del rango del arreglo\n")
                            archivo.close()
                            #archivo = open("Errores/Errores.txt", "a")
                            #archivo.write("Error: Index fuera del rango del arreglo\n")
                            #archivo.close()
                            #return Symbol('',0,typeExpression.INTEGER,0,0)
                            Environment.saveError("Error: Index fuera del rango del arreglo", 'Local', self.fila, self.columna)
                    else:
                        archivo = open("Salida.txt", "a")
                        archivo.write("Error: Solo se puede ingresar a un array o vector\n")
                        archivo.close()
                        Environment.saveError("Error: Solo se puede ingresar a un array o vector", 'Local', self.fila, self.columna)
                else:
                    archivo = open("Salida.txt", "a")
                    archivo.write("Error: Los indices deben ser integer\n")
                    archivo.close()
                    Environment.saveError("Error: Los indices deben ser integer", 'Local', self.fila, self.columna)
            elif(len(self.indexArray) == 9):
                tempIndex = self.indexArray[0].execute(environment)
                tempIndex2 = self.indexArray[1].execute(environment)
                tempIndex3 = self.indexArray[2].execute(environment)
                tempIndex4 = self.indexArray[3].execute(environment)
                tempIndex5 = self.indexArray[4].execute(environment)
                tempIndex6 = self.indexArray[5].execute(environment)
                tempIndex7 = self.indexArray[6].execute(environment)
                tempIndex8 = self.indexArray[7].execute(environment)
                tempIndex9 = self.indexArray[8].execute(environment)
                if(todosInt):
                    UsedList = List.getValue()[tempIndex.getValue()].getValue()[tempIndex2.getValue()].getValue()[tempIndex3.getValue()].getValue()[tempIndex4.getValue()].getValue()[tempIndex5.getValue()].getValue()[tempIndex6.getValue()].getValue()[tempIndex7.getValue()].getValue()[tempIndex8.getValue()]
                    if(UsedList.getType() == typeExpression.ARRAY or UsedList.getType() == typeExpression.VECTOR):
                        try:
                            return UsedList.getValue()[tempIndex9.getValue()]
                        except:
                            ruta = "Salida.txt"
                            archivo = open(ruta, "a")
                            archivo.write("Error: Index fuera del rango del arreglo\n")
                            archivo.close()
                            #archivo = open("Errores/Errores.txt", "a")
                            #archivo.write("Error: Index fuera del rango del arreglo\n")
                            #archivo.close()
                            #return Symbol('',0,typeExpression.INTEGER,0,0)
                            Environment.saveError("Error: Index fuera del rango del arreglo", 'Local', self.fila, self.columna)
                    else:
                        archivo = open("Salida.txt", "a")
                        archivo.write("Error: Solo se puede ingresar a un array o vector\n")
                        archivo.close()
                        Environment.saveError("Error: Solo se puede ingresar a un array o vector", 'Local', self.fila, self.columna)
                else:
                    archivo = open("Salida.txt", "a")
                    archivo.write("Error: Los indices deben ser integer\n")
                    archivo.close()
                    Environment.saveError("Error: Los indices deben ser integer", 'Local', self.fila, self.columna)
            elif(len(self.indexArray) == 10):
                tempIndex = self.indexArray[0].execute(environment)
                tempIndex2 = self.indexArray[1].execute(environment)
                tempIndex3 = self.indexArray[2].execute(environment)
                tempIndex4 = self.indexArray[3].execute(environment)
                tempIndex5 = self.indexArray[4].execute(environment)
                tempIndex6 = self.indexArray[5].execute(environment)
                tempIndex7 = self.indexArray[6].execute(environment)
                tempIndex8 = self.indexArray[7].execute(environment)
                tempIndex9 = self.indexArray[8].execute(environment)
                tempIndex10 = self.indexArray[9].execute(environment)
                if(todosInt):
                    UsedList = List.getValue()[tempIndex.getValue()].getValue()[tempIndex2.getValue()].getValue()[tempIndex3.getValue()].getValue()[tempIndex4.getValue()].getValue()[tempIndex5.getValue()].getValue()[tempIndex6.getValue()].getValue()[tempIndex7.getValue()].getValue()[tempIndex8.getValue()].getValue()[tempIndex9.getValue()]
                    if(UsedList.getType() == typeExpression.ARRAY or UsedList.getType() == typeExpression.VECTOR):
                        try:
                            return UsedList.getValue()[tempIndex10.getValue()]
                        except:
                            ruta = "Salida.txt"
                            archivo = open(ruta, "a")
                            archivo.write("Error: Index fuera del rango del arreglo\n")
                            archivo.close()
                            #archivo = open("Errores/Errores.txt", "a")
                            #archivo.write("Error: Index fuera del rango del arreglo\n")
                            #archivo.close()
                            #return Symbol('',0,typeExpression.INTEGER,0,0)
                            Environment.saveError("Error: Index fuera del rango del arreglo", 'Local', self.fila, self.columna)
                    else:
                        archivo = open("Salida.txt", "a")
                        archivo.write("Error: Solo se puede ingresar a un array o vector\n")
                        archivo.close()
                        Environment.saveError("Error: Solo se puede ingresar a un array o vector", 'Local', self.fila, self.columna)
                else:
                    archivo = open("Salida.txt", "a")
                    archivo.write("Error: Los indices deben ser integer\n")
                    archivo.close()
                    Environment.saveError("Error: Los indices deben ser integer", 'Local', self.fila, self.columna)
            elif(len(self.indexArray) == 11):
                tempIndex = self.indexArray[0].execute(environment)
                tempIndex2 = self.indexArray[1].execute(environment)
                tempIndex3 = self.indexArray[2].execute(environment)
                tempIndex4 = self.indexArray[3].execute(environment)
                tempIndex5 = self.indexArray[4].execute(environment)
                tempIndex6 = self.indexArray[5].execute(environment)
                tempIndex7 = self.indexArray[6].execute(environment)
                tempIndex8 = self.indexArray[7].execute(environment)
                tempIndex9 = self.indexArray[8].execute(environment)
                tempIndex10 = self.indexArray[9].execute(environment)
                tempIndex11 = self.indexArray[10].execute(environment)
                if(todosInt):
                    UsedList = List.getValue()[tempIndex.getValue()].getValue()[tempIndex2.getValue()].getValue()[tempIndex3.getValue()].getValue()[tempIndex4.getValue()].getValue()[tempIndex5.getValue()].getValue()[tempIndex6.getValue()].getValue()[tempIndex7.getValue()].getValue()[tempIndex8.getValue()].getValue()[tempIndex9.getValue()].getValue()[tempIndex10.getValue()]
                    if(UsedList.getType() == typeExpression.ARRAY or UsedList.getType() == typeExpression.VECTOR):
                        try:
                            return UsedList.getValue()[tempIndex11.getValue()]
                        except:
                            ruta = "Salida.txt"
                            archivo = open(ruta, "a")
                            archivo.write("Error: Index fuera del rango del arreglo\n")
                            archivo.close()
                            #archivo = open("Errores/Errores.txt", "a")
                            #archivo.write("Error: Index fuera del rango del arreglo\n")
                            #archivo.close()
                            #return Symbol('',0,typeExpression.INTEGER,0,0)
                            Environment.saveError("Error: Index fuera del rango del arreglo", 'Local', self.fila, self.columna)
                    else:
                        archivo = open("Salida.txt", "a")
                        archivo.write("Error: Solo se puede ingresar a un array o vector\n")
                        archivo.close()
                        Environment.saveError("Error: Solo se puede ingresar a un array o vector", 'Local', self.fila, self.columna)
                else:
                    archivo = open("Salida.txt", "a")
                    archivo.write("Error: Los indices deben ser integer\n")
                    archivo.close()
                    Environment.saveError("Error: Los indices deben ser integer", 'Local', self.fila, self.columna)
            elif(len(self.indexArray) == 12):
                tempIndex = self.indexArray[0].execute(environment)
                tempIndex2 = self.indexArray[1].execute(environment)
                tempIndex3 = self.indexArray[2].execute(environment)
                tempIndex4 = self.indexArray[3].execute(environment)
                tempIndex5 = self.indexArray[4].execute(environment)
                tempIndex6 = self.indexArray[5].execute(environment)
                tempIndex7 = self.indexArray[6].execute(environment)
                tempIndex8 = self.indexArray[7].execute(environment)
                tempIndex9 = self.indexArray[8].execute(environment)
                tempIndex10 = self.indexArray[9].execute(environment)
                tempIndex11 = self.indexArray[10].execute(environment)
                tempIndex12 = self.indexArray[11].execute(environment)
                if(todosInt):
                    UsedList = List.getValue()[tempIndex.getValue()].getValue()[tempIndex2.getValue()].getValue()[tempIndex3.getValue()].getValue()[tempIndex4.getValue()].getValue()[tempIndex5.getValue()].getValue()[tempIndex6.getValue()].getValue()[tempIndex7.getValue()].getValue()[tempIndex8.getValue()].getValue()[tempIndex9.getValue()].getValue()[tempIndex10.getValue()].getValue()[tempIndex11.getValue()]
                    if(UsedList.getType() == typeExpression.ARRAY or UsedList.getType() == typeExpression.VECTOR):
                        try:
                            return UsedList.getValue()[tempIndex12.getValue()]
                        except:
                            ruta = "Salida.txt"
                            archivo = open(ruta, "a")
                            archivo.write("Error: Index fuera del rango del arreglo\n")
                            archivo.close()
                            #archivo = open("Errores/Errores.txt", "a")
                            #archivo.write("Error: Index fuera del rango del arreglo\n")
                            #archivo.close()
                            #return Symbol('',0,typeExpression.INTEGER,0,0)
                            Environment.saveError("Error: Index fuera del rango del arreglo", 'Local', self.fila, self.columna)
                    else:
                        archivo = open("Salida.txt", "a")
                        archivo.write("Error: Solo se puede ingresar a un array o vector\n")
                        archivo.close()
                        Environment.saveError("Error: Solo se puede ingresar a un array o vector", 'Local', self.fila, self.columna)
                else:
                    archivo = open("Salida.txt", "a")
                    archivo.write("Error: Los indices deben ser integer\n")
                    archivo.close()
                    Environment.saveError("Error: Los indices deben ser integer", 'Local', self.fila, self.columna)
            elif(len(self.indexArray) == 13):
                tempIndex = self.indexArray[0].execute(environment)
                tempIndex2 = self.indexArray[1].execute(environment)
                tempIndex3 = self.indexArray[2].execute(environment)
                tempIndex4 = self.indexArray[3].execute(environment)
                tempIndex5 = self.indexArray[4].execute(environment)
                tempIndex6 = self.indexArray[5].execute(environment)
                tempIndex7 = self.indexArray[6].execute(environment)
                tempIndex8 = self.indexArray[7].execute(environment)
                tempIndex9 = self.indexArray[8].execute(environment)
                tempIndex10 = self.indexArray[9].execute(environment)
                tempIndex11 = self.indexArray[10].execute(environment)
                tempIndex12 = self.indexArray[11].execute(environment)
                tempIndex13 = self.indexArray[12].execute(environment)
                if(todosInt):
                    UsedList = List.getValue()[tempIndex.getValue()].getValue()[tempIndex2.getValue()].getValue()[tempIndex3.getValue()].getValue()[tempIndex4.getValue()].getValue()[tempIndex5.getValue()].getValue()[tempIndex6.getValue()].getValue()[tempIndex7.getValue()].getValue()[tempIndex8.getValue()].getValue()[tempIndex9.getValue()].getValue()[tempIndex10.getValue()].getValue()[tempIndex11.getValue()].getValue()[tempIndex12.getValue()]
                    if(UsedList.getType() == typeExpression.ARRAY or UsedList.getType() == typeExpression.VECTOR):
                        try:
                            return UsedList.getValue()[tempIndex13.getValue()]
                        except:
                            ruta = "Salida.txt"
                            archivo = open(ruta, "a")
                            archivo.write("Error: Index fuera del rango del arreglo\n")
                            archivo.close()
                            #archivo = open("Errores/Errores.txt", "a")
                            #archivo.write("Error: Index fuera del rango del arreglo\n")
                            #archivo.close()
                            #return Symbol('',0,typeExpression.INTEGER,0,0)
                            Environment.saveError("Error: Index fuera del rango del arreglo", 'Local', self.fila, self.columna)
                    else:
                        archivo = open("Salida.txt", "a")
                        archivo.write("Error: Solo se puede ingresar a un array o vector\n")
                        archivo.close()
                        Environment.saveError("Error: Solo se puede ingresar a un array o vector", 'Local', self.fila, self.columna)
                else:
                    archivo = open("Salida.txt", "a")
                    archivo.write("Error: Los indices deben ser integer\n")
                    archivo.close()
                    Environment.saveError("Error: Los indices deben ser integer", 'Local', self.fila, self.columna)
            elif(len(self.indexArray) == 14):
                tempIndex = self.indexArray[0].execute(environment)
                tempIndex2 = self.indexArray[1].execute(environment)
                tempIndex3 = self.indexArray[2].execute(environment)
                tempIndex4 = self.indexArray[3].execute(environment)
                tempIndex5 = self.indexArray[4].execute(environment)
                tempIndex6 = self.indexArray[5].execute(environment)
                tempIndex7 = self.indexArray[6].execute(environment)
                tempIndex8 = self.indexArray[7].execute(environment)
                tempIndex9 = self.indexArray[8].execute(environment)
                tempIndex10 = self.indexArray[9].execute(environment)
                tempIndex11 = self.indexArray[10].execute(environment)
                tempIndex12 = self.indexArray[11].execute(environment)
                tempIndex13 = self.indexArray[12].execute(environment)
                tempIndex14 = self.indexArray[13].execute(environment)
                if(todosInt):
                    UsedList = List.getValue()[tempIndex.getValue()].getValue()[tempIndex2.getValue()].getValue()[tempIndex3.getValue()].getValue()[tempIndex4.getValue()].getValue()[tempIndex5.getValue()].getValue()[tempIndex6.getValue()].getValue()[tempIndex7.getValue()].getValue()[tempIndex8.getValue()].getValue()[tempIndex9.getValue()].getValue()[tempIndex10.getValue()].getValue()[tempIndex11.getValue()].getValue()[tempIndex12.getValue()].getValue()[tempIndex13.getValue()]
                    if(UsedList.getType() == typeExpression.ARRAY or UsedList.getType() == typeExpression.VECTOR):
                        try:
                            return UsedList.getValue()[tempIndex14.getValue()]
                        except:
                            ruta = "Salida.txt"
                            archivo = open(ruta, "a")
                            archivo.write("Error: Index fuera del rango del arreglo\n")
                            archivo.close()
                            #archivo = open("Errores/Errores.txt", "a")
                            #archivo.write("Error: Index fuera del rango del arreglo\n")
                            #archivo.close()
                            #return Symbol('',0,typeExpression.INTEGER,0,0)
                            Environment.saveError("Error: Index fuera del rango del arreglo", 'Local', self.fila, self.columna)
                    else:
                        archivo = open("Salida.txt", "a")
                        archivo.write("Error: Solo se puede ingresar a un array o vector\n")
                        archivo.close()
                        Environment.saveError("Error: Solo se puede ingresar a un array o vector", 'Local', self.fila, self.columna)
                else:
                    archivo = open("Salida.txt", "a")
                    archivo.write("Error: Los indices deben ser integer\n")
                    archivo.close()
                    Environment.saveError("Error: Los indices deben ser integer", 'Local', self.fila, self.columna)
            elif(len(self.indexArray) == 15):
                tempIndex = self.indexArray[0].execute(environment)
                tempIndex2 = self.indexArray[1].execute(environment)
                tempIndex3 = self.indexArray[2].execute(environment)
                tempIndex4 = self.indexArray[3].execute(environment)
                tempIndex5 = self.indexArray[4].execute(environment)
                tempIndex6 = self.indexArray[5].execute(environment)
                tempIndex7 = self.indexArray[6].execute(environment)
                tempIndex8 = self.indexArray[7].execute(environment)
                tempIndex9 = self.indexArray[8].execute(environment)
                tempIndex10 = self.indexArray[9].execute(environment)
                tempIndex11 = self.indexArray[10].execute(environment)
                tempIndex12 = self.indexArray[11].execute(environment)
                tempIndex13 = self.indexArray[12].execute(environment)
                tempIndex14 = self.indexArray[13].execute(environment)
                tempIndex15 = self.indexArray[14].execute(environment)
                if(todosInt):
                    UsedList = List.getValue()[tempIndex.getValue()].getValue()[tempIndex2.getValue()].getValue()[tempIndex3.getValue()].getValue()[tempIndex4.getValue()].getValue()[tempIndex5.getValue()].getValue()[tempIndex6.getValue()].getValue()[tempIndex7.getValue()].getValue()[tempIndex8.getValue()].getValue()[tempIndex9.getValue()].getValue()[tempIndex10.getValue()].getValue()[tempIndex11.getValue()].getValue()[tempIndex12.getValue()].getValue()[tempIndex13.getValue()].getValue()[tempIndex14.getValue()]
                    if(UsedList.getType() == typeExpression.ARRAY or UsedList.getType() == typeExpression.VECTOR):
                        try:
                            return UsedList.getValue()[tempIndex15.getValue()]
                        except:
                            ruta = "Salida.txt"
                            archivo = open(ruta, "a")
                            archivo.write("Error: Index fuera del rango del arreglo\n")
                            archivo.close()
                            #archivo = open("Errores/Errores.txt", "a")
                            #archivo.write("Error: Index fuera del rango del arreglo\n")
                            #archivo.close()
                            #return Symbol('',0,typeExpression.INTEGER,0,0)
                            Environment.saveError("Error: Index fuera del rango del arreglo", 'Local', self.fila, self.columna)
                    else:
                        archivo = open("Salida.txt", "a")
                        archivo.write("Error: Solo se puede ingresar a un array o vector\n")
                        archivo.close()
                        Environment.saveError("Error: Solo se puede ingresar a un array o vector", 'Local', self.fila, self.columna)
                else:
                    archivo = open("Salida.txt", "a")
                    archivo.write("Error: Los indices deben ser integer\n")
                    archivo.close()
                    Environment.saveError("Error: Los indices deben ser integer", 'Local', self.fila, self.columna)
            elif(len(self.indexArray) == 16):
                tempIndex = self.indexArray[0].execute(environment)
                tempIndex2 = self.indexArray[1].execute(environment)
                tempIndex3 = self.indexArray[2].execute(environment)
                tempIndex4 = self.indexArray[3].execute(environment)
                tempIndex5 = self.indexArray[4].execute(environment)
                tempIndex6 = self.indexArray[5].execute(environment)
                tempIndex7 = self.indexArray[6].execute(environment)
                tempIndex8 = self.indexArray[7].execute(environment)
                tempIndex9 = self.indexArray[8].execute(environment)
                tempIndex10 = self.indexArray[9].execute(environment)
                tempIndex11 = self.indexArray[10].execute(environment)
                tempIndex12 = self.indexArray[11].execute(environment)
                tempIndex13 = self.indexArray[12].execute(environment)
                tempIndex14 = self.indexArray[13].execute(environment)
                tempIndex15 = self.indexArray[14].execute(environment)
                tempIndex16 = self.indexArray[15].execute(environment)
                if(todosInt):
                    UsedList = List.getValue()[tempIndex.getValue()].getValue()[tempIndex2.getValue()].getValue()[tempIndex3.getValue()].getValue()[tempIndex4.getValue()].getValue()[tempIndex5.getValue()].getValue()[tempIndex6.getValue()].getValue()[tempIndex7.getValue()].getValue()[tempIndex8.getValue()].getValue()[tempIndex9.getValue()].getValue()[tempIndex10.getValue()].getValue()[tempIndex11.getValue()].getValue()[tempIndex12.getValue()].getValue()[tempIndex13.getValue()].getValue()[tempIndex14.getValue()].getValue()[tempIndex15.getValue()]
                    if(UsedList.getType() == typeExpression.ARRAY or UsedList.getType() == typeExpression.VECTOR):
                        try:
                            return UsedList.getValue()[tempIndex16.getValue()]
                        except:
                            ruta = "Salida.txt"
                            archivo = open(ruta, "a")
                            archivo.write("Error: Index fuera del rango del arreglo\n")
                            archivo.close()
                            #archivo = open("Errores/Errores.txt", "a")
                            #archivo.write("Error: Index fuera del rango del arreglo\n")
                            #archivo.close()
                            #return Symbol('',0,typeExpression.INTEGER,0,0)
                            Environment.saveError("Error: Index fuera del rango del arreglo", 'Local', self.fila, self.columna)
                    else:
                        archivo = open("Salida.txt", "a")
                        archivo.write("Error: Solo se puede ingresar a un array o vector\n")
                        archivo.close()
                        Environment.saveError("Error: Solo se puede ingresar a un array o vector", 'Local', self.fila, self.columna)
                else:
                    archivo = open("Salida.txt", "a")
                    archivo.write("Error: Los indices deben ser integer\n")
                    archivo.close()
                    Environment.saveError("Error: Los indices deben ser integer", 'Local', self.fila, self.columna)
            elif(len(self.indexArray) == 17):
                tempIndex = self.indexArray[0].execute(environment)
                tempIndex2 = self.indexArray[1].execute(environment)
                tempIndex3 = self.indexArray[2].execute(environment)
                tempIndex4 = self.indexArray[3].execute(environment)
                tempIndex5 = self.indexArray[4].execute(environment)
                tempIndex6 = self.indexArray[5].execute(environment)
                tempIndex7 = self.indexArray[6].execute(environment)
                tempIndex8 = self.indexArray[7].execute(environment)
                tempIndex9 = self.indexArray[8].execute(environment)
                tempIndex10 = self.indexArray[9].execute(environment)
                tempIndex11 = self.indexArray[10].execute(environment)
                tempIndex12 = self.indexArray[11].execute(environment)
                tempIndex13 = self.indexArray[12].execute(environment)
                tempIndex14 = self.indexArray[13].execute(environment)
                tempIndex15 = self.indexArray[14].execute(environment)
                tempIndex16 = self.indexArray[15].execute(environment)
                tempIndex17 = self.indexArray[16].execute(environment)
                if(todosInt):
                    UsedList = List.getValue()[tempIndex.getValue()].getValue()[tempIndex2.getValue()].getValue()[tempIndex3.getValue()].getValue()[tempIndex4.getValue()].getValue()[tempIndex5.getValue()].getValue()[tempIndex6.getValue()].getValue()[tempIndex7.getValue()].getValue()[tempIndex8.getValue()].getValue()[tempIndex9.getValue()].getValue()[tempIndex10.getValue()].getValue()[tempIndex11.getValue()].getValue()[tempIndex12.getValue()].getValue()[tempIndex13.getValue()].getValue()[tempIndex14.getValue()].getValue()[tempIndex15.getValue()].getValue()[tempIndex16.getValue()]
                    if(UsedList.getType() == typeExpression.ARRAY or UsedList.getType() == typeExpression.VECTOR):
                        try:
                            return UsedList.getValue()[tempIndex17.getValue()]
                        except:
                            ruta = "Salida.txt"
                            archivo = open(ruta, "a")
                            archivo.write("Error: Index fuera del rango del arreglo\n")
                            archivo.close()
                            #archivo = open("Errores/Errores.txt", "a")
                            #archivo.write("Error: Index fuera del rango del arreglo\n")
                            #archivo.close()
                            #return Symbol('',0,typeExpression.INTEGER,0,0)
                            Environment.saveError("Error: Index fuera del rango del arreglo", 'Local', self.fila, self.columna)
                    else:
                        archivo = open("Salida.txt", "a")
                        archivo.write("Error: Solo se puede ingresar a un array o vector\n")
                        archivo.close()
                        Environment.saveError("Error: Solo se puede ingresar a un array o vector", 'Local', self.fila, self.columna)
                else:
                    archivo = open("Salida.txt", "a")
                    archivo.write("Error: Los indices deben ser integer\n")
                    archivo.close()
                    Environment.saveError("Error: Los indices deben ser integer", 'Local', self.fila, self.columna)
            elif(len(self.indexArray) == 18):
                tempIndex = self.indexArray[0].execute(environment)
                tempIndex2 = self.indexArray[1].execute(environment)
                tempIndex3 = self.indexArray[2].execute(environment)
                tempIndex4 = self.indexArray[3].execute(environment)
                tempIndex5 = self.indexArray[4].execute(environment)
                tempIndex6 = self.indexArray[5].execute(environment)
                tempIndex7 = self.indexArray[6].execute(environment)
                tempIndex8 = self.indexArray[7].execute(environment)
                tempIndex9 = self.indexArray[8].execute(environment)
                tempIndex10 = self.indexArray[9].execute(environment)
                tempIndex11 = self.indexArray[10].execute(environment)
                tempIndex12 = self.indexArray[11].execute(environment)
                tempIndex13 = self.indexArray[12].execute(environment)
                tempIndex14 = self.indexArray[13].execute(environment)
                tempIndex15 = self.indexArray[14].execute(environment)
                tempIndex16 = self.indexArray[15].execute(environment)
                tempIndex17 = self.indexArray[16].execute(environment)
                tempIndex18 = self.indexArray[17].execute(environment)
                if(todosInt):
                    UsedList = List.getValue()[tempIndex.getValue()].getValue()[tempIndex2.getValue()].getValue()[tempIndex3.getValue()].getValue()[tempIndex4.getValue()].getValue()[tempIndex5.getValue()].getValue()[tempIndex6.getValue()].getValue()[tempIndex7.getValue()].getValue()[tempIndex8.getValue()].getValue()[tempIndex9.getValue()].getValue()[tempIndex10.getValue()].getValue()[tempIndex11.getValue()].getValue()[tempIndex12.getValue()].getValue()[tempIndex13.getValue()].getValue()[tempIndex14.getValue()].getValue()[tempIndex15.getValue()].getValue()[tempIndex16.getValue()].getValue()[tempIndex17.getValue()]
                    if(UsedList.getType() == typeExpression.ARRAY or UsedList.getType() == typeExpression.VECTOR):
                        try:
                            return UsedList.getValue()[tempIndex18.getValue()]
                        except:
                            ruta = "Salida.txt"
                            archivo = open(ruta, "a")
                            archivo.write("Error: Index fuera del rango del arreglo\n")
                            archivo.close()
                            #archivo = open("Errores/Errores.txt", "a")
                            #archivo.write("Error: Index fuera del rango del arreglo\n")
                            #archivo.close()
                            #return Symbol('',0,typeExpression.INTEGER,0,0)
                            Environment.saveError("Error: Index fuera del rango del arreglo", 'Local', self.fila, self.columna)
                    else:
                        archivo = open("Salida.txt", "a")
                        archivo.write("Error: Solo se puede ingresar a un array o vector\n")
                        archivo.close()
                        Environment.saveError("Error: Solo se puede ingresar a un array o vector", 'Local', self.fila, self.columna)
                else:
                    archivo = open("Salida.txt", "a")
                    archivo.write("Error: Los indices deben ser integer\n")
                    archivo.close()
                    Environment.saveError("Error: Los indices deben ser integer", 'Local', self.fila, self.columna)
            elif(len(self.indexArray) == 19):
                tempIndex = self.indexArray[0].execute(environment)
                tempIndex2 = self.indexArray[1].execute(environment)
                tempIndex3 = self.indexArray[2].execute(environment)
                tempIndex4 = self.indexArray[3].execute(environment)
                tempIndex5 = self.indexArray[4].execute(environment)
                tempIndex6 = self.indexArray[5].execute(environment)
                tempIndex7 = self.indexArray[6].execute(environment)
                tempIndex8 = self.indexArray[7].execute(environment)
                tempIndex9 = self.indexArray[8].execute(environment)
                tempIndex10 = self.indexArray[9].execute(environment)
                tempIndex11 = self.indexArray[10].execute(environment)
                tempIndex12 = self.indexArray[11].execute(environment)
                tempIndex13 = self.indexArray[12].execute(environment)
                tempIndex14 = self.indexArray[13].execute(environment)
                tempIndex15 = self.indexArray[14].execute(environment)
                tempIndex16 = self.indexArray[15].execute(environment)
                tempIndex17 = self.indexArray[16].execute(environment)
                tempIndex18 = self.indexArray[17].execute(environment)
                tempIndex19 = self.indexArray[18].execute(environment)
                if(todosInt):
                    UsedList = List.getValue()[tempIndex.getValue()].getValue()[tempIndex2.getValue()].getValue()[tempIndex3.getValue()].getValue()[tempIndex4.getValue()].getValue()[tempIndex5.getValue()].getValue()[tempIndex6.getValue()].getValue()[tempIndex7.getValue()].getValue()[tempIndex8.getValue()].getValue()[tempIndex9.getValue()].getValue()[tempIndex10.getValue()].getValue()[tempIndex11.getValue()].getValue()[tempIndex12.getValue()].getValue()[tempIndex13.getValue()].getValue()[tempIndex14.getValue()].getValue()[tempIndex15.getValue()].getValue()[tempIndex16.getValue()].getValue()[tempIndex17.getValue()].getValue()[tempIndex18.getValue()]
                    if(UsedList.getType() == typeExpression.ARRAY or UsedList.getType() == typeExpression.VECTOR):
                        try:
                            return UsedList.getValue()[tempIndex19.getValue()]
                        except:
                            ruta = "Salida.txt"
                            archivo = open(ruta, "a")
                            archivo.write("Error: Index fuera del rango del arreglo\n")
                            archivo.close()
                            #archivo = open("Errores/Errores.txt", "a")
                            #archivo.write("Error: Index fuera del rango del arreglo\n")
                            #archivo.close()
                            #return Symbol('',0,typeExpression.INTEGER,0,0)
                            Environment.saveError("Error: Index fuera del rango del arreglo", 'Local', self.fila, self.columna)
                    else:
                        archivo = open("Salida.txt", "a")
                        archivo.write("Error: Solo se puede ingresar a un array o vector\n")
                        archivo.close()
                        Environment.saveError("Error: Solo se puede ingresar a un array o vector", 'Local', self.fila, self.columna)
                else:
                    archivo = open("Salida.txt", "a")
                    archivo.write("Error: Los indices deben ser integer\n")
                    archivo.close()
                    Environment.saveError("Error: Los indices deben ser integer", 'Local', self.fila, self.columna)
            elif(len(self.indexArray) == 20):
                tempIndex = self.indexArray[0].execute(environment)
                tempIndex2 = self.indexArray[1].execute(environment)
                tempIndex3 = self.indexArray[2].execute(environment)
                tempIndex4 = self.indexArray[3].execute(environment)
                tempIndex5 = self.indexArray[4].execute(environment)
                tempIndex6 = self.indexArray[5].execute(environment)
                tempIndex7 = self.indexArray[6].execute(environment)
                tempIndex8 = self.indexArray[7].execute(environment)
                tempIndex9 = self.indexArray[8].execute(environment)
                tempIndex10 = self.indexArray[9].execute(environment)
                tempIndex11 = self.indexArray[10].execute(environment)
                tempIndex12 = self.indexArray[11].execute(environment)
                tempIndex13 = self.indexArray[12].execute(environment)
                tempIndex14 = self.indexArray[13].execute(environment)
                tempIndex15 = self.indexArray[14].execute(environment)
                tempIndex16 = self.indexArray[15].execute(environment)
                tempIndex17 = self.indexArray[16].execute(environment)
                tempIndex18 = self.indexArray[17].execute(environment)
                tempIndex19 = self.indexArray[18].execute(environment)
                tempIndex20 = self.indexArray[19].execute(environment)
                if(todosInt):
                    UsedList = List.getValue()[tempIndex.getValue()].getValue()[tempIndex2.getValue()].getValue()[tempIndex3.getValue()].getValue()[tempIndex4.getValue()].getValue()[tempIndex5.getValue()].getValue()[tempIndex6.getValue()].getValue()[tempIndex7.getValue()].getValue()[tempIndex8.getValue()].getValue()[tempIndex9.getValue()].getValue()[tempIndex10.getValue()].getValue()[tempIndex11.getValue()].getValue()[tempIndex12.getValue()].getValue()[tempIndex13.getValue()].getValue()[tempIndex14.getValue()].getValue()[tempIndex15.getValue()].getValue()[tempIndex16.getValue()].getValue()[tempIndex17.getValue()].getValue()[tempIndex18.getValue()].getValue()[tempIndex19.getValue()]
                    if(UsedList.getType() == typeExpression.ARRAY or UsedList.getType() == typeExpression.VECTOR):
                        try:
                            return UsedList.getValue()[tempIndex20.getValue()]
                        except:
                            ruta = "Salida.txt"
                            archivo = open(ruta, "a")
                            archivo.write("Error: Index fuera del rango del arreglo\n")
                            archivo.close()
                            #archivo = open("Errores/Errores.txt", "a")
                            #archivo.write("Error: Index fuera del rango del arreglo\n")
                            #archivo.close()
                            #return Symbol('',0,typeExpression.INTEGER,0,0)
                            Environment.saveError("Error: Index fuera del rango del arreglo", 'Local', self.fila, self.columna)
                    else:
                        archivo = open("Salida.txt", "a")
                        archivo.write("Error: Solo se puede ingresar a un array o vector\n")
                        archivo.close()
                        Environment.saveError("Error: Solo se puede ingresar a un array o vector", 'Local', self.fila, self.columna)
                else:
                    archivo = open("Salida.txt", "a")
                    archivo.write("Error: Los indices deben ser integer\n")
                    archivo.close()
                    Environment.saveError("Error: Los indices deben ser integer", 'Local', self.fila, self.columna)   
        else:
            archivo = open("Salida.txt", "a")
            archivo.write("Error: indices solo pueden ser utilizados en arreglos o vectores\n")
            archivo.close()
            Environment.saveError("Error: indices solo pueden ser utilizados en arreglos o vectores", 'Local', self.fila, self.columna)
        return Symbol("",0,typeExpression.INTEGER,0,0) 