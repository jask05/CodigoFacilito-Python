#encoding: utf-8 

print "\n"
print "+ FUNCIÓN FILTER \n"
print "++ Recibe una función y una lista e itera sobre cada uno de los elementos."
print "++ PYTHON 3 SE LLAMA COMPRESIÓN DE LISTAS."
print "\n"

def filtro(elem):
	return (elem > 0)

def filtro2(elem):
	return (elem == "o")

lista = [1,-3,2,-7,-8,10]
s = "hola mundo"

lr = filter(filtro,lista)
fs = filter(filtro2, s)

print lista
print lr

print "\n"

print s
print fs
print type(fs)

####################################
# http://www.juanjoconti.com.ar/2008/10/24/listas-por-comprension-en-python/
print "\n ##########################"
print "Más info: http://www.juanjoconti.com.ar/2008/10/24/listas-por-comprension-en-python/"
print "\n"

palabras = ['uno', 'dos', 'Santa Fe', 'Python', '...', 'Soleado']

def incluye_n(s):
    return 'N' in s.upper()

print incluye_n('Python')

print incluye_n('Soleado')

sin_compresion = filter(incluye_n, palabras)
print "Sin compresión: ", sin_compresion

compresion = [p for p in palabras if incluye_n(p)]
print "Compresión: ", compresion
