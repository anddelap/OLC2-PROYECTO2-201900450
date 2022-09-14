from Enum.typeExpression import typeExpression
from Environment.Environment import Environment
from Environment.Symbol import Symbol
from Abstract.Expression import Expression
from Enum.nativeFunction import nativeFunction
from Expression.Array import Array
from Expression.Primitive import Primitive
import copy
class StructDec(Expression):
    def __init__(self, value, fila, columna):
        self.value = value
        self.fila = fila
        self.columna = columna
    def execute(self, environment: Environment) -> Symbol:
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
                    #print("Entra")
                    return Symbol("",var,[typeExpression.STRUCT,tempStruct.id],0,0)
            else:
                ruta = "Salida.txt"
                archivo = open(ruta, "a")
                archivo.write("Error: El struct no tiene el numero de atributos requeridos\n")
                archivo.close()
                #archivo = open("Errores/Errores.txt", "a")
                #archivo.write("Error: Los tipos no coinciden en la declaracion\n")
                #archivo.close()
                Environment.saveError("Error: El struct no tiene el numero de atributos requeridos",'Local', self.fila, self.columna)