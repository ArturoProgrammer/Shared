#!/usr/bin/python

class Project:
	def __init__ (self):
		#Guarda el registro de ultimo uso
		pass

	def status (self):
		self.activate = True

		return self.activate


def AccessPublic():
	pass

def AccessPrivar():
	pass


class Rep:
	def __init__(self, rep_name, access):
		self.repositoryname = rep_name
		self.typeacces = access

		if self.typeacces == public:
			AccessPublic()
		else:
			AccessPrivate()


	def stop(self):
		"""Detiene el repositorio"""
		pass

	def start(self):
		"""Inicia el repositorio"""
		pass

	def public(self):
		"""Vuelve publico el repositorio"""
		pass

	def private(self):
		"""Vuelve privado el repositorio"""
		pass

	def delete(self):
		"""Borra el repositorio"""
		pass