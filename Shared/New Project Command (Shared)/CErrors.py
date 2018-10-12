#!/usr/bin/python

import sys
import webbrowser
from SFSProjectCommand import *
from BankFunction import *


"""
Modulo creado para lanzar un error en pantalla al momento de ocurrir
una contingencia con algun comando.
"""


"""================ERRORES DE LA TERMINAL============="""

NumError =  ['100', '101', '102', '103', '208', '209', '210', '303', '305', '313', '404', '505'] #Lista errores
Character = ["#", "$", "{", "}", "[", "]", "?", "'", "¿", "/", "%", "°", ] #Lista de caracteres no admitidos

def evaluate(name):
	if name == Character:
		print "\nEl Nombre no es valido"


"""==================================================="""

def console():
	num = 0

	while num == 0:
		com = raw_input(">>> $ ")
		print "*Command in execution: ", com

		if com == "exit":
			sys.exit()
		elif com == "project.new @sudo{admin}":
			print "---Permiso de Administrador requerido---"
			name = raw_input("Ingrese la clave de administrador: ")
			if name == RealAdminName:
				NewProject(name)
			else:
				print "Error210: Error de autenticacion."
		elif com == "repository.deploy":
			pass
		elif com == "OfficialPage.deploy":
			webbrowser.main(www.shared.hol.es, -n)
	else:
		pass

if __name__ == '__main__':
	console()