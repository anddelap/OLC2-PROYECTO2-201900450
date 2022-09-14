reserved ={
    #'print' : 'RPRINT',
    'println' : 'RPRINTLN',
    # ========Tipos de datos validos ========= (Palabras Reservadas)
    'i64':'I64',
    'f64':'F64',
    'bool':'BOOL',
    'char':'CHAR',
    'String':'RSTRING',
    'str':'PSTRING',
    'usize':'USIZE',
    # ========Operaciones =========
    'pow': 'RPOW',
    'powf': 'RPOWF',
    # ========Asignacion ========
    "vec":"RVEC",
    "Vec":"DECVEC",
    "new":"NEW",
    "with_capacity":"WCAPACITY",
    #'global':'GLOBAL',
    #'local':'LOCAL',
    'let':'LET',
    'mut':'MUT',
    #Nativas
    'log10':'LOG10',
    'log':'LOG',
    'sin':'SIN',
    'cos':'COS',
    'tan':'TAN',
    #BOOL
    'true':'TRUE',
    'false': 'FALSE',
    # ========Funciones =========
    #main
    'main':'RMAIN',
    #Creacion
    'fn': 'FN',
    'end': 'END',
    #Funciones Nativas
    'sqrt':'SQRT',
    'abs':'ABS',
    'to_string':'TO_STRING',
    'to_owned':'TO_OWNED',
    'clone':'CLONE',
    'chars':'CHARS',
    'len': 'RLEN',
    'contains':'CONTAINS',
    'capacity':'CAPACITY',
    #'trunc':'TRUNC',
    #'parse':'PARSE',
    #'float': 'FLOAT',
    #'typeof':'TYPEOF',
    #'length': 'LENGTH',
    #'uppercase': 'UPPER',
    #'lowercase': 'LOWER',
    'push':'RPUSH',
    'insert':'INSERT',
    'remove':'REMOVE',
    #'pop':'POP',
    #=========Casteo ========
    'as':'AS',
    # ========Loops =========
    #While.
    'while':'RWHILE',
    #For
    'for': 'RFOR',
    'in': 'IN',
    #Loop
    'loop':'RLOOP',
    #Setencias de tranferencia
    'break':    'BREAK',
    'continue': 'CONTINUE',
    'return'  : 'RETURN',
    # ========Condicionales =========
    'if':'RIF',
    #'elseif': 'ELSEIF',
    'else': 'RELSE',
    'match': 'RMATCH',
    # ======== Structs =========
    'struct': 'STRUCT',
}
tokens =[
    
    # ========Otros =============
    #Tipos de numeros
    'DECIMAL',
    'ENTERO',
    #Tipos de palabras
    'CARACTER',
    'CADENA',
    #Simbolos
    'PARIZQ',
    'PARDER',
    'PICOMA',
    'COMA',
    'LLAVEIZQ',
    'LLAVEDER',
    'POINTER',
    'GUIONBAJO',
    # ========Expresiones =======
    #Aritmeticas
    #Suma
    'MAS',
    #Resta
    'MENOS',
    #Multiplicacion
    'POR',
    #Division
    'DIVIDIDO',
    #Potencia
    #'POTENCIA',
    #Modulo
    'MODULO',
    #Relacionales
    'MAYORQUE',
    'MENORQUE',
    'MAYORIGUAL',
    'MENORIGUAL',
    'IGUALIGUAL',
    'DIFERENCIA',
    #Coincidencia
    'PALO',
    #Logicas
    'AND',
    'OR',
    'NOT',
    # ========Impresion =========
    #'RPRINT',
    #'RPRINTLN',
    # ========Asignacion =========
    #'GLOBAL',
    #'LOCAL',
    'IGUAL',
    'DOSPUNTOS',
    'ID',
    # ========Funciones =========
    #Creacion
    #Funciones Nativas
    'PUNTO',
    #LLamada
    #Paso por valor o referencia
    # ========Condicionales =========
    # ========Loops =========
    #While
    #For
    #Setencias de tranferencia
    #========Arreglos =======
    'CORDER',
    'CORIZQ',
    #========Structs ========
] + list(reserved.values())

#Tokens
# ========Otros =============
#'POINTER',
t_POINTER = r'&'
#Tipos de numeros
#'DECIMAL',
def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        ruta = "Salida.txt"
        archivo = open(ruta, "a")
        archivo.write("Floaat value too large %d\n", t.value)
        archivo.close()
        #Salida.append("Floaat value too large %d\n", t.value)
        t.value = 0
    return t
#'ENTERO',
def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        #Salida.append("Integer value too large %d\n", t.value)
        ruta = "Salida.txt"
        archivo = open(ruta, "a")
        archivo.write("Integer value too large %d\n", t.value)
        archivo.close()
        t.value = 0
    return t
#Tipos de palabras
#'CARACTER',
def t_CARACTER(t):
    r'\'.?\''
    t.value = t.value[1:-1]
    return t
#'CADENA',
def t_CADENA(t):
    r'\".*?\"'
    t.value = t.value[1:-1]
    return t
#Booleano
#'BOOLEANO',
#Simbolos
#'PARIZQ',
t_PARIZQ    = r'\('
#'PARDER',
t_PARDER    = r'\)'
#'PICOMA',
t_PICOMA    =r';'
#'COMA',
t_COMA      =r'\,'
#'LLAVEIZQ',
t_LLAVEIZQ  = r'\{'
#'LLAVEDER',
t_LLAVEDER  = r'\}'
# ========Expresiones =======
#Aritmeticas
#Suma
t_MAS       = r'\+'
#Resta
t_MENOS     = r'-'
#Multiplicacion
t_POR       = r'\*'
#Division
t_DIVIDIDO  = r'/'
#Potencia
#t_POTENCIA  = r'\^'
#Modulo
t_MODULO    = r'%'
#Nativas
#Relacionales
#'MAYORQUE',
t_MAYORQUE   = r'>'
#'MENORQUE',
t_MENORQUE   = r'<'
#'MAYORIGUAL',
t_MAYORIGUAL = r'>='
#'MENORIGUAL',
t_MENORIGUAL = r'<='
#'IGUALIGUAL',
t_IGUALIGUAL = r'=='
#'DIFERENCIA',
t_DIFERENCIA= r'!='
#Coinicionales
t_PALO      = r'\|'
#Logicas
#'AND',
t_AND       = r'&&'
#'OR',
t_OR        = r'\|\|'
#'NOT',
t_NOT       = r'!' 
# ========Asignacion =========
#'IGUAL',
t_IGUAL     = r'='
#'DOSPUNTOS',
t_DOSPUNTOS = r':'
#'PUNTO',
t_PUNTO = r'.'
#'GUIONBAJO',
t_GUIONBAJO = r'_'
#'ID'
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type= reserved.get(t.value,'ID')
    return t
# ========Funciones =========
#Creacion
#Funciones Nativas
#LLamada
#Paso por valor o referencia
# ========Condicionales =========
# ========Loops =========
#While
#For
#Setencias de tranferencia
#========Arreglos =======
t_CORDER = r'\]'
t_CORIZQ = r'\['
#========Structs ========
#========Ignore =========
t_ignore = " \t\r"
#========Comentarios=====
def t_COMMENTM(t):
    #r'\#=(.|\n)*?=\#'
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count("\n")
    pass
     # No return value. Token discarded
#t_ignore_COMMENTM = r'\#=(.|\n)*?=\#'
t_ignore_COMMENTU = r'\/\/.*'
#========Error =========
def t_error(t):
    #global Salida
    #Salida += "Illegal character '%s'" % t.value[0]
     
    #Salida.append( "Illegal character '%s'\n" % t.value[0])
    ruta = "Salida.txt"
    archivo = open(ruta, "a")
    archivo.write("Error Lexico: Caractér ilegal en "+str(t.lineno)+". Caracter: '%s'\n" % t.value[0])
    archivo.close()
    #archivo = open("Errores/Errores.txt", "a")
    #archivo.write("Error Lexico: Caractér ilegal en "+str(t.lineno)+". Caracter: '%s'\n" % t.value[0])
    #archivo.close()
    #Environment.errores.append((str(len(Environment.errores)+1),"Error Lexico: Caractér ilegal "+t.value[0],'Global', str(t.lineno), str(t.lexpos(1))))
    Environment.saveError("Error Lexico: Caractér ilegal "+t.value[0], 'Global', t.lineno, t.lexpos)
    #print( Environment.errs)
    t.lexer.skip(1)
#========Salto de Linea ==    
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Construyendo el analizador léxico
#from Expression.ArrayCallAsig import ArrayCallAsig
#from Instruction.AssigArray import AssigArray
#from Expression.ArrayCall import ArrayCall
#from Instruction.transSen import transSen
#from Instruction.PrintlnList import PrintlnList
#from Instruction.PrintList import PrintList
#from Instruction.Block import Block
#Enums
from Enum.transferSen import trasnferSen
from Enum.arithmeticOperation import arithmeticOperation
from Enum.nativeOperation import nativeOperation
from Enum.relationalOperation import relationalOperation
from Enum.logicOperation import logicOperation
from Enum.nativeFunction import nativeFunction
#Entorno
from Environment.Environment import Environment
from Expression.StructDec import StructDec
#Instrucciones
from Instruction.Main import Main
from Instruction.Println import Println
from Instruction.Declaration import Declaration
from Instruction.Assigment import Assignment
from Instruction.Function import Function
from Instruction.CallFuncSt import CallFuncSt
from Instruction.Parameter import Parameter
from Instruction.While import While
from Instruction.Loop import Loop
from Instruction.If import If
from Instruction.Match import Match
from Instruction.For import For
from Instruction.Natives.Push import Push
from Instruction.Natives.Insert import Insert
from Instruction.Natives.Remove import Remove
#Expresion
from Expression.Primitive import Primitive
from Expression.Arithmetic import Arithmetic
from Expression.Relational import Relational
from Expression.Logic import Logic
from Expression.VariableCall import VariableCall
from Expression.Casteo import Casteo
from Expression.Struct import Struct
#from Expression.Natives import Native
from Expression.NativesF import NativeFunction
from Enum.typeExpression import typeExpression
from Expression.Array import Array
from Expression.Vector import Vector
from Expression.transSen import transSen
from Expression.ArrayAccess import ArrayAccess
from Expression.StructAccess import StructAccess
import ply.lex as lex
lexer = lex.lex()

#def find_column(input, token):
#     line_start = input.rfind('\n', 0, token.lexpos) + 1
#     return (token.lexpos - line_start) + 1
#==================================================================== SINTACTICO ============================================================
# Asociación de operadores y precedencia
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('right', 'NOT'),
    ('left','IGUALIGUAL','DIFERENCIA','MENORQUE','MENORIGUAL','MAYORQUE','MAYORIGUAL'),
    ('left','MAS','MENOS'),
    ('left','POR','DIVIDIDO','MODULO'),
    ('right','UMENOS'),
    ('left', 'RPOW', 'RPOWF'),
)

# Definición de la gramática=====================================================
def p_inicio(t):
    '''inicio : instructions '''
    globalEnv = Environment(None)
    for ins in t[1]:
        ins.execute(globalEnv)
#================================================================================
def p_instructions(t):
    '''instructions : instructions instruction
                    | instruction
    '''
    if(len(t)==3):
        t[1].append(t[2])
        t[0] = t[1]
    elif(len(t)==2):
        t[0]=[t[1]]
#================================================================================
#def p_instruction(t):
#    '''instruction  : impresion
#                    | declaration
#                    | assigment
#    '''
#    t[0]=t[1]
#| function
#| callFuncSt
#| whileSt
#| assig_array
#| ifSt
#| forSt
#| trans
def p_instruction(t):
    '''instruction  : function
                    | struct
                    | main
    '''
    t[0]=t[1]
#: main
def p_main(t):
    '''
        main : FN RMAIN PARIZQ PARDER LLAVEIZQ ins LLAVEDER
    '''
    t[0] = Main(t[6])
def p_ins(t):
    '''
        ins : ins in
            | in
    '''
    if(len(t)==3):
        t[1].append(t[2])
        t[0] = t[1]
    elif(len(t)==2):
        t[0]=[t[1]]

def p_in(t):
    '''in : impresion
          | declaration
          | assigment
          | whileSt
          | ifSt
          | matchSt
          | forSt
          | loopSt
          | withpointSt
          | trans
          | callFuncSt
    '''
    t[0]=t[1]
#================================================================================

#================================================================================
def p_impresion(t):
    '''impresion : RPRINTLN NOT PARIZQ expresion PARDER PICOMA
                 | RPRINTLN NOT PARIZQ listPrint PARDER PICOMA'''
    if(len(t[1]) == 7):
        t[0] = Println(t[4], t.lineno(1),t.lexpos(1))

def p_listPrintValues(t):
    '''listPrint   : listPrint COMA expresion
                    | expresion
    '''
    if(len(t) == 4):
        t[1].append(t[3])
        t[0] = t[1]
    elif(len(t) == 2):
        t[0] = [t[1]]
#================================================================================
def p_declaration(t):
    '''declaration : LET MUT ID DOSPUNTOS typeDef IGUAL expresion PICOMA
                   | LET ID DOSPUNTOS typeDef IGUAL expresion PICOMA  
                   | LET MUT ID IGUAL expresion PICOMA  
                   | LET ID IGUAL expresion PICOMA  
                   | LET MUT ID DOSPUNTOS CORIZQ typeDef PICOMA expresion CORDER IGUAL expresion PICOMA   
                   | LET ID DOSPUNTOS CORIZQ typeDef PICOMA expresion CORDER IGUAL expresion PICOMA
                   | LET MUT ID DOSPUNTOS DECVEC MENORQUE typeDef MAYORQUE IGUAL expresion PICOMA   
                   | LET ID DOSPUNTOS DECVEC MENORQUE typeDef MAYORQUE IGUAL expresion PICOMA 
    '''
    # 1) Declaración de variable con tipo mutable
    # 2) Declaración de variable con tipo no mutable
    # 3) Declaración de variable sin tipo mutable
    # 4) Declaración de variable sin tipo no mutable
    # 5) Declaración de variable tipo arreglo de 1 dimension mutable
    # 6) Declaración de variable tipo arreglo de 1 dimension no mutable
    # 7) Declaración de variable tipo vector mutable
    # 8) Declaración de variable tipo vector no mutable 
    # 9) Declaracion de variable tipo struct mutable
    # 10) Declaracion de variable tipo struct no mutable

    if(len(t)==9):
        t[0] = Declaration(t[3], t[5], t[7], t.lineno(1),t.lexpos(1), False, True, None,False,False) #1
    elif(len(t)==8):
        t[0] = Declaration(t[2], t[4], t[6], t.lineno(1),t.lexpos(1), False, False, None,False,False) #2
    elif(len(t)==7):
        if(isinstance(t[5],list)):
            t[0] = Declaration(t[3], typeExpression.STRUCT, t[5], t.lineno(1),t.lexpos(1), False, True, None,False,True) #9
        else:
            t[0] = Declaration(t[3], None, t[5], t.lineno(1),t.lexpos(1), False, True, None,False,False) #3
    elif(len(t)==6):
        if(isinstance(t[4],list)):
            t[0] = Declaration(t[2], typeExpression.STRUCT, t[4], t.lineno(1),t.lexpos(1), False, False, None,False,True) #10
        else:
            t[0] = Declaration(t[2], None, t[4], t.lineno(1),t.lexpos(1), False, False, None,False,False) #4
    elif(len(t)==13):
        t[0] = Declaration(t[3], t[6], t[11], t.lineno(1),t.lexpos(1), True, True, t[8],False,False) #5
    elif(len(t)==12):
        if(t[5]=='Vec'):
            t[0] = Declaration(t[3], t[7], t[10], t.lineno(1),t.lexpos(1), True, True, None,True),False #7
        else:
            t[0] = Declaration(t[2], t[5], t[10], t.lineno(1),t.lexpos(1), True, False, t[7],False,False) #6
    elif(len(t)==11):
        t[0] = Declaration(t[2], t[6], t[9], t.lineno(1),t.lexpos(1), True, False, None,True,False) #8
#    | ID IGUAL expresion PICOMA
#    | ID IGUAL CORIZQ listValues CORDER PICOMA   
#    elif(len(t)==5):
#        t[0] = Assignment(t[1], t[3], t.lineno(1),t.lexpos(1))
#    elif (len(t)==7):
#        t[0] = Declaration(t[1], typeExpression.ARRAY, Array(t[4],t.lineno(1), t.lexpos(1)), t.lineno(1), t.lexpos(1), True)
#def p_specialDeclaration(t):
#    '''
#        specialDeclaration: LET ID IGUAL ifSt PICOMA
#    '''
#    t[0] = Declaration(t[2], None, t[4], t.lineno(1),t.lexpos(1), False, False, None,False,True)
#================================================================================
def p_struct(t):
    '''struct : STRUCT ID LLAVEIZQ structBody LLAVEDER
    '''
    t[0] = Struct(t[2],t[4],t.lineno(1),t.lexpos(1))

def p_structBody(t):
    '''structBody : structBody COMA atributo
                  | atributo
    '''
    if(len(t) == 4):
        t[1].append(t[3])
        t[0] = t[1]
    elif(len(t) == 2):
        t[0] = [t[1]]

def p_atributo(t):
    '''atributo : ID DOSPUNTOS typeDef
    '''
    t[0] = [t[1],t[3],None]

#===================================================================================
def p_assigment(t):
    '''assigment : ID IGUAL expresion PICOMA
                 | ID access IGUAL expresion PICOMA
    '''
    #| ID PUNTO ID IGUAL expresion PICOMA
    if(len(t)==5):
        t[0] = Assignment(t[1], t[3], None,t.lineno(1),t.lexpos(1))
    elif(len(t)==6):
        t[0] = Assignment(t[1], t[4], t[2],t.lineno(1),t.lexpos(1))
    #elif(len(t)==7):
    #    t[0] = Assignment([t[1],t[3]], t[5], None,t.lineno(1),t.lexpos(1))
#================================================================================
def p_function(t):
    '''function : FN ID parametersFunc LLAVEIZQ block LLAVEDER
                | FN ID parametersFunc MENOS MAYORQUE typeDef LLAVEIZQ block LLAVEDER
    '''
    if(len(t)==7):
        t[0] = Function(t[2],t[3],t[5],None,t.lineno(1),t.lexpos(1))
    elif(len(t)==10):
        t[0] = Function(t[2],t[3],t[8],t[6],t.lineno(1),t.lexpos(1))
def p_parametersFunc(t):
    '''parametersFunc   : PARIZQ parameters PARDER
                        | PARIZQ PARDER
    '''
    if(len(t) == 4):
        t[0] = t[2]
    elif(len(t) == 3):
        t[0] = []
def p_parameters(t):
    '''parameters   : parameters COMA parameter
                    | parameter
    '''
    if(len(t) == 4):
        t[1].append(t[3])
        t[0] = t[1]
    elif(len(t) == 2):
        t[0] = [t[1]]
def p_parameter(t):
    '''parameter    : ID DOSPUNTOS typeDef
                    | ID DOSPUNTOS POINTER MUT PARIZQ typeDef PARDER
                    | ID DOSPUNTOS POINTER MUT DECVEC MENORQUE typeDef MAYORQUE
    '''
    if len(t) == 4:
        t[0] = Parameter(t[1],t[3],t.lineno(1),t.lexpos(1),False,False,False)
    elif len(t) == 8:
        t[0] = Parameter(t[1],t[6],t.lineno(1),t.lexpos(1),True,True,False)
    elif len(t) == 9:
        t[0] = Parameter(t[1],t[6],t.lineno(1),t.lexpos(1),True,False,True)
#================================================================================
def p_block(t):
    '''block    : ins
                | 
    '''
    if(len(t) == 2):
        t[0] = t[1]
    else:
        t[0] = []
#================================================================================
def p_callFuncSt(t):
    '''callFuncSt   : ID parametersCallFunc PICOMA
    '''
    t[0] = CallFuncSt(t[1],t[2],t.lineno(1),t.lexpos(1))
def p_parametersCallFunc(t):
    '''parametersCallFunc   :  PARIZQ listValues PARDER
                            |  PARIZQ PARDER
    '''
    if(len(t) == 4):
        t[0] = t[2]
    elif(len(t) == 1):
        t[0] = []
#===================================================================================
def p_listValues(t):
    '''listValues   : listValues COMA expresion
                    | expresion
    '''
    if(len(t) == 4):
        t[1].append(t[3])
        t[0] = t[1]
    elif(len(t) == 2):
        t[0] = [t[1]]
def p_coincidencia(t):
    '''
        coincidencia : coincidencia PALO expresion
                     | expresion
    '''
    if(len(t) == 4):
        t[1].append(t[3])
        t[0] = t[1]
    elif(len(t) == 2):
        t[0] = [t[1]]

#================================================================================
def p_whileSt(t):
    ''' whileSt : RWHILE expresion LLAVEIZQ block LLAVEDER
    '''
    t[0] = While(t[2],t[4],t.lineno(1),t.lexpos(1))
#================================================================================
def p_forSt(t):
    '''forSt : RFOR ID IN expresion PUNTO PUNTO expresion LLAVEIZQ block LLAVEDER
             | RFOR ID IN expresion LLAVEIZQ block LLAVEDER
    '''
    if len(t)==11:
        t[0]= For(t[2],None,t[4],t[7],t[9],t.lineno(1),t.lexpos(1))
    elif len(t)==8:
        t[0]= For(t[2],None,t[4],None,t[6],t.lineno(1),t.lexpos(1))
    #| RFOR ID IN expresion LLAVEIZQ block LLAVEDER
    #| RFOR ID IN ID LLAVEIZQ block LLAVEDER
    #elif len(t)==8:
    #   t[0]= For(t[2],None,t[4],None,t[5])
    #elif len(t)==13:
    #    t[0]= For(t[2],t[4],t[6],t[8],t[10])
#================================================================================
def p_loopSt(t):
    '''loopSt : RLOOP LLAVEIZQ block LLAVEDER
    '''
    t[0] = Loop(t[3],t.lineno(1),t.lexpos(1))
#================================================================================
def p_ifSt(t):
    '''ifSt : RIF expresion LLAVEIZQ block LLAVEDER elseSt
    '''
    t[0] = If(t[2], t[4], t[6],t.lineno(1),t.lexpos(1))
def p_elseSt(t):
    '''elseSt : RELSE LLAVEIZQ block LLAVEDER
              | elseifSt
              |
    '''
    if(len(t)==2):
       t[0] = t[1]
    elif(len(t)==5):
        t[0] = t[3]
def p_esleifSt(t):
    '''elseifSt : RELSE RIF expresion LLAVEIZQ block LLAVEDER elseSt
                |
    '''
    t[0] = If(t[3], t[5], t[7],t.lineno(1),t.lexpos(1))
#================================================================================
def p_matchSt(t):
    '''matchSt : RMATCH expresion LLAVEIZQ options LLAVEDER
    '''
    t[0] = Match(t[2],t[4],t.lineno(1),t.lexpos(1))
def p_options(t):
    '''options : options option
               | option
    '''
    if(len(t)==3):
        t[1].append(t[2])
        t[0] = t[1]
    elif(len(t)==2):
        t[0] = [t[1]]
def p_option(t):
    '''option : coincidencia IGUAL MAYORQUE in COMA
              | coincidencia IGUAL MAYORQUE LLAVEIZQ block LLAVEDER
              | GUIONBAJO IGUAL MAYORQUE in COMA
              | GUIONBAJO IGUAL MAYORQUE LLAVEIZQ block LLAVEDER
              | expresion IGUAL MAYORQUE in COMA
              | expresion IGUAL MAYORQUE LLAVEIZQ block LLAVEDER
    '''
    if(len(t)==6):
        if(t[1] == "_"):
            t[0] = [t[4]]
        else:
            #print(t[1])
            t[0] = [t[1],t[4]]
    elif(len(t)==7):
        t[0] = [t[1],t[5]]
#================================================================================
def p_transSen(t):
    '''trans : BREAK PICOMA
             | CONTINUE PICOMA
             | RETURN expresion PICOMA
             '''
    if   t[1] == 'break' :      t[0] =     transSen(trasnferSen.BREAK,"")
    elif t[1] == 'continue' :   t[0] =     transSen(trasnferSen.CONTINUE,"")
    elif t[1] == 'return' :     t[0] =     transSen(trasnferSen.RETURN, t[2])
#================================================================================
def p_typeDef(t):
    '''typeDef  : RSTRING
                | I64
                | F64
                | BOOL
                | CHAR
                | POINTER PSTRING
                | USIZE
                | DECVEC MENORQUE typeDef MAYORQUE
                | CORIZQ typeDef PICOMA expresion CORDER
                | ID
    '''
    if   t[1] == 'String' :                 t[0] = typeExpression.STRING
    elif t[1] == 'i64' :                    t[0] = typeExpression.INTEGER
    elif t[1] == 'f64' :                    t[0] = typeExpression.FLOAT
    elif t[1] == 'char' :                   t[0] = typeExpression.CHAR
    elif t[1] == 'bool' :                   t[0] = typeExpression.BOOL
    elif t[1] == 'usize' :                  t[0] = typeExpression.USIZE
    elif t[1] == '[' :                      t[0] = typeExpression.ARRAY
    elif t[1] == 'Vec' :                    t[0] = typeExpression.VECTOR
    elif t[1] == '&':                       t[0] = typeExpression.PSTRING
    else:
        t[0] = [typeExpression.STRUCT, t[1]]
#================================================================================

def p_expresion_binaria(t):
    '''expresion : expresion MAS expresion
                | expresion MENOS expresion
                | expresion POR expresion
                | expresion DIVIDIDO expresion
                | expresion MODULO expresion
                | expresion MAYORQUE expresion
                | expresion MENORQUE expresion
                | expresion MAYORIGUAL expresion
                | expresion MENORIGUAL expresion
                | expresion IGUALIGUAL expresion
                | expresion DIFERENCIA expresion
                | expresion AND expresion
                | expresion OR expresion
    '''
    if   t[2] == '+': t[0] = Arithmetic(t[1], t[3], arithmeticOperation.PLUS, t.lineno(1), t.lexpos(1), None)
    elif t[2] == '-': t[0] = Arithmetic(t[1], t[3], arithmeticOperation.MINUS, t.lineno(1), t.lexpos(1), None)
    elif t[2] == '*': t[0] = Arithmetic(t[1], t[3], arithmeticOperation.MULTIPLY, t.lineno(1), t.lexpos(1), None)
    elif t[2] == '/': t[0] = Arithmetic(t[1], t[3], arithmeticOperation.DIV, t.lineno(1), t.lexpos(1), None)
    elif t[2] == '%': t[0] = Arithmetic(t[1], t[3], arithmeticOperation.MODULE, t.lineno(1), t.lexpos(1), None)
    elif t[2] == '>': t[0] = Relational(t[1],t[3], relationalOperation.MAYOR, t.lineno(1), t.lexpos(1))
    elif t[2] == '<': t[0] = Relational(t[1],t[3], relationalOperation.MENOR, t.lineno(1), t.lexpos(1))
    elif t[2] == '>=': t[0] = Relational(t[1],t[3], relationalOperation.MAYORIGUAL, t.lineno(1), t.lexpos(1))
    elif t[2] == '<=': t[0] = Relational(t[1],t[3], relationalOperation.MENORIGUAL, t.lineno(1), t.lexpos(1))
    elif t[2] == '==': t[0] = Relational(t[1],t[3], relationalOperation.IGUALIGUAL, t.lineno(1), t.lexpos(1))
    elif t[2] == '!=': t[0] = Relational(t[1],t[3], relationalOperation.DIFERENTE, t.lineno(1), t.lexpos(1))
    elif t[2] == '&&': t[0] = Logic(t[1],t[3], logicOperation.AND, t.lineno(1), t.lexpos(1))
    elif t[2] == '||': t[0] = Logic(t[1],t[3], logicOperation.OR, t.lineno(1), t.lexpos(1))
#elif t[2] == '^': t[0] = Arithmetic(t[1], t[3], arithmeticOperation.POTENCY)
#====================================================
def p_expresion_potencia(t):
    '''expresion : I64 DOSPUNTOS DOSPUNTOS RPOW PARIZQ expresion COMA expresion PARDER
                 | F64 DOSPUNTOS DOSPUNTOS RPOWF PARIZQ expresion COMA expresion PARDER
    '''
    if t[1] == 'i64' and t[4] == 'pow':
        t[0] = Arithmetic(t[6], t[8], arithmeticOperation.POTENCY, t.lineno(1), t.lexpos(1), "i64")
    elif t[1] == 'f64' and t[4] == 'powf':
        t[0] = Arithmetic(t[6], t[8], arithmeticOperation.POTENCY, t.lineno(1), t.lexpos(1), "f64")
        
#====================================================
def p_expresion_unaria(t):
    '''expresion : MENOS    expresion %prec UMENOS
                 | NOT      expresion
                 | expresion PUNTO SQRT PARIZQ PARDER
                 | expresion PUNTO ABS PARIZQ PARDER
                 | expresion PUNTO TO_STRING PARIZQ PARDER
                 | expresion PUNTO TO_OWNED PARIZQ PARDER
                 | expresion PUNTO CLONE PARIZQ PARDER
                 | expresion PUNTO CHARS PARIZQ PARDER
                 | expresion PUNTO RLEN PARIZQ PARDER
                 | expresion PUNTO CONTAINS PARIZQ POINTER expresion PARDER
                 | expresion PUNTO CAPACITY PARIZQ PARDER
                 | expresion PUNTO REMOVE PARIZQ expresion PARDER
                 | expresion PUNTO ID
                 | expresion AS typeDef
                 '''
    #| expresion PUNTO ID
    #| LOG10    PARIZQ expresion PARDER
    #| SIN      PARIZQ expresion PARDER
    #| COS      PARIZQ expresion PARDER
    #| TAN      PARIZQ expresion PARDER
    #| TRUNC    PARIZQ typeDef COMA expresion PARDER
    #| PARSE    PARIZQ typeDef COMA expresion PARDER
    #| FLOAT    PARIZQ expresion PARDER
    #| RSTRING  PARIZQ expresion PARDER
    #| TYPEOF   PARIZQ expresion PARDER 
    #| LENGTH   PARIZQ expresion PARDER
    #| UPPER    PARIZQ expresion PARDER
    #| LOWER    PARIZQ expresion PARDER
    if t[1]   == '-':           t[0] = Arithmetic(t[2], None, arithmeticOperation.NEGATIVE, t.lineno(1), t.lexpos(1), None)
    #""" elif t[1] == 'log10':       t[0] = Native(t[3],None,nativeOperation.LOG10) 
    #elif t[1] == 'sin':         t[0] = Native(t[3],None,nativeOperation.SIN)
    #elif t[1] == 'cos':         t[0] = Native(t[3],None,nativeOperation.COS)
    #elif t[1] == 'tan':         t[0] = Native(t[3],None,nativeOperation.TAN)
    #elif t[1] == 'sqrt':        t[0] = Native(t[3],None,nativeOperation.SQRT)
    elif t[1] == '!':            t[0] = Logic(t[2], None, logicOperation.NOT, t.lineno(1), t.lexpos(1))
    #elif t[1] == 'parse':       t[0] = NativeFunction(t[5], t[3], nativeFunction.PARSE)
    #elif t[1] == 'trunc':       t[0] = NativeFunction(t[5], t[3], nativeFunction.TRUNC)  
    #elif t[1] == 'float':       t[0] = NativeFunction(t[3], None, nativeFunction.FLOAT)
    elif t[2] == 'as':           t[0] = Casteo(t[1], t[3], t.lineno(1), t.lexpos(1))
    elif t[3] == 'to_string':    t[0] = NativeFunction(t[1], None, None, nativeFunction.TO_STRING, t.lineno(1), t.lexpos(1))
    elif t[3] == 'to_owned':     t[0] = NativeFunction(t[1], None, None, nativeFunction.TO_OWNED, t.lineno(1), t.lexpos(1))
    elif t[3] == 'sqrt':         t[0] = NativeFunction(t[1], None, None, nativeFunction.SQRT, t.lineno(1), t.lexpos(1))
    elif t[3] == 'abs':          t[0] = NativeFunction(t[1], None, None, nativeFunction.ABS, t.lineno(1), t.lexpos(1))
    elif t[3] == 'clone':        t[0] = NativeFunction(t[1], None, None, nativeFunction.CLONE, t.lineno(1), t.lexpos(1))
    elif t[3] == 'chars':        t[0] = NativeFunction(t[1], None, None, nativeFunction.CHARS, t.lineno(1), t.lexpos(1))
    elif t[3] == 'len':          t[0] = NativeFunction(t[1], None, None, nativeFunction.LEN, t.lineno(1), t.lexpos(1))
    elif t[3] == 'contains':     t[0] = NativeFunction(t[1], t[6], None, nativeFunction.CONTAINS, t.lineno(1), t.lexpos(1))
    elif t[3] == 'capacity':     t[0] = NativeFunction(t[1], None, None, nativeFunction.CAPACITY, t.lineno(1), t.lexpos(1))
    elif t[3] == 'remove':       t[0] = Remove(t[1], t[5], t.lineno(1), t.lexpos(1))
    else:
        t[0] = StructAccess(t[1],t[3],t.lineno(1),t.lexpos(1))
    #else:
    #   print(type(t[2]))
    #elif t[3] == 'push':         t[0] = NativeFunction(t[1], t[5], None, nativeFunction.PUSH, t.lineno(1), t.lexpos(1))
    #elif t[1] == 'typeof':      t[0] = NativeFunction(t[3], None, nativeFunction.TYPEOF)
    #elif t[1] == 'length':      t[0] = NativeFunction(t[3], None, nativeFunction.LENGTH)
    #elif t[1] == 'uppercase':   t[0] = NativeFunction(t[3], None, nativeFunction.UPPER)
    #elif t[1] == 'lowercase':   t[0] = NativeFunction(t[3], None, nativeFunction.LOWER) """
    #else:                   t[0] = t[1]   | listValues 
#====================================================
def p_expresion_variable(t):
    '''expresion : ID access'''
    #if len(t)==2:
    #    t[0] = VariableCall(t[1])
    if(t[2]==None):
        t[0] = VariableCall(t[1], t.lineno(1), t.lexpos(1))
    elif(isinstance(t[2],list)):
        t[0] = ArrayAccess(t[1], t[2], t.lineno(1), t.lexpos(1))
    #else:
    #    t[0] = StructAccess(t[1],t[2],t.lineno(1),t.lexpos(1))
def p_access(t):
    '''access : access CORIZQ expresion CORDER
              | CORIZQ expresion CORDER
              | '''
    #| PUNTO ID
    if len(t)==1:
        t[0] = None
    elif(len(t) == 5):
        t[1].append(t[3])
        t[0] = t[1]
    elif(len(t) == 4):
        t[0] = [t[2]]
    elif(len(t) == 3):
        t[0] = t[2]

def p_structDec(t):
    '''expresion : ID LLAVEIZQ structDecBody LLAVEDER
    '''
    t[0] = StructDec([t[1],t[3]],t.lineno(1),t.lexpos(1))
def p_structDecBody(t):
    '''structDecBody : structDecBody COMA atributoDec
                     | atributoDec
    '''
    if(len(t) == 4):
        t[1].append(t[3])
        t[0] = t[1]
    elif(len(t) == 2):
        t[0] = [t[1]]

def p_atributoDec(t):
    '''atributoDec : ID DOSPUNTOS expresion
    '''
    t[0] = [t[1],t[3]]
#def p_expresion_StructAccess(t):
#    '''expresion : ID PUNTO ID
#    '''
#    t[0] = StructAccess(t[1],t[3],t.lineno(1),t.lexpos(1))
#====================================================
#def p_exresion_struct(t):
#    'expresion : structDec'
#    t[0] = StructDec(t[1],t.lineno(1),t.lexpos(1))
#====================================================
def p_withpoint(t):
    '''withpointSt : expresion PUNTO RPUSH PARIZQ expresion PARDER PICOMA
                   | expresion PUNTO ID IGUAL expresion PICOMA
                   | expresion PUNTO INSERT PARIZQ expresion COMA expresion PARDER PICOMA
    '''
    if(t[3]=='push'):
        t[0] = Push(t[1], t[5], t.lineno(1), t.lexpos(1))
    elif(t[3]=='insert'):
        t[0] = Insert(t[1], t[5], t[7] ,t.lineno(1), t.lexpos(1))
    else:
        t[0] = Assignment([t[1],t[3]], t[5], None,t.lineno(1),t.lexpos(1))

#====================================================
#def p_exresion_struct(t):
    #'''expresion: structDec'''
    #t[0] = StructDec(t[1],t.lineno(1),t.lexpos(1))

#====================================================
def p_expresion_agrupacion(t):
    '''expresion : PARIZQ expresion PARDER'''
    t[0] = t[2]
#====================================================
#STRING = 0
def p_expresion_cadena(t):
    '''expresion    : CADENA'''
    t[0] = Primitive(t[1],typeExpression.PSTRING)
#====================================================
#INTEGER = 1
def p_expresion_entero(t):
    '''expresion    : ENTERO'''
    t[0] = Primitive(t[1],typeExpression.INTEGER)
#====================================================
#FLOAT = 2
def p_expresion_decimal(t):
    '''expresion    : DECIMAL'''
    t[0] = Primitive(t[1],typeExpression.FLOAT)
#====================================================
#BOOL = 3
def p_expresion_booleanof(t):
    '''expresion    : TRUE'''
    t[0] = Primitive(True,typeExpression.BOOL)
def p_expresion_booleanot(t):
    '''expresion    : FALSE'''
    t[0] = Primitive(False,typeExpression.BOOL)
#====================================================
#CHAR = 4
def p_expresion_caracter(t):
    '''expresion    : CARACTER'''
    t[0] = Primitive(t[1],typeExpression.CHAR)
#====================================================
    #| ID listArray
    #elif len(t)==3:
    #    t[0] = t[2]
#====================================================
def p_expresion_returnf(t):
    '''expresion : ID parametersCallFunc
    '''
    t[0] = CallFuncSt(t[1],t[2],t.lineno(1),t.lexpos(1))
#====================================================
#""" def p_assig_array(t):
#    '''assig_array : ID listArrayA IGUAL expresion PICOMA'''
#    t[0] = AssigArray(t[1], t[4], t[2])
#def p_list_array(t):
#    '''listArray : listArray CORIZQ expresion CORDER
#                 | CORIZQ expresion CORDER'''
#    if len(t)==5:
#        t[0] = ArrayCall(t[1],t[3])
#    elif len(t)==4:
#        tempVar= VariableCall(t[-1])
#        t[0] = ArrayCall(tempVar,t[2])
def p_exp_vector(t):
    '''expresion : RVEC NOT CORIZQ listValues CORDER
                 | RVEC NOT CORIZQ expresion PICOMA expresion CORDER
                 | DECVEC DOSPUNTOS DOSPUNTOS NEW PARIZQ PARDER
                 | DECVEC DOSPUNTOS DOSPUNTOS WCAPACITY PARIZQ expresion PARDER
                 '''
    if(len(t)==6):
        t[0] = Vector(None,None,t[4],t.lineno(1), t.lexpos(1))
    elif(len(t)==8):
        if(t[4]=='with_capacity'):
            t[0] = Vector(None,t[6],None,t.lineno(1), t.lexpos(1))
        else:
            t[0] = Vector(t[4],t[6],None,t.lineno(1), t.lexpos(1))
    elif(len(t)==7):
        t[0] = Vector(None,None,None,t.lineno(1), t.lexpos(1))
    
    
def p_exp_array(t):
    'expresion : CORIZQ listValues CORDER'
    t[0] = Array(None,None,t[2],t.lineno(1), t.lexpos(1))
def p_exp_array_can(t):
    '''expresion : CORIZQ expresion PICOMA expresion CORDER'''
    t[0] = Array(t[2],t[4],None,t.lineno(1), t.lexpos(1))
#def p_list_arrayA(t):
#    '''listArrayA : listArrayA CORIZQ expresion CORDER
#                 | CORIZQ expresion CORDER'''
#    if len(t)==5:
#        t[0] = ArrayCallAsig(t[1],t[3])
#    elif len(t)==4:
#        tempVar= VariableCall(t[-1])
#        t[0] = ArrayCallAsig(tempVar,t[2]) """   
# ===================================================   
def p_error(t):
    #global Salida
    #Salida.append("Error sintáctico en la linea "+t.lineno+" '%s'\n" % t.value)
    ruta = "Salida.txt"
    archivo = open(ruta, "a")
    archivo.write("Error sintáctico: en la linea "+str(t.lineno)+" con '%s'\n" % t.value)
    archivo.close()
    #archivo = open("Errores/Errores.txt", "a")
    #archivo.write("Error sintáctico: en la linea "+str(t.lineno)+" con '%s'\n" % t.value)
    #archivo.close()
    Environment.saveError("Error sintáctico: con "+str(t.value), 'Global', t.lineno, t.lexpos)

import ply.yacc as yacc
parser = yacc.yacc()
