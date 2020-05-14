#encoding: utf-8 

print "\n"
print "+ CLASES DECORADORES\n"
print "++ "
print "\n"

class Decorador(object):
	"""Mi clase decoradora"""
	def __init__(self, funcion):
		self.funcion = funcion

	def __call__(self,*args,**kwargs):
		print "Functión ejecutada ", self.funcion.__name__
		self.funcion(*args,**kwargs)

@Decorador
def resta(n,m):
	print n-m

resta(3,5)

		