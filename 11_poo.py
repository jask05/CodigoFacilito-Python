#encoding: utf-8 

print "+ Clases y objetos \n"
print " ++ Objeto: un coche, botella, persona, etc. con características."
print " ++ Características: atributos del objeto."
print " ++ Acciones que puede realizar el objeto: métodos."
print " ++ Objeto: humano. Atributos: ojos, color de piel, etc. Acciones: caminar, dormir, comer."
print " ++ CLASE: plantilla/molde del cual proviene el objeto. Se establecen atributos y métodos del objeto. \n"
print "\n ---------- \n"
print " + CLASE Humano: "
print """\r ++ Este método lo reconoce y cuando se crea un nuevo objeto se ejecuta este método.
\r ++ SELF: se guarda la referencia al objeto que esté creado """
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
		print self.edad

# Estoy creando un objeto/instanciando la clase Humano
pedro = Humano(25)
raul = Humano(21)

pedro.hablar("Hola")
raul.hablar("Hola Pedro!")
print "Soy Pedro y tengo ", pedro.edad, " años."
print "Soy Pedro y tengo ", raul.edad, " años."