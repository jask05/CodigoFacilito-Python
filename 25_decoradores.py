#encoding: utf-8 

print "\n"
print "+ DECORADORES\n"
print "++ Función que recibe una función y regresa una función 'decorada'."
print "\n"

# logeado = False
logeado = True
usuario = "CodifoFacilito"

def admin(f):
	def comprobar(*args,**kwargs):
		if logeado:
			f(*args,**kwargs)
		else:
			print "No tiene permisos para ejecutar", f.__name__

	return comprobar

def decorador(funcion):
	def funcionDecorada(*args,**kwargs):
		print "Funcion ejecutada ", funcion.__name__
		funcion(*args,**kwargs)

	return funcionDecorada

def resta(n,m):
	print n-m

resta(5,3)

# Decorando
# decorador(resta)(3,5)
decorada = decorador(resta)
decorada(3,5)

print "###### Resta2 \n"
# Simplificar
@decorador
def resta2(n,m):
	print n-m

resta2(3,5)

print "###### Exponente \n"
@admin
@decorador
def exponente(n,m):
	print n*+m

exponente(3,5)