#encoding: utf-8 
print "\n"
print "+ LECTURA DE ARCHIVOS\n"
print "++ Sin pasar parámetor, por defecto, modo lectura (r)."
print "++ Escritura. Si no existe, lo crea, si no lo pisa. (w)."
print "++ Añadir, solo se puede escribir en él. Se agrega al final y debe existir. (a)."
print "++ Leer y escribir. Debe existir. (r+)."
print "\n"

try:
	f = open("33_ejemplo.txt", "w")
except:
	exit()
	print "Error"

f.write("Hola, este es mi primer archivo.")

# bytes a recorrer y desde donde
# 0  - Comienzo del archivo
# 1 -  A partir de la posición que se encuentra actualmente.
# 2 - Cuenta a partir del final del archivo
f.seek(-2,2) 

# Para saber donde está el puntero
print f.tell()

f.write("INTRUSO")


print "\n---------------------\n"

agregar = ["Hola ", "Mundo\n", "Hi Programadores!\n"]

f.writelines(agregar)

# Indica si el archivo está cerrado.
f.closed

print "\n---------------------\n"
f.close()

if not f.closed:
	f.writelines(agregar)