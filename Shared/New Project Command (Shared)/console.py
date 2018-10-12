#!/usr/bin/python


import sys
from SFSProjectCommand import Project as proj
from extrafunctions import TerminalCodeEditor as CodeEditor

__author__ = "Armando Arturo"
__version__ = "0.1"
__licences = "GPL & GNU"



class Terminal(object):
	def start ():
		CommandList = ["exit", "commands.help", "NewProject", "ShareProject", "StopProject", "DelProject", "VerifiedProjectCode", "editor.open"] 


		TextCommandInput = str(raw_input(">>> $ ")) #Caja de Comandos

		#Evaluador de Comandos
		if TextCommandInput == "exit":
			sys.exit()
		elif TextCommandInput == "commands.help":
			print CommandList
		elif TextCommandInput == "NewProject":
			proj.NewProject("")
		elif TextCommandInput == "ShareProject":
			proj.ShareProject()
		elif TextCommandInput == "StopProject":
			proj.StopProject()
		elif TextCommandInput == "DelProject":
			proj.DelProject()
		elif TextCommandInput == "VerifiedProjectCode":
			proj.VerifiedProjectCode()
		elif TextCommandInput == "editor.open":
			CodeEditor()



	i = 0

	#Loop de ejecucion principal
	while i == 0:
		start()
	else:
		break