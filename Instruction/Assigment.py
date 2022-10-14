from Environment.Environment import Environment
from Abstract.Expression import Expression
from Abstract.Instruction import Instruction
from Enum.typeExpression import typeExpression
class Assignment(Instruction):

    def __init__(self, id: str, value: Expression, indexArray ,fila, columna) -> None:
        self.id = id
        self.value = value
        self.indexArray = indexArray
        self.fila = fila
        self.columna = columna
        self.transfer = False
        
    def execute(self, environment: Environment):
        newValue = self.value.execute(environment)
        if(self.indexArray == None):
            if(isinstance(self.id, list)):
                asig = self.id[0].execute(environment)
                if(asig != None):
                    #print(self.id[0])
                    if(asig.isMutable):
                        encontro = False
                        for i in range(0,len(asig.getValue()[1])):
                            if(asig.getValue()[1][i][0] == self.id[1]):
                                encontro = True
                                if(asig.getValue()[1][i][1] == newValue.getType()):
                                    asig.getValue()[1][i][2] = newValue
                                    break
                                else:
                                    ruta = "Salida.txt"
                                    archivo = open(ruta, "a")
                                    archivo.write("Error: Los tipos no coinciden en la asignacion\n")
                                    archivo.close()
                                    #archivo = open("Errores/Errores.txt", "a")
                                    #archivo.write("Error: Los tipos no coinciden en la asignacion\n")
                                    #archivo.close()
                                    Environment.saveError("Error: Los tipos no coinciden en la asignacion",'Local', self.fila, self.columna)
                                    break
                        #print(asig.getValue()[1][0][2].getValue())
                        if(encontro==False):
                            archivo = open("Salida.txt", "a")
                            archivo.write("Error: El atributo "+ self.id[1] + " no existe\n")
                            archivo.close()
                            Environment.saveError("Error: El atributo "+ self.id[1] + " no existe", 'Local', self.fila, self.columna)
                    else:
                        archivo = open("Salida.txt", "a")
                        archivo.write("Error: La variable "+ self.id[0] + " no es mutable\n")
                        archivo.close()
                        Environment.saveError("Error: La variable "+ self.id[0] + " no es mutable", 'Local', self.fila, self.columna)
                    
                else:
                    archivo = open("Salida.txt", "a")
                    archivo.write("Error: la variable " + id + " no existe\n")
                    archivo.close()
                    #archivo = open("Errores/Errores.txt", "a")
                    #archivo.write("Error: la variable " + id + " no puede ser cambiada de tipo\n")
                    #archivo.close()
                    Environment.saveError("Error: la variable " + id + " no existe", 'Local', self.fila, self.columna)
            else:
                asig = environment.getSVariable(self.id)
                #print(asig.getId())
                if(asig==None):
                    archivo = open("Salida.txt", "a")
                    archivo.write("Error: la variable " + id + " no existe\n")
                    archivo.close()
                    #archivo = open("Errores/Errores.txt", "a")
                    #archivo.write("Error: la variable " + id + " no puede ser cambiada de tipo\n")
                    #archivo.close()
                    Environment.saveError("Error: la variable " + id + " no existe", 'Local', self.fila, self.columna)
                else:
                    if(asig.getType()==typeExpression.STRING or asig.getType()==typeExpression.PSTRING):
                        aux = [self.id,str(newValue.getValue())]
                        asignacion = False
                        value = newValue
                        if(newValue.getId() != ""):
                            value = newValue.getValue()
                            aux[1] = newValue.getId()
                        for temp in Environment.getTemporales():
                            #print(len(temp))
                            if(len(temp) == 5):
                                if str(value.getValue()) == temp[4]:
                                    aux[1] = temp[0]
                                    asignacion = True
                        pointer=""
                        for temp in Environment.getTemporales(): 
                            if(isinstance(temp, list)):
                                if(len(temp) == 3):
                                    if(temp[0] == self.id):
                                        pointer = temp[2]
                                        break
                        Environment.saveTemporal(pointer,"","",Environment.getP())
                        Environment.saveTemporal("H","","",0)
                        Environment.saveExpression("stack[(int)t"+str(Environment.getContador()-2)+"] = t"+str(Environment.getContador()-1)+";")
                        Environment.saveExpression("heap[(int)H] = "+str(len(value.getValue()))+";")
                        for v in value.getValue():
                            Environment.saveExpression("H = H + 1;")
                            Environment.saveExpression("heap[(int)H] = "+str(ord(v))+";")
                        Environment.saveExpression("H = H + 1;")
                    environment.alterVariable(self.id, newValue, self.fila, self.columna)
        else:
                List = environment.getVariable(self.id)
                todosInt = False
                if(List.getType() == typeExpression.ARRAY or List.getType() == typeExpression.VECTOR):
                    for index in self.indexArray:
                        if(index.execute(environment).getType() == typeExpression.INTEGER or index.execute(environment).getType() == typeExpression.USIZE):
                            todosInt = True
                        else:
                            todosInt = False
                            break 
                    if(len(self.indexArray) == 1):
                        tempIndex = self.indexArray[0].execute(environment)
                        if(todosInt):
                            try:
                                List.getValue()[tempIndex.getValue()] = newValue
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
                            archivo.write("Error: El indice debe ser un integer\n")
                            archivo.close()
                            Environment.saveError("Error: El indice debe ser un integer", 'Local', self.fila, self.columna)
                    elif(len(self.indexArray) == 2):
                        tempIndex = self.indexArray[0].execute(environment)
                        tempIndex2 = self.indexArray[1].execute(environment)
                        if(todosInt):
                            UsedList = List.getValue()[tempIndex.getValue()]
                            if(UsedList.getType() == typeExpression.ARRAY or UsedList.getType() == typeExpression.VECTOR):
                                try:
                                    UsedList.getValue()[tempIndex2.getValue()] = newValue
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
                    elif(len(self.indexArray) == 3):
                        tempIndex = self.indexArray[0].execute(environment)
                        tempIndex2 = self.indexArray[1].execute(environment)
                        tempIndex3 = self.indexArray[2].execute(environment)
                        if(todosInt):
                            UsedList = List.getValue()[tempIndex.getValue()].getValue()[tempIndex2.getValue()]
                            if(UsedList.getType() == typeExpression.ARRAY or UsedList.getType() == typeExpression.VECTOR):
                                try:
                                    UsedList.getValue()[tempIndex3.getValue()] = newValue
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
                    elif(len(self.indexArray) == 4):
                        tempIndex = self.indexArray[0].execute(environment)
                        tempIndex2 = self.indexArray[1].execute(environment)
                        tempIndex3 = self.indexArray[2].execute(environment)
                        tempIndex4 = self.indexArray[3].execute(environment)
                        if(todosInt):
                            UsedList = List.getValue()[tempIndex.getValue()].getValue()[tempIndex2.getValue()].getValue()[tempIndex3.getValue()]
                            if(UsedList.getType() == typeExpression.ARRAY or UsedList.getType() == typeExpression.VECTOR):
                                try:
                                    UsedList.getValue()[tempIndex4.getValue()] = newValue
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
                    elif(len(self.indexArray) == 5):
                        tempIndex = self.indexArray[0].execute(environment)
                        tempIndex2 = self.indexArray[1].execute(environment)
                        tempIndex3 = self.indexArray[2].execute(environment)
                        tempIndex4 = self.indexArray[3].execute(environment)
                        tempIndex5 = self.indexArray[4].execute(environment)
                        if(todosInt):
                            UsedList = List.getValue()[tempIndex.getValue()].getValue()[tempIndex2.getValue()].getValue()[tempIndex3.getValue()].getValue()[tempIndex4.getValue()]
                            if(UsedList.getType() == typeExpression.ARRAY or UsedList.getType() == typeExpression.VECTOR):
                                try:
                                    UsedList.getValue()[tempIndex5.getValue()] = newValue
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
                                    UsedList.getValue()[tempIndex6.getValue()] = newValue
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
                                    UsedList.getValue()[tempIndex7.getValue()] = newValue
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
                                    UsedList.getValue()[tempIndex8.getValue()] = newValue
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
                                    UsedList.getValue()[tempIndex9.getValue()] = newValue
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
                                    UsedList.getValue()[tempIndex10.getValue()] = newValue
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
                                    UsedList.getValue()[tempIndex11.getValue()] = newValue
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
                                    UsedList.getValue()[tempIndex12.getValue()] = newValue
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
                                    UsedList.getValue()[tempIndex13.getValue()] = newValue
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
                                    UsedList.getValue()[tempIndex14.getValue()] = newValue
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
                                    UsedList.getValue()[tempIndex15.getValue()] = newValue
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
                                    UsedList.getValue()[tempIndex16.getValue()] = newValue
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
                                    UsedList.getValue()[tempIndex17.getValue()] = newValue
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
                                    UsedList.getValue()[tempIndex18.getValue()] = newValue
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
                                    UsedList.getValue()[tempIndex19.getValue()] = newValue
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
                                    UsedList.getValue()[tempIndex20.getValue()] = newValue
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
                    archivo.write("Error: indices solo pueden ser utilizados en arreglos o vectores\n")
                    archivo.close()
                    Environment.saveError("Error: indices solo pueden ser utilizados en arreglos o vectores", 'Local', self.fila, self.columna)