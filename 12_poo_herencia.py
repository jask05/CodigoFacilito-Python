#encoding: utf-8 

print "+ HERENCIAS \n"
print " ++ Super clase > sub clase."
print "\n ---------- \n"

class Humano:
	
	def __init__(self, edad):
		# ATRIBUTO
		# Cualquier instancia que se haga de la clase Humano o cualquier objeto que se cree
		# va a tener una edad de X. Si quiero cambiar esa edad para una personalizada hay 
		# que agregar un nuevo argumento.
		self.edad = edad

	# Si no se pone self en el método python no puede enviar
	# este método cuando se instancie.
	def hablar(self, mensaje):
		print mensaje
		# print self.edad

# El método INIT se hereda al estar referido en humanos
class IngSistemas(Humano):

	# Tiene + importancia que el init de Humano
	# Sobreescribir métodos
	def __init__(self):
		print "Hola IngSistemas!"

	def programar(self,lenguaje):
		print "Voy a programar en ", lenguaje

class LicDerecho(Humano):

	def estudiarCaso(self, de):
		print "Voy a estudar el caso de ", de


pedro = IngSistemas()
raul = LicDerecho(22)

pedro.hablar("Hola")
raul.hablar("Hola Pedro!")

pedro.programar("Python")
raul.estudiarCaso("Pedro")

# print "Soy Pedro y tengo ", pedro.edad, " años."
print "Soy Pedro y tengo ", raul.edad, " años."