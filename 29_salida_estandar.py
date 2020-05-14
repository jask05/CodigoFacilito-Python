#encoding: utf-8 

print "\n"
print "+ SALIDA ESTÁNDAR\n"
print "++ ."
print "\n"

print "Uno", 
print "Dos"

print "\n"

print "Tres \n\tCuadro \nCinco"

print "\n"

edad = 19

print "Mi edad es:", edad, "años."

print "\n-----------\n"

print "+ Especificadores"
print """
+ d enteros
+ f reales
+ s cadenas (string)
+ o octal
+ h hexadecimal
"""
print "Mi edad es: %d años y otra %s." %(edad,"cosa")

edad = 5.1234
print "\n+ Poniendo . (punto) seguido de los dígitos que quiero más letra es lo que muesta.\n"
print "Mi edad es: %.4f años." %(edad)

edad = "Dieciueve"
print "Mi edad es: %.4s años." %(edad)

edad = "Dieciueve"
print "\nMi edad es: %20s años y más cosas." %(edad)
print "Mi edad es: %-20s años y más cosas." %(edad)