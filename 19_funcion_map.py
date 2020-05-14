#encoding: utf-8 

print "\n"
print "+ FUNCIÓN MAP \n"
print "++ Iteraciones de órden superior."
print "++ Regresan una lista ya habiendo procesado unas listas."
print "++ PYTHON 3 SE LLAMA COMPRESIÓN DE LISTAS."
print "++ Si los parámetros enviados tienen diferente tamaño, la función va a iterar tantas veces como sea el tamaño mayor, es decir si una lista/tupla tiene 3 elementos y la otra tiene 4, la función MAP se iterará 4 veces y al valor faltante le dará un valor None"
print "++ Al llamar a la función map con argumentos f y l ,dónde f es una función y l una lista, retorna una lista con los resultados de aplicar f a cada elemento de l."
print "\n"

def operador(n,m):
	
	# Sin esta condición marcaría error por haber una lista
	# más pequeña por lo que no puede sumarse.
	if n == None or m == None:
		return 0
	
	return n+m

l1 = [1,2,3,4]
t1 = (9,8,7,6)

# Lo almacena en un nuevo elemento
lr = map(operador,l1, t1)

print l1
print t1
print "\n Suma los elementos de la lista y la tupla: ", lr

print "\n Si es más pequeña ... se itera n veces según el número de secuencia más grande"

l2 = [1,2,3,4]
t2 = (9,8,7)

# Lo almacena en un nuevo elemento
lr2 = map(operador,l2, t2)
print lr2

print "\n Cadena de caracteres"

l3 = "Hola"
t3 = "Mundo"

# Lo almacena en un nuevo elemento
lr3 = map(operador,l3, t3)
print lr3

##################################
# Info sacada de: http://www.juanjoconti.com.ar/2008/10/24/listas-por-comprension-en-python/

palabras = ['uno', 'dos', 'Santa Fe', 'Python', '...', 'Soleado']
print "Utilizando map: ", map(len, palabras) # saca el tamaño de cada palabra

# Utilizando compresión se listas
palabras_compress = [len(p) for p in palabras]
print "Utilizando compresión de listas: ", palabras_compress