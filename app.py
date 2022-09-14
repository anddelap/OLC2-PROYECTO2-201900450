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
        env.simbolos=[]
        env.errores=[]
        codigo = request.form["entrada"]
        g.codigo=codigo
        archivo = open("Salida.txt", "w")
        archivo.write("")
        archivo.close()
        archivo = open("Errores/Errores.txt", "w")
        archivo.write("")
        archivo.close()
        #Entra al analisis
        gramatica.parser.parse(codigo)
        #Obtiene las Salidas hacia la Salida General
        archivo = open("Salida.txt",'r')
        Salida = archivo.read()
        g.salida = Salida
        #archivo.close()
        #archivo = open("Errores/Errores.txt", "r")
        #errores = archivo.readlines()
        #env.errores = errs
        #print(env.errs)
        global errs
        errs = env.errores
        global simbolos
        simbolos = env.simbolos
        #global errs
        #errs = tuple(errores)
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
    
@app.route('/about-me')
def AboutMe():
    #simbolos = tuple(env.simbolos)
    #global errs
    return render_template("about-me.html")

if __name__ == '__main__':
    app.run('0.0.0.0',5000, debug=True)