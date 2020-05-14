# -*- coding: utf-8 -*-

# No es necesario corchetes. Sin corchetes = TUPLAS
# Pero ES IMPORTANTE que los elementos estén separados por comas.
t = 1, True, "Hola"
print t

print "\n ------------ \n"
print "+ Es recomendable poner paréntesis cuando se define. \n"
t2 = (3, False, "Chau")
print t2
print type(t2)

print "\n + Acceder a elementos \n"
print t2[1]

print "\n ------------ \n"

print "+ Diferencias: TUPLA tiene dimensión fija. NO SE PUEDEN AGREGAR NI MODIFICAR LOS ELEMENTOS \n"
print "+ Error que aparecería: TypeError: 'tuple' object does not support item assignment \n"
# t2[1] = True
# print t2[1]