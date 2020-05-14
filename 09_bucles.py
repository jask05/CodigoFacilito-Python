#encoding: utf-8 

print "------------ "
print "+ While"

edad = 0

while edad <= 20:
	
	if edad == 15:
		# No ejecuta la siguiente parte
		# Pero se vuelve a repetir hasta salir
		# del WHILE
		edad = edad +1
		continue
		# Para salir del bucle y no continuar
		# se utiliza:
		# break

	print "Tiendes: " + str(edad)
	edad = edad + 1

print "\n"
print "------------"
print "+ For in para recorrer listas, tuplas o diccionarios."

lista = ["Elemento 1", "Elemento 2", "Elemento 3"]

for elem in lista:
	print elem

print "\n "
print "+ Imprimiendo una cadena con for in"

for letra in "cadena":
	print letra
