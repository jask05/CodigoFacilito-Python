#encoding: utf-8 

print "\n"
print "+ ENCAPSULACIÓN \n"
print "++ Atributos/métodos pueden ser privados o públicos."
print "++ Se limita el acceso desde fuera de la clase."
print "++ Privada/pública: establecido por el nombre o método del atributo" 
print "\r (se inicia con dos guiones bajos __ PERO NO TERMINAR si no sería un método especial de Python)"

class Prueba(object):
	
	def __init__(self):
		self.__privado 	= "Soy privado"
		self.privado 	= "Soy público"

	# Solo se utilizan dentro de la misma clase
	def __metodoPrivado(self):
		print "Soy un método privado!"

	def metodoPublico(self):
		print "Soy un método público!"

	# Acceso a un método privado
	# Método auxiliar
	def getPrivado(self):
		return self.__privado

	def setPrivado(self, valor):
		self.__privado = self.__metodoPrivado()

print "\n --------------- \n "

objeto = Prueba()

print "+ objeto.privado"
print objeto.privado

print " --------------- \n "

print "+ objeto.setPrivado(\"Tengo un nuevo valor!\")"
objeto.setPrivado("Tengo un nuevo valor!")

print "\n"

print "+ objeto.getPrivado()"
print objeto.getPrivado()

print " --------------- \n "

print "+ objeto.metodoPublico(): "
print objeto.metodoPublico()

print " --------------- \n "

# print "+ objeto.__metodoPrivado()"
# objeto.__metodoPrivado()

print " --------------- \n "