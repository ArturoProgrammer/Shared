# !/usr/bin/python3.5
# -*- coding: utf-8 -*-

"""
Funciones:
-Crear un nuevo repositorio local : create_repository
-Eliminar un repositorio existente : delete_repository
-Compartir un repositorio local : share_repository
-Empaquetar un repositorio local : pack_repository
"""

import account_props
import os
import sys
import subprocess
import shutil
from Tkinter import *
import time
import funtionsFALL


def adviceMessage (message):
	mWindow = Tk()
	mWindow.title("Advertencia")
	label = Label(mWindow, text=message)
	button = Button(mWindow, text="Aceptar", command=sys.exit())

	button.pack()
	label.pack()
	mWindow.mainloop()


# Funcion publica
def create_repository (proj_licence , proj_version, proj_name, proj_lang, GUI=True):
	if GUI == True:
		adviceMessage("todo ha salido bien y deacuerdo a lo planeado")
	elif GUI == False:
		print "CREANDO NUEVO REPOSITORIO"
	#print(account_props.getUsername())						# Obtiene el nombre del usuario

	if not os.path.exists("Projects/"):
		os.mkdir("Projects")

	if proj_licence == "" or proj_licence == None:
		proj_licence = "Apache License 2.0" # En caso de no pasar este argumento, se tomara por default la licencia Apache License 2.0

	"""Funcion para crear los directorios"""
	os.chdir("Projects/")

	if os.path.exists(proj_name + "/"):
		print "ADVERTENCIA: ya existe un directorio con ese mismo nombre. Reemplazar=r Continuar sin reemplazar=c"
		opt = raw_input("[R/c]: ").lower()
		if opt == "r":
			shutil.rmtree(proj_name + "/")	# Se elimina directorio viejo
			os.mkdir(proj_name + "/")	# Se crea el nuevo directorio
			os.chdir(proj_name + '/')
		elif opt == "c":
			os.mkdir(proj_name + "1/") 	# Nombre con diferenciador
			os.chdir(proj_name + '1/')
	else:
		os.mkdir(proj_name)
		os.chdir(proj_name + '/')

	# Se crea el directorio raiz
	os.mkdir("Resources")
	os.mkdir("Icons")
	os.mkdir("Bin")
	if GUI == True:
		adviceMessage("Repositorio creado correctamente!")
	elif GUI == False:
		print "Repositorio creado correctamente!"

	"""Funcion para crear las master key lists"""

	ckey = funtionsFALL.criptoKeyGenerator()

	manifest_template = """
{
	"Author" : {app_author}
	"Aplication name" : {app_name}
	"Test Command" : {test_command}
	"Creation Date" : {origin_date}
	"Version" : {app_version}
	"Licences" : {app_licence}
	"CriptoKey" : {app_key}
}
	""".format(app_author = "Fernando", app_name = proj_name, test_command = proj_name + '-execute', origin_date = time.strftime('%x'), app_version = proj_version, app_licence = proj_licence, app_key = ckey)
	writeJSONtemplate = open("AppManifest.json", "w")
	writeJSONtemplate.write(manifest_template)
	writeJSONtemplate.close()
	if GUI == True:
		adviceMessage("Archivo AppManifest.json creado con exito!")
	elif GUI == False:
		print "Archivo AppManifest.json creado con exito!"