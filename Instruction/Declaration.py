from copy import copy
from xmlrpc.client import FastMarshaller
from Environment.Symbol import Symbol
from Expression.Primitive import Primitive
from Abstract.Instruction import Instruction
from Abstract.Expression import Expression
from Environment.Environment import Environment
from Enum.typeExpression import typeExpression
from Expression.Struct import Struct
import copy
class Declaration(Instruction):
    def __init__(self, id: str, type: typeExpression, value: Expression, fila: int, columna: int, isArray: bool, mutable:bool, sizeArray, isVector:bool, struct: bool ) -> None:
        self.id = id
        self.type = type
        self.value = value
        self.fila = fila
        self.columna = columna
        self.isArray = isArray
        self.isVector = isVector
        self.mutable = mutable
        self.transfer = False
        self.sizeArray = sizeArray
        self.struct = struct
    def execute(self, environment:Environment):
        if(self.struct == False):
            tempValue = self.value.execute(environment)
            if(self.isArray == False):
                if(self.type != None):
                    if (self.type.value != tempValue.getType().value):
                        if(self.type == typeExpression.USIZE and tempValue.getType() == typeExpression.INTEGER):
                            tempValue.type = typeExpression.USIZE
                            environment.saveVariable(self.id, tempValue, self.type, self.fila, self.columna, self.isArray,self.mutable,False)
                            return
                        else:
                            ruta = "Salida.txt"
                            archivo = open(ruta, "a")
                            archivo.write("Error: Los tipos no coinciden en la declaracion\n")
                            archivo.close()
                            #archivo = open("Errores/Errores.txt", "a")
                            #archivo.write("Error: Los tipos no coinciden en la declaracion\n")
                            #archivo.close()
                            Environment.saveError("Error: Los tipos no coinciden en la declaracion",'Local', self.fila, self.columna)
                            environment.saveVariable('None',Primitive(0,typeExpression.INTEGER).execute(environment),typeExpression.INTEGER, self.fila, self.columna,self.isArray,self.mutable,False)
                            return
                    aux = [self.id,""]
                    asignacion = False
                    for temp in Environment.getTemporales():
                        #print(len(temp))
                        if(len(temp) == 5):
                            if str(tempValue.getValue()) == temp[4]:
                                aux[1] = str(temp[0])
                                asignacion = True
                            #Environment.saveDeclaration(self.id,temp[0])
                    if(asignacion == True):
                        Environment.saveDeclaration(aux[0],aux[1])
                    else:
                        Environment.saveDeclaration(self.id,str(tempValue.getValue()))

                    environment.saveVariable(self.id, tempValue, self.type, self.fila, self.columna, self.isArray,self.mutable, False)
                else:
                    aux = [self.id,""]
                    asignacion = False
                    for temp in Environment.getTemporales():
                        #print(len(temp))
                        if(len(temp) == 5):
                            if str(tempValue.getValue()) == temp[4]:
                                aux[1] = temp[0]
                                asignacion = True
                            #Environment.saveDeclaration(self.id,temp[0])
                    if(asignacion == True):
                        Environment.saveDeclaration(aux[0],aux[1])
                    else:
                        if(tempValue.getId()==""):
                            Environment.saveDeclaration(self.id,str(tempValue.getValue()))
                        elif tempValue.getId() != "":
                            Environment.saveDeclaration(self.id,tempValue.getId())
                    
                    environment.saveVariable(self.id, tempValue, tempValue.getType(), self.fila, self.columna, self.isArray,self.mutable, False)
            else:
                if(self.isVector == False):
                    correct = True
                    tempArray = self.value.execute(environment)
                    size = self.sizeArray.execute(environment)
                    if( size.getValue() == len(tempValue.getValue())):
                        for tempValue in tempArray.getValue():
                            #value = tempValue.execute(environment)
                            if(self.type.value != tempValue.getType().value):
                                correct = False
                                break
                        if(correct == True):
                            environment.saveVariable(self.id, tempArray, typeExpression.ARRAY, self.fila, self.columna, self.isArray,self.mutable, False)
                        else:
                            ruta = "Salida.txt"
                            archivo = open(ruta, "a")
                            archivo.write("Error: Los elementos del arreglo no son del tipo requerido\n")
                            archivo.close()
                            #archivo = open("Errores/Errores.txt", "a")
                            #archivo.write("Error: Los tipos no coinciden en la declaracion\n")
                            #archivo.close()
                            Environment.saveError("Error: Los elementos del arreglo no son del tipo requerido",'Local', self.fila, self.columna)
                            
                    else:
                        ruta = "Salida.txt"
                        archivo = open(ruta, "a")
                        archivo.write("Error: El arreglo no es del tamaño que se requiere\n")
                        archivo.close()
                        #archivo = open("Errores/Errores.txt", "a")
                        #archivo.write("Error: Los tipos no coinciden en la declaracion\n")
                        #archivo.close()
                        Environment.saveError("Error: El arreglo no es del tamaño que se requiere",'Local', self.fila, self.columna)
                        #environment.saveVariable('None',Primitive(0,typeExpression.INTEGER).execute(environment),typeExpression.INTEGER, self.fila, self.columna,self.isArray,self.mutable)
                        #return
                else:
                    tempVector = self.value.execute(environment)
                    if(len(tempVector.getValue())==0):
                        environment.saveVariable(self.id, tempVector, typeExpression.VECTOR, self.fila, self.columna, self.isArray,self.mutable, False)
                    else:
                        correct = True
                        for tempValue in tempVector.getValue():
                            #value = tempValue.execute(environment)
                            if(self.type.value != tempValue.getType().value):
                                correct = False
                                break
                        if(correct == True):
                            environment.saveVariable(self.id, tempVector, typeExpression.VECTOR, self.fila, self.columna, self.isArray,self.mutable, False)
                        else:
                            ruta = "Salida.txt"
                            archivo = open(ruta, "a")
                            archivo.write("Error: Los elementos del arreglo no son del tipo requerido\n")
                            archivo.close()
                            #archivo = open("Errores/Errores.txt", "a")
                            #archivo.write("Error: Los tipos no coinciden en la declaracion\n")
                            #archivo.close()
                            Environment.saveError("Error: Los elementos del vector no son del tipo requerido",'Local', self.fila, self.columna)
        else:
            tempStruct = environment.getStruct(self.value[0],self.fila,self.columna)
            #print(tempStruct.atributos)
            copyA = copy.deepcopy(tempStruct.atributos)
            var = [tempStruct.id , copyA]
            if(tempStruct != None):
                if(len(var[1])==len(self.value[1])):
                    correcto = True
                    for i in range(0,len(tempStruct.atributos)):
                        if(tempStruct.atributos[i][0] == self.value[1][i][0]):
                            value = self.value[1][i][1].execute(environment)
                            if(value.getType() == tempStruct.atributos[i][1]): 
                                var[1][i][2] = value

                            else:
                                ruta = "Salida.txt"
                                archivo = open(ruta, "a")
                                archivo.write("Error: Los tipos no coinciden en la declaracion de "+self.value[1][i][0]+"\n")
                                archivo.close()
                                #archivo = open("Errores/Errores.txt", "a")
                                #archivo.write("Error: Los tipos no coinciden en la declaracion\n")
                                #archivo.close()
                                Environment.saveError("Error: Los tipos no coinciden en la declaracion de "+self.value[1][i][0],'Local', self.fila, self.columna)
                                correcto = False
                                break
                        else:
                            ruta = "Salida.txt"
                            archivo = open(ruta, "a")
                            archivo.write("Error: El atributo "+ self.value[1][i][0] +" no pertenece al struct "+ tempStruct.id +"\n")
                            archivo.close()
                            #archivo = open("Errores/Errores.txt", "a")
                            #archivo.write("Error: Los tipos no coinciden en la declaracion\n")
                            #archivo.close()
                            Environment.saveError("Error: El atributo "+ self.value[1][i][0] +" no pertenece al struct "+ tempStruct.id,'Local', self.fila, self.columna)
                            correcto = False
                            break
                    if(correcto == True):
                        #print(var[1])
                        #print(tempStruct.atributos)
                        environment.saveVariable(self.id, Symbol("",var,typeExpression.STRUCT,0,0), [typeExpression.STRUCT, tempStruct.id], self.fila, self.columna, self.isArray,self.mutable, False)
                else:
                    ruta = "Salida.txt"
                    archivo = open(ruta, "a")
                    archivo.write("Error: El struct no tiene el numero de atributos requeridos\n")
                    archivo.close()
                    #archivo = open("Errores/Errores.txt", "a")
                    #archivo.write("Error: Los tipos no coinciden en la declaracion\n")
                    #archivo.close()
                    Environment.saveError("Error: El struct no tiene el numero de atributos requeridos",'Local', self.fila, self.columna)



        
