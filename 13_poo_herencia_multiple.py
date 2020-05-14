#encoding: utf-8 

print "+ HERENCIAS múltiple\n"
print " ++ Hereda métodos de varias clases. Amigo (Estudioso) - Ing. Sistemas + Lic. Derecho"
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

	def __init__(self, escuela):
		print "Mi escuela es: ", escuela

	def estudiarCaso(self, de):
		print "Voy a estudar el caso de ", de


class Estudioso(LicDerecho,IngSistemas):
	# pass: "vete, no hay nada que ver aquí."
	# La clase tiene que tener un método por obligación
	# Si no lo tiene, tiene que haber un pass
	# Si se quiere añadir + métodos se quita "pass"
	pass 

pepe = Estudioso("Paules")

pepe.hablar("Hola, soy Pepe!")
pepe.programar("C++")
print "\n +++ Prevalece el init de IngSistemas por el orden en como llamado en la herencia de la clase \"Estudioso\". \n"
pepe.estudiarCaso("Juan")