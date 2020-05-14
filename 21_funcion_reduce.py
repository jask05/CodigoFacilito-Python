#encoding: utf-8 

print "\n"
print "+ FUNCIÓN REDUCE \n"
print "++ Reducir una lista a un solo elemento."
print "++ Recorre y junta elementos de par en par."
print "\n"

s = ("H", "o", "l", "a", "_", "m", "u", "n", "d", "o")
l = [1,2,3,4,5]

def concatenar(a,b):
	return a+b

def suma(a,b):
	return a+b

sr = reduce(concatenar,s)
sr2 = reduce(suma, l)

print type(sr)
print sr

print type(sr2)
print sr2