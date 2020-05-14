#encoding: utf-8 

print "\n"
print "+ Métodos de diccionarios \n"

diccionario = {
	"redes_sociales": ['Twitter', 'Facebook', 'LinkedIn'],
	3: 'Tres',
	'Hola': "Mundo"
}

print "############ \n"

print """diccionario = {
	"redes_sociales": ['Twitter', 'Facebook', 'LinkedIn'],
	3: 'Tres',
	'Hola': "Mundo"
}"""

print "############ \n"

print "+ diccionario.has_key(\"Hola\")"
print diccionario.has_key("Hola")

print "\n"
print "+ diccionario.items()"
print diccionario.items()

print "\n"
print "+ diccionario.keys()"
print diccionario.keys()

print "\n"
print "+ diccionario.values()"
print diccionario.values()

print "\n"
print "+ diccionario.pop(valor, [d]) - [d]: regresa valor si NO se encuentra"
print diccionario 
print diccionario.pop(3)
print diccionario.pop(4, "no se encuentra el 4")
print diccionario

print "\n"
print "+ del diccionario[clave]"
del diccionario["Hola"]
print diccionario

print "\n"
print "+ diccionario.clear()"
print diccionario
diccionario.clear()
diccionario["clave_nueva"] = "valor"
print diccionario

print "\n"
print "+ diccionario.copy()"
diccionario_2 = diccionario.copy()
print diccionario_2