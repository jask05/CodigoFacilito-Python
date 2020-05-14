#encoding: utf-8 

print "+ Listas y métodos \n"
print "---------- \n"

lista = [1, "Dos", 3, 3]
buscar = 1

print "buscar in lista: ", buscar in lista
print "\n + Hay que comprobar si existe ese elemento en la lista."

if buscar in lista:
	print "Existe. Índice del elemento - lista.index(buscar): ", lista.index(buscar)
else:
	print "No existe ese elemento"

buscar = 0
if buscar in lista:
	print "Existe. Índice del elemento - lista.index(buscar): ", lista.index(buscar)
else:
	print "No existe ese elemento"

print "\n ---------- \n"
print "+ Append: lista.append(\"x\")"
print lista
lista.append("Nuevo elemento")
print lista

print "\n ---------- \n"
print "+ Count "
print lista.count(3)

print "\n ---------- \n"
print "+ Insert: index que quiero agregar, elemento. "
print lista
lista.insert(2,"Nuevo insert")
print lista

print "\n ---------- \n"
print "+ Sumar listas "
print lista
iterable = [1,2,3,4]
lista.extend(iterable)
print lista

print "\n ---------- \n"
print "+ Sacar elemento de lista y elimina. pop() "
print lista
print "pop() saca el último si no se especifica: ", lista.pop()
print "pop(2) saca: ", lista.pop(2)

print "\n ---------- \n"
print "+ Elimina el elemento. remove(valor) "
print "+ Usar un FOR si se quieren eliminar todos los elementos ya que solo elimina 1."
print lista
print lista.remove(3)
print lista

print "\n ---------- \n"
print "+ Reverse "
print lista
lista.reverse()
print lista