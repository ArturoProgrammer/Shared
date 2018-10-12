import base64
import random


"""
Metodo de llaves de encriptacion n.1
"""

#Arreglo con las llaves criptograficas aceptadas por el software
CriptoKeys = []

def stringGate (code, let):
	if let == True:
		return code

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



def create ():
	for i in range(1, 9):
		#cvi = int(cv)

		DataIntegerVal = [4554551321564, 3923739124124, 5785613546845, 7974814678934, 1002454214010, 9146700547288, 9797210104120]
		yi = random.randint(0, 6)
		dataint = DataIntegerVal[yi]

		DataStringVal = ["f56f54gs485asdfa", "oasd8uasiasf9293", "oansd9823rbkwegf", "basnmafbahjsfk55", "km2wmsf904kks5fa", "886858g8499asd2a", "f9apsdm3wkansdaa", "8s34uit0wio23df9", "kamjsfdiqwjroi2u39874"]
		ys = random.randint(0, 8)

		key = Aleador(IntegerValor(), Base64Valor(str(DataStringVal[ys])), StringValor(), BinaryValor(dataint))
		
		CriptoKeys.insert(i, key)

		keysSelected = CriptoKeys[0:12]
		STRkey = str(keysSelected)

		file = open("MyProjectKey.txt", "w")
		file.write(STRkey)
		file.close()

		return STRkey


if __name__ == '__main__':
	create()