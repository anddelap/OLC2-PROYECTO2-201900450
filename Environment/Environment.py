from Enum.typeExpression import typeExpression
from Environment.Symbol import Symbol
from app import Errores
import datetime

errores = []
simbolos = []
temporales = []
funcionesC3D = []
stack = []
heap = []
contador = 0
contadorL = 0
class Environment:
    def __init__(self,father):
        #Usamos un dicionario para nuestra tabla de simbolos, guardara el id como clave y como cuerpo el simbolo
        self.variable = {}
        self.function = {}
        self.struct = {}
        #Father es el entorno exterior al que podemos acceder
        self.father = father
        #self.errores={}
    #========================== PARA ERRORES =====================
    def saveError(description, ambito, fila, columna):
        global errores
        errores.append((str(len(errores)+1), description, ambito, str(fila), columna, str(datetime.datetime.now())))
    # ========================== TEMPORALES ==========================
    def saveTemporal(expresion1,operation,expresion2 ,resultado):
        global temporales
        global contador
        temporales.append(["t"+str(contador),expresion1,operation,expresion2,resultado])
        contador += 1
        
    def saveDeclaration(id,expresion):
        global temporales
        temporales.append([id,expresion])

    def saveExpression(expression):
        global temporales
        temporales.append(expression)

    def getTemporales():
        return temporales
    
    def getContador():
        global contador
        return contador
    #========================== ETIQUETAS ==========================
    def getEtiqueta():
        global contadorL
        return contadorL

    def aumentarContadorL():
        global contadorL
        contadorL += 1
    
    #========================== PARA VARIABLES =====================
    def saveVariable(self, id:str, value, type: typeExpression, fila: int, columna: int, isArray: bool, mutable: bool, temporal: bool):
        if(self.variable.get(id) != None):
            archivo = open("Salida.txt", "a")
            archivo.write("Error: La variable "+ id +" ya existe\n")
            #archivo = open("Errores/Errores.txt", "a")
            #archivo.write("Error: La variable "+ id +" ya existe\n")
            #archivo.close()
            Environment.saveError("Error: La variable "+ id +" ya existe", 'Local', fila, columna)
            return
        tempVar = Symbol(id,value,type,fila,columna)
        if(value != None and type != None):
            value.isMutable = mutable
            tempVar.isArray = isArray
            tempVar.isMutable = mutable
            self.variable[id] = tempVar
            global simbolos
            if(temporal == False):
                if (type == typeExpression.INTEGER):
                    simbolos.append((id,"Variable","Int","Local",fila,columna))
                elif (type == typeExpression.USIZE):
                    simbolos.append((id,"Variable","usize","Local",fila,columna))
                elif (type == typeExpression.STRING):
                    simbolos.append((id,"Variable","String","Local",fila,columna))
                elif (type == typeExpression.PSTRING):
                    simbolos.append((id,"Variable","&str","Local",fila,columna))
                elif (type == typeExpression.FLOAT):
                    simbolos.append((id,"Variable","Float","Local",fila,columna))
                elif (type == typeExpression.BOOL):
                    simbolos.append((id,"Variable","Bool","Local",fila,columna))
                elif (type == typeExpression.CHAR):
                    simbolos.append((id,"Variable","Char","Local",fila,columna))
                elif (type == typeExpression.ARRAY):
                    #valorr = self.printarray(value)
                    simbolos.append((id,"Variable","Array","Local",fila,columna))
                elif (type == typeExpression.VECTOR):
                    #valorr = self.printarray(value)
                    simbolos.append((id,"Variable","Vector","Local",fila,columna))
                elif(isinstance(type,list)):
                    if(type[0] == typeExpression.STRUCT):
                        simbolos.append((id,"Variable",type[1],"Local",fila,columna))
        else:
            self.variable[id] = tempVar
    
    def getVariable(self, id: str)-> Symbol:
        tempVar = self
        while (tempVar != None):
            if (tempVar.variable.get(id) != None):
                return tempVar.variable.get(id).getValue()
            tempVar = tempVar.father
        #archivo = open("Salida.txt", "a")
        #archivo.write("Error: la variable "+ id + " no existe\n")
        #archivo.close()
        return None
    
    def getSVariable(self, id: str)-> Symbol:
        tempVar = self
        while (tempVar != None):
            if (tempVar.variable.get(id) != None):
                return tempVar.variable.get(id)
            tempVar = tempVar.father
        #archivo = open("Salida.txt", "a")
        #archivo.write("Error: la variable "+ id + " no existe\n")
        #archivo.close()
        return None

    def alterVariable(self, id: str, value: Symbol, fila, columna):
        tempEnv = self
        while(tempEnv != None):
            if(tempEnv.variable.get(id) != None):
                tempVar: Symbol = tempEnv.variable.get(id)
                if(tempVar.getType() == value.getType()):
                    if(tempVar.isMutable == True):
                        tempVar.value = value
                        self.variable[id] = tempVar
                        return
                    else: 
                        archivo = open("Salida.txt", "a")
                        archivo.write("Error: La variable "+ id +" no es mutable\n")
                        archivo.close()
                        Environment.saveError("Error: La variable "+ id +" no es mutable", 'Local', fila, columna)
                        return
                else:
                    tempVar: Symbol = tempEnv.variable.get(id)
                    if(tempVar.getType() == typeExpression.USIZE and value.getType() == typeExpression.INTEGER):
                        tempVar.value = value
                        tempVar.type = typeExpression.USIZE
                        self.variable[id] = tempVar
                        return
                    archivo = open("Salida.txt", "a")
                    archivo.write("Error: la variable " + id + " no puede ser cambiada de tipo\n")
                    archivo.close()
                    #archivo = open("Errores/Errores.txt", "a")
                    #archivo.write("Error: la variable " + id + " no puede ser cambiada de tipo\n")
                    #archivo.close()
                    Environment.saveError("Error: la variable " + id + " no puede ser cambiada de tipo", 'Local', fila, columna)
                    return
            tempEnv = tempEnv.father
        archivo = open("Salida.txt", "a")
        archivo.write("Error: la variable " + id + " no existe\n")
        archivo.close()
        #archivo = open("Errores/Errores.txt", "a")
        #archivo.write("Error: la variable " + id + " no existe\n")
        #archivo.close()
        Environment.saveError("Error: la variable " + id + " no existe", 'Local', fila, columna)
        return None

    #========================== PARA FUNCIONES =====================
    
    def saveFunction(self, id: str, function,fila,columna):
        if (self.function.get(id) != None):
            archivo = open("Salida.txt", "a")
            archivo.write("Error: La función " + id + " ya existe\n")
            archivo.close()
            #archivo = open("Errores/Errores.txt", "a")
            #archivo.write("Error: la función " + id + " ya existe\n")
            #archivo.close()
            Environment.saveError("Error: la función " + id + " ya existe", 'Local', fila, columna)
            return
        self.function[id] = function
        simbolos.append((id,"Function","-","Global",fila,columna))
           
    def getFunction(self, id: str, fila, columna):
        tempEnv = self
        while(tempEnv != None):
            if(tempEnv.function.get(id) != None):
                return tempEnv.function.get(id)
            tempEnv = tempEnv.father
        archivo = open("Salida.txt", "a")
        archivo.write("Error: La función " + id + " no existe\n")
        archivo.close()
        #archivo = open("Errores/Errores.txt", "a")
        #archivo.write("Error: la función " + id + " no existe\n")
        #archivo.close()
        Environment.saveError("Error: La función " + id + " no existe", 'Local', fila, columna)
        return None
    
    def getGlobal(self):
        tempEnv: Environment = self
        while(tempEnv.father != None):
            tempEnv = tempEnv.father
        return tempEnv

    #========================== PARA STRUCTS =====================

    def saveStruct(self, id: str, struct,fila,columna):
        if (self.struct.get(id) != None):
            archivo = open("Salida.txt", "a")
            archivo.write("Error: El struct " + id + " ya existe\n")
            archivo.close()
            #archivo = open("Errores/Errores.txt", "a")
            #archivo.write("Error: el struct " + id + " ya existe\n")
            #archivo.close()
            Environment.saveError("Error: El struct " + id + " ya existe", 'Local', fila, columna)
            return
        self.struct[id] = struct
        simbolos.append((id,"Struct","-","Global",fila,columna))

    def getStruct(self, id: str, fila, columna):
        tempEnv = self
        while(tempEnv != None):
            if(tempEnv.struct.get(id) != None):
                return tempEnv.struct.get(id)
            tempEnv = tempEnv.father
        archivo = open("Salida.txt", "a")
        archivo.write("Error: El struct " + id + " no existe\n")
        archivo.close()
        #archivo = open("Errores/Errores.txt", "a")
        #archivo.write("Error: El struct " + id + " no existe\n")
        #archivo.close()
        Environment.saveError("Error: El struct " + id + " no existe", 'Local', fila, columna)
        return None
    # ========================== PARA ARRAY ========================
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
