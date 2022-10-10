import os
from flask import Flask, redirect, render_template, request, g,  Blueprint, send_from_directory
import Analizador.gramatica as gramatica
import Environment.Environment as env
app = Flask(__name__)
errs = ()
simbolos = []

@app.route('/', methods=['GET','POST'])
def index():
    return redirect('/compilar')

@app.route('/compilar', methods=['GET', 'POST'])
def compilar():
    if request.method == 'POST':
        if 'compilar' in request.form:
            env.simbolos=[]
            env.errores=[]
            env.contador=0
            env.contadorL=0
            env.temporales=[]
            codigo = request.form["entrada"]
            g.codigo=codigo
            archivo = open("Salida.txt", "w")
            archivo.write("#include <stdio.h> \nfloat stack[100000]; \nfloat heap[100000]; \nfloat P; \nfloat H;\n")
            archivo.close()
            archivo = open("Errores/Errores.txt", "w")
            archivo.write("")
            archivo.close()
            #Entra al analisis
            gramatica.parser.parse(codigo)
            #Obtiene las Salidas hacia la Salida General
            declaracionTemporales = ""
            for temp in env.temporales:
                if len(temp) == 5:
                    if(temp[0][0]=="t"):
                        declaracionTemporales += temp[0]+","
            declaracionTemporales = "float "+declaracionTemporales
            #declaracionTemporales[len(declaracionTemporales)-1] = ";"
            declaracionTemporales = declaracionTemporales[:len(declaracionTemporales)-1] + ";" + declaracionTemporales[len(declaracionTemporales):]
            #print(declaracionTemporales)
            with open('Salida.txt', 'r') as file:
                # read a list of lines into data
                data = file.readlines()
            #print(data)
            data.append(declaracionTemporales+"\n\n")
            # AQUI PUEDEN IR LAS FUNCIONES
            #data.append("int main(){\n")
            for temp in env.temporales:
                if(isinstance(temp,list)):
                    if(len(temp)==5):
                        if(temp[2]=="" and temp[3]==""):
                            data.append(temp[0]+" = "+temp[1]+";\n")
                        else:
                            data.append(temp[0]+" = "+temp[1]+" "+temp[2]+" "+temp[3]+";\n")
                    elif(len(temp)==2):
                        data.append(temp[0]+" = "+temp[1]+";\n")
                else:
                    data.append(temp+"\n")
            #data.append("return 0;\n")
            #data.append("}")
            # ======== AQUI SE ESCRIBE EN EL ARCHIVO DE SALIDA =========
            with open('Salida.txt', 'w') as file:
                file.writelines(data)
            # ========================================================
            archivo = open("Salida.txt",'r')
            Salida = archivo.read()
            g.salida = Salida
            #archivo.close()
            #archivo = open("Errores/Errores.txt", "r")
            #errores = archivo.readlines()
            #env.errores = errs
            #print(env.errs)
            #print(env.temporales)
            global errs
            errs = env.errores
            global simbolos
            simbolos = env.simbolos
            #global errs
            #errs = tuple(errores)
            return render_template("compilar.html")
        elif 'mirilla' in request.form:
            codigo = request.form["entrada"]
            g.codigo=codigo
            print('mirilla')
            return render_template("compilar.html")
        elif 'bloque' in request.form:
            codigo = request.form["entrada"]
            g.codigo=codigo
            print('bloque')
            return render_template("compilar.html")
    else:
        return render_template("compilar.html")

@app.route('/reportes/tabla-simbolos')
def tablaSimbolos():
    #simbolos = tuple(env.simbolos)
    global errs
    return render_template("Reportes/tabla-simbolos.html", simbolos = simbolos)

@app.route('/reportes/errores')
def Errores():
    #simbolos = tuple(env.simbolos)
    global errs
    return render_template("Reportes/errores.html", errs=errs)

@app.route('/reportes/bd-existente')
def BDExistente():
    #simbolos = tuple(env.simbolos)
    #global errs
    return render_template("Reportes/base-datos-e.html")

@app.route('/reportes/base-datos')
def BaseDatos():
    #simbolos = tuple(env.simbolos)
    #global errs
    return render_template("Reportes/base-datos.html")

@app.route('/reportes/optimizacion')
def RporteOpti():
    #simbolos = tuple(env.simbolos)
    #global errs
    return render_template("Reportes/optimizacion.html")
    
@app.route('/about-me')
def AboutMe():
    #simbolos = tuple(env.simbolos)
    #global errs
    return render_template("about-me.html")

if __name__ == '__main__':
    app.run('0.0.0.0',5000, debug=True)