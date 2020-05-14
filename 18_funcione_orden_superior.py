#encoding: utf-8 

print "\n"
print "+ FUNCIONES ORDEN SUPERIOR \n"
print "++ El hecho de que los programas se basen en funciones (matemáticas)."

def prueba(f):
	return f() # Al poner los paréntesis se está ejecutando.

def porEnviar():
	return 2+2

print "-------- \n"

print prueba(porEnviar)

print "\n -------- \n"

def seleccion(operacion):

	def suma(n,m):
		return n+m

	def multiplicacion(n,m):
		return n*m
	
	if operacion == "suma":
		return suma
	elif operacion == "multi":
		return multiplicacion

fGuardada = seleccion("suma")
print fGuardada(2,3)

mGuardada = seleccion("multi")
print mGuardada(3,3)