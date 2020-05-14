#encoding: utf-8 

print "\n"
print "+ COMPRESIÓN DE LISTAS \n"
print "++ Remplaza a map y filter en la v3."
print "\n"

l = [1,2,3,-1,4]
print "print l: ", l
s = ["H", "o", "l", "a"]
print "print s: ", s, "\n"

l2 = [num for num in l if num > 0]
# Por cada c en la lista s multiplicar c * num, 
# siempre que num esté en l (lista) y el valor 
# de l sea mayor a 0
l3 = [c * num for c in s 
				for num in l
					if num > 0]


print "Ejemplo de multiplicar una letra h*2:", "h"*2
print "lista s: ", s
print "lista l: ", l
print "lista l2 (filtra números > 0): ", l2
print "lista l3: ", l3 

print "\n"
print "+ Más Info \n"
print "- http://mundogeek.net/archivos/2008/03/10/python-programacion-funcional/ \n"
print """l2 = [n ** 2 for n in l]
- Esta expresión se leería como “para cada n en l haz n ** 2”. 
\r Como vemos tenemos primero la expresión que modifica los valores 
\r de la lista original (n ** 2), después el for, el nombre que vamos a 
\r utilizar para referirnos al elemento actual de la lista original, 
\r el in, y la lista sobre la que se itera."""