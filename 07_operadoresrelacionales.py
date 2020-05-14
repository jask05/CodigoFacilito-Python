# -*- coding: utf-8 -*-

print "+ Permiten relacionar y comparar elementos que devuelve un valor. TRUE o FALSE"

print "+ No se puede hacer 'slicing'. d[0:2] no está permitido. No existe índices, por eso no se puede. \n"

v = 4
c = 5

# Operador relacional
r = c == v
print r

c=5
r = c == v

print r

print "\n +++ Diferencias \n"

a2 = 1
b2 = 2

c2 = a2 != b2
print c2

print "\n +++ Comparación \n"

c2 = a2 > b2
d2 = a2 < b2
e2 = a2 <= b2
f2 = a2 >= b2

print c2
print d2
print e2
print f2

print "\n +++ Usado con cadenas "
print "\n 	+ Cuando se comparan cadenas, compara el tamaño de estas letra a letra. \n"

a3 = "Hola"
b3 = "Adiós"
c3 = "Adióss"

print a3 == b3
print a3 != b3
print c3 >= b3

print "\n +++ Usado con listas "

l1 = ["hola", 3, 4]
l2 = ["hola", 3, 5]

l3 = l1 == l2
print l3

l2 = ["hola", 3, 4]
l3 = l1 == l2
print l3