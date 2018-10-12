#!/usr/bin/python

import sys
import subprocess
import webbrowser
import SFSProjectCommand

"""
Comandos para el Shared Files System (SFS).

Comandos:
-InitSoftwareAdmin() - Inicia la administracion del software.
-ServerCopy()
"""

__author__ = "Armando Arturo"
__version__ = "0.0.5"

def InitSoftwareAdmin():
	"""Inicia la administracion del repositorio de un programa."""

	VC = open("project_code.txt")
	ValueSoftCode = raw_input("Ingrese su Codigo Proyecto para continuar: ")
	VC.read()

	if ValueSoftCode != VC:
		print "El codigo es incorrecto."
	else:
		print "Iniciando administracion del programa..."


def del_project():
	"""Borra el proyecto"""
	subprocess.call("source deleteprol.sh", shell=True)	#Falta crear el archivo

def ServerCopy():
	"""Copia los archivos prioritarios del proyecto al servidor"""
	subprocess.call("source ServerCopy.sh", shell=True)	#Falta crear el archivo