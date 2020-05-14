# -*- coding: utf-8 -*-
print "Tipo INT y tipo Long"
print ""
print "El tipo long almacena más datos pero requiere más memoria en el sistema"
print "---------------------------------"
print "Variable tipo INT e = 5"
e = 5
print "Si quiero que sea de tipo long, se pone una L al final. e = 5L"
e = 5L

real = 0.567
real = 0.56e3

print "Imprimiendo real"
print real

print "--------------------"
a = 26
b = 11.3
c = 5
d = 3.5

# Suma
print a + b

# Resta
print c - a

# Multiplicación
print d * c

# Exponente
print c ** 2

# División
# Tendría que ser 0,19. No genera número real, lo pasa a entero
print c / a
# Para que devuelva a número real, utilizar float
float (c)

# División entera
print c / a

# Módulo
print 7%3