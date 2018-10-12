# !/usr/bin/python3.5
# -*- coding: utf-8 -*-

"""
Propiedades del archivo
"""

import json
import os

def getUsername ():
	"""obtiene el nombre de usuario"""
	
	path = "../user/user-settings.json"

	with open(path) as content:
		data = json.load(content)
		for uname in data:
			return uname.get("Username")
