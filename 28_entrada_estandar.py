#encoding: utf-8 

print "\n"
print "+ ENTRADA ESTÁNDAR\n"
print "++ Entradas desde teclado."
print "\n"


try:
	valor = input('Introduce un número: ')
	valor = int(valor)
except:
	print "Eso no es un número"
else:
	print valor