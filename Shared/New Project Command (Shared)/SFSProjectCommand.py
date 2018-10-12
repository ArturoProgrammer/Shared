#!/usr/bin/python
#-*- encoding: utf-8 -*-

import os
import sys
import base64
import pcommands
import random
from collections import OrderedDict
import subprocess
from repository import Rep, Project


"""
Modulo creado para al SFS (Shared File System).
Comando:
-NewProject() - Crea un nuevo proyecto.
-ShareProject() - Comparte el proyecto.
-StopProject() - Detiene un proyecto.
-DelProject() - Elimina un proyecto.
-VerifiedProjectCode() - Verifica el codigo de un proyecto.
"""

__author__ = "Armando Arturo"
__version__ = "0.6.5"


VerifiCode = 0

#Arreglo con las llaves criptograficas aceptadas por el software
CriptoKeys = []

#Funcion terminada
def IntegerValor():
	for i in range(1, 9):
		x = random.randint(1, 122299291)
		xs = str(x)

		return xs


#Funcion terminada
def StringValor ():
	letters = ["a","b","c","d","e","f","Q","L"] #Arreglo de strings

	for i in range(1, 9):
		x = random.randint(0, 7)
		xa = letters[x]

		return xa


def Base64Valor(data):
	xb64 = base64.b64encode(data)
	xb64s = str(xb64)

	return xb64s


#Funcion terminada
def BinaryValor (let):
	letx = int(let)
	bincode = bin(letx)


	return bincode


def Aleador (intv, b64v, strv, binv):
	val = intv + b64v
	val2 = val + strv
	val3 = val2 + binv
	final_val = val3

	return final_val #Retorna el valor para el momento en el que se ejecuta la funcion

def create (cv):
	for i in range(1, 9):
		cvi = int(cv)

		# Se agregas valores de tipo entero aleatorios
		DataIntegerVal = [4554551321564, 3923739124124, 5785613546845, 7974814678934, 1002454214010, 9146700547288, 9797210104120, 0000656543430, 4004547579904]
		yi = random.randint(0, 8)
		dataint = DataIntegerVal[yi]

		# Se agregan valores de tipo cadena aleatorios
		DataStringVal = ["f56f54gs485asdfa", "oasd8uasiasf9293", "oansd9823rbkwegf", "basnmafbahjsfk55", "km2wmsf904kks5fa", "886858g8499asd2a", "f9apsdm3wkansdaa", "8s34uit0wio23df9", "kamjsfdiqwjroi2u39874"]
		ys = random.randint(0, 8)
		dataval = DataStringVal[ys]

		# Se une el resultado aleado mas los valores de tipo entero y cadena anteriores
		key = Aleador(IntegerValor(), Base64Valor(dataval), StringValor(), BinaryValor(dataint))
		
		CriptoKeys.insert(i, key)

		keysSelected = CriptoKeys[0:12] 
		STRkey = str(keysSelected)

		file = open("MyProjectKey.txt", "w")
		file.write(STRkey)
		file.close()

		return STRkey

create(02)


#Funcion Privada
def newprojCode_withNamed():
	"""Crea un nuevo proyecto"""
	print "\n======Creando Nuevo Proyecto======\n"

	project_name = raw_input("*Nombre del Proyecto: ").lower()

	if project_name == "":
		cancel()		#Si project_name esta vacio, se cierra directamente la aplicacion

	project_languges = raw_input("*Lenguaje: ").upper()
	pname = project_name

	print "\n==================================\n"

	directory = str("Project_" + pname + "/")

	if os.path.exists("Project"):
		#Nos ubicamos en el directorio raiz del Proyecto
		subprocess.call(["mkdir", directory], shell=True)
		print "Creando el Directorio Raiz..."
	else:
		os.mkdir("Project")
		os.chdir("Project/")
		subprocess.call(["mkdir", directory])
		if not os.path.exists(directory):
			print "LA CARPETA {} NO EXISTE!".format(directory)
			cancel()
		else:
			os.chdir(directory)

	print "Accediendo al Directorio", dirs + "..."
	print "Creando el Directorio de Iconos..."
	subprocess.call("mkdir Iconos", shell=True)		#directorio iconos *
	print "Creando el Directorio de Debug..."
	subprocess.call("mkdir Debug", shell=True)		#directorio debug *
	print "Crenado el Directoiro de Scripts..."
	subprocess.call("mkdir Scripts", shell=True)	#directorio scripts *
	print "Se ha Creado el Proyecto", pname, "con Exito!!"
 
	#Se crea el codigo de verificacion del proyecto
	for i in range(0, 15):
		x = random.randint(1, 10000000)	#Calcula numeros aleatorios de 1 a 10,000,000(10 millones)
		VerifiCode = x					#VerifiCode deja el valor de 0 y toma el valor de x
		CodeValue = bin(VerifiCode)		#Encripta el codigo a binario


	print "Su codigo de proyecto es:", CodeValue + "\n"
	print "Realizando copias de archivos prioritarios a los servidores..."
	pcommands.ServerCopy()
	print "Copias realizadas con exito!!"

#Funcion Privada
def newprojcode(name):
	"""Crea un nuevo proyecto"""
	print "\n======Creando Nuevo Proyecto======\n"
	project_name = name

	if project_name == "" or project_name == None:
		cancel()

	print "*Nombre del Proyecto: ", project_name

	project_languges = raw_input("*Lenguaje: ")
	pname = project_name

	print "\n==================================\n"

	directory = str("Project_" + pname + "/")

	if os.path.exists("Project"):
		#Nos ubicamos en el directorio raiz del Proyecto
		subprocess.call(["mkdir", directory], shell=True)
		print "Creando el Directorio Raiz..."
	else:
		os.mkdir("Project")
		os.chdir("Project/")
		subprocess.call(["mkdir", directory])
		if not os.path.exists(directory):
			print "LA CARPETA {} NO EXISTE!".format(directory)
			cancel()
		else:
			os.chdir(directory)

	dirs = "Project" + pname + "/"
	#Nos ubicamos en el directorio raiz del Proyecto
	os.chdir(dirs)
	print "Accediendo al Directorio", dirs + "..."
	print "Creando el Directorio de Iconos..."
	subprocess.call("mkdir Iconos", shell=True)		#directorio iconos *
	print "Creando el Directorio de Debug..."
	subprocess.call("mkdir Debug", shell=True)		#directorio debug *
	print "Crenado el Directoiro de Scripts..."
	subprocess.call("mkdir Scripts", shell=True)	#directorio scripts *
	print "Creando los Archivos XML del Proyecto...\n"
	subprocess.call("source XMLProjectFiles.sh", shell=True)
	print "Se ha Creado el Proyecto", pname, " con Exito!!"

	#Se crea el codigo de verificacion del proyecto
	for i in range(0, 15):
		x = random.randint(1, 1000000)	#Calcula numeros aleatorios de 1 a 1,000,000(1 millon)
		VerifiCode = x					#VerifiCode deja el valor de 0 y toma el valor de x
		CodeValue = bin(VerifiCode)		#Encripta el codigo a binario

	print "Su codigo de proyecto es:", CodeValue + "\n"
	SaveKey(CodeValue)
	print "Realizando copias de archivos prioritarios a los servidores..."
	pcommands.ServerCopy()
	print "Copias realizadas con exito!!"


"""======================================================================================================================="""


#Funcion Privada
def cancel():
	sys.exit()


# Funcion Publica
def NewProject (projectname):
	"""Crea un nuevo proyecto"""
	if projectname == "" or projectname == None:
		newprojcode(projectname)
	else:
		newprojCode_withNamed()

#Funcion Publica
def ShareProject(projname):
	"""Comparte el proyecto con el sistema de gestion o con otro usuario."""

	if projname == "" or projname == None:
		projname = raw_input("Ingrese el nombre del proyecto: ").lower()
		if projname == "":
			cancel()

	print "Iniciando la verificacion del proyecto " + projname

	if projname == None or projname == "":
		proname = raw_input("Ingrese el nombre del proyecto: ")
	else:
		print "System Error!!"


	comprobante = raw_input("Para continuar con el proceso, por favor, ingrese el codigo del proyecto: ")
	CodeValue = open("project_code.txt", "r")
	if comprobante != CodeValue.read():
		print "Error, el codigo es incorrecto"
	else:
		print "Codigo correcto, compartiendo el proyecto " + pname
	
	CodeValue.close()

#Funcion Publica
def VerifiedProjectCode():
	"""Verifica si el codigo de un proyecto es correcto."""
	codigo_user = raw_input("Ingrese el codigo del proyecto: ")
	StreamVCode = open("project_code.txt", "r")
		
	if codigo_user == StreamVCode:
		print "Codigo correcto."
	else:
		print "El codigo es incorrecto."

	StreamVCode.close()

#Funcion Publica
def DelProject(projname):
	"""Borra un proyecto con la autorizacion del creador del proyecto."""
	if projname == "" or projname == None:
		pjnm = raw_input("\nNombre del proyecto: ").lower()
		if pjnm == "" or pjnm == None:
			cancel()
	else:
		# Proceso para borrar todo el proyecto
		pass

	pa = open("author_name.txt", "r")	#Abre el archivo con el nombre del autor
	pa.read()
	pc = open("project_code.txt", "r")	#Abre el archivo con el codigo de proyecto
	pc.read()

	userpa = raw_input("Ingrese el nombre del autor: ").lower()
	userpc = raw_input("Ingrese el codigo del proyecto: ").lower()

	if userpa == pa and userpc == pc:	#Se verifica que userpa(nombre del autor por el usuario) sea igual a pa(nombre original del autor) y lo mismo con el codigo del proyecto
		print "Iniciando el Borrado del Proyecto..."
		pcommands.del_project()
		print "El proyecto se ha borrado con exito!"
	else:
		print "El codigo del proyecto o el nombre del autor no es correcto."
		cancel()

#Funcion Publica | solucionar errores
def StopProject (paser):
	"""Detiene el desarrollo de un proyecto."""
	ModKeyProjectProtection = Project.status()		#Status del proyecto

	if ModKeyProjectProtection == False:
		repositorio.stopChanges()


#Funcion Publica
def CommandHelp(paser):
	"""Ayuda sobre los comandos de la consola"""

	print "\n===============Commands List===============\n"
		
	print "NewProject - {}".format(NewProject.__doc__)
	print "DelProject - {}".format(DelProject.__doc__)
	print "ShareProject - {}".format(ShareProject.__doc__)
	print "StopProject - {}".format(StopProject.__doc__)
	print "Help - {}".format(CommandHelp.__doc__)
	print "Exit - Finaliza la sesion en la terminal."




"""====INICIA LA CONSTRUCCION DEL MENU===="""
def mainMenu ():
	if __name__ == "__main__":
		salir = False
		mensaje = ""
		
		#Diccionario con los items del menu
		menu = OrderedDict(
				[
					('a', NewProject),
					('b', DelProject),
					('c', ShareProject),
					('d', StopProject),
					('e', CommandHelp)
				]
			)
		
		while not salir:
			print "-" * len(mensaje)
			print mensaje
			
			for opcion, funcion in menu.iteritems():
				mensaje_final = '{}) {}'.format(opcion, funcion.__doc__)	#Se imprime la documentacion de cada funcion
				print mensaje_final


			respuesta = raw_input("\n>>> Shared!:~_$ ").lower()
			salir = respuesta == 'exit'
			
			funcion = menu.get(respuesta, None)
			if funcion:
				funcion(None)
		else:
			txtcom = "Sesion de Comandos__$: [Finished] \n"
			text = "Cerrando la terminal..."
			print "-" * len(txtcom)
			print text
			print txtcom


if __name__ == '__main__':
	mainMenu()