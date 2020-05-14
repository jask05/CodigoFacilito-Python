#encoding: utf-8 

print "\n"
print "+ EXCEPCIONES\n"
print "++ Se generan cuando ocurre un error cuando se ejecuta el programa."
print "\n"

print "Bienvenido"

n = "fadf"

try:
	#print l
	print n/5
# except:
except TypeError:
	print "Error tipo de dato!"
except NameError:
	print "Variable no existe"
except ZeroDivisionError:
	print "No se puede dividir entre 0."
else:
	print "No hubo error!"
finally:
	print "Si ocurrió un error o no, se ejecuta!"

print "Adiós!"

print "--------------- \n"

class UnoError(Exception):
	def __init__(self, valor):
		self.valorError = valor

	def __str__(self):
		print "_No se puede difivir entre uno el número: ", self.valorError

d = 5
n = 1
try:
	if n == 1:
		raise UnoError(d)
except UnoError:
	print "Se ha producido un error!"

if n==1:
	raise UnoError(d)

