#encoding: utf-8 

print "\n"
print "+ GENERADORES + ################### VOLVER A REVISAR \n"
print "++ Parecido a compresión de listas."
print "++ No devuelve lista, si no valores de 1 en 1 en los cuales podemos iterar."
print "++ Para cambiar de compresión a generadores, solo hay que modificar los [ por ( ."
print "\n"

l = [1,2,3,-1,4]
print "print l: ", l


s = ["H", "o", "l", "a"]
print "print s: ", s, "\n"

l2 = [c * num for c in s
				for num in l
					if num > 0]

l3 = (c * num for c in s
				for num in l
					if num > 0)

print l
print "Compresión de listas: ", l2
print type(l3)
print "Imprime H, el primer paso: ", l3.next()
print l3.next()
print l3.next()

print "\n Bucle impreso con for. Utiliza el .next() para ir imprimiendo todo. \n"
for letra in l3:
	print letra

print "\n"
print "+ Generador "

def factorial(n):
	i = 1
	while n > 1:
		i = n*i
		yield i
		n -= 1

for e in factorial(5):
	print e
