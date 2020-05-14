# -*- coding: utf-8 -*-

print "\n"
print "+ Para saber el tipo de una variable se utiliza la función type( ) \n "

# Comillas simples
cads = 'Texto entre comillas simples'

# Comillas dobles
cadd = "Texto entre comillas dobles"

print type(cads)
print cads
print type(cadd)
print cadd

print "\n ------------------- \n"
print "+ Ahora se trabajará con texto en varias líneas \n"

text1 = "Este texto \n tiene varias \n líneas"
print text1

text2 = "Este texto \t tiene algunas \n \t tabulaciones con \ t"
print text2

print "\n ------------------- \n"
print "+ Si se utilizan las comillas triples se pueden poner en varias líneas \n"

print """Esto iría en la primera
pero tenemos también la segunda
y la tercera"""

print "\n ------------------- \n"

print "+ Repetición y concatenación \n \n"

cad = "Cadena" * 3
print cad

print "\n ------------------- \n"

print "+ Concatenación. Se utiliza el + \n \n"

cad02 = "Cadena1 "
cad03 = "cadena2"

print cad02 + cad03

print "\n ------------------- \n"
print """+ Tipo booleano (True | False). La primera letra siempre mayúscula. 
En caso de 'not' va en minúsculas."""

bT = True
bF = False

bAnd = True and False
bOr = True or False
bNot = not True # se convierte en falso

print bAnd
print bOr
print bNot