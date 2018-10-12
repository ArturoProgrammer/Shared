# !/usr/bin/python3.5
# -*- coding: utf-8 -*-

from Tkinter import *
from ModuleLocals import main_subModule as sharedmod
import sys

"""
Archivo principal del plugin
"""

name = raw_input("NOMBRE DEL PROYECTO: ")			# Nombre del repositorio
if name == "":
	sys.exit()
lang = raw_input("LENGUAJE: ")						# Lenguaje base del proyecto
version = raw_input("VERSION: ")
license = raw_input("LICENCIA: ")

sharedmod.create_repository(license ,version, name, lang, GUI=False) 

# ---------------------------------INTERFAZ GRAFICA DEL USUARIO---------------------------------

def onCreate ():
	app = Tk()
	app.title("Shared")
	etiqueta = Label(app, text="Hola mundo!!!")
	boton = Button(app, text="OK!!", command="consolelog")

	etiqueta.pack()
	boton.pack()
	app.mainloop()