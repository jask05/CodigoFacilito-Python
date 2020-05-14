#encoding: utf-8 

print "+ Cadenas y métodos\n"
print " ++ Una cadena o una lista es un objeto (llamados secuencia)"
print "\n ---------- \n"

s = "Hola omundoo"
print "Len(string): ", len(s)

print "\n ------------ \n "
print "++ Cuenta el nº de veces que se encuentra/repite la cadena entre paréntesis."
print "++ CADENA.count(valor, [inicio], [fin])"
print "++ inicio: dónde empieza a buscar (comienza por 0)"
print "++ fin: dónde termina a buscar (lenght -1)"
print " O mayúscula:  ", s.count("O")
print " o minúscula:  ", s.count("o")
print " o minúscula:  ", s.count("o", 0, 3)
print " o minúscula:  ", s.count("o", 5) # Hasta el fin de la cadena

print "\n ------------ \n "
print "++ Lower y Upper."
print "++ Convierte a minúsculas o mayúsculas."
s = "Hola mundo, esto es una prueba."
print s.lower()
print s.upper()

print "\n ------------ \n "
print "++ Replace"
print "++ Parámetro opcional repetición. Cuántas veces quiero que se ejecute"
print s.replace("o", "[X]")
print s.replace("o", "[X]", 1)

print "\n ------------ \n "
print "++ Split - CADENA.split(separador, [maxsplit])"
print "++ Divir letras por separados"
s = "Hola mundo"
print s.split("o")
print s.split("o", 1)
print "Separa cuando encuentre espacios en blanco: ", s.split()

print "\n ------------ \n "
print "++ Find - CADENA.find(valor, [inicio], [fin])"
print "++ Bucar dentro de una cadena"
s = "Hola mundo, esto es una prueba!"
print "El índice/ubicación de la letra a del string \"", s, "\" es: ", s.find("a")
print "Búsqueda de atrás para adelante: ", s.rfind("a")

print "\n ------------ \n "
print "++ Join - CADENA.join(secuencia)"
print "++ Une listas o tuplas. Devuelve cadena."
s = ";"
n = ""
t = ("H", "o", "l", "a")
print s.join(t)
print n.join(t)
print type(s.join(t))
