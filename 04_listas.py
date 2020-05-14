# -*- coding: utf-8 -*-
print """Listas: tipo de colección ordenadas. 
Encerrados entre corchetes y separados por comas.
Ej: l = [2, "tres", True, ["uno", 10]]
"""

num = [1,2,3,4,5,6,7,8,9,10,[11,12,13,14,15]]
l = [2, "tres", True, ["uno", 10]]

print l 

print "\n ------------ \n"

l2 = l[2]
print l2

print "\n ------------ "
print "Accediendo a la lista dentro de otra lista \n"
print l[3][0]

print "\n ------------ "
print "Cambiando contenido \n"

l[1] = 4
print l[1]

print "\n ------------ "
print "Modificación [:] \n"

l3 = l[0:3]
print l3

print """ Poner uno si, uno no. Poner longitud de salto +1. Saltar de 1 si 1 no 
sería 1 +1 = 2."""
l3 = l[0:3:2]
print l3
print "\n Si omito el 3, copia todos los elementos a partir del índice 0."
l3 = l[0::2]
print l3

print "\n ------------ "
print "Cambiar valores a la lista \n"
l[0:2] = ["primer cambio", "txt"]
print l

print "\n Reemplazar dos elementos por uno \n"
l[0:2] = ["segundo cambio"]
print l

print "\n ------------ "
print "Accediendo al revés con índices negativos \n"

print num[-1][-1]
print num[-2]

print "\n ------------ "
print "PRACTICANDO \n"

# En este caso comenzaría por el primer número (0 es el primero)
# hasta 4 números más adelante (NO LA 4ta posición contando 0)
# Por lo que saldría: 1,2,3,4
# Si en vez de 0 se pone 1, sería desde la posición 1 hasta la 4
print num[0:4] 
print num[2:4] 

print "\n - \"Uno si, uno no\" \n"
print num[0:9:2]
print num[0:9:3]

print "\n - \"Todos los elementos pero con saltos\" \n"
print num[0::2]
