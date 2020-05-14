#encoding: utf-8 
print "\n"
print "+ ARCHIVOS\n"
print "++ Sin pasar parámetor, por defecto, modo lectura (r)."
print "++ Escritura. Si no existe, lo crea, si no lo pisa. (w)."
print "++ Añadir, solo se puede escribir en él. Se agrega al final y debe existir. (a)."
print "++ Leer y escribir. Debe existir. (r+)."
print "\n"

try:
	f = open("32_ejemplo.txt", "r+")
except:
	print "Error al abrir el archivo"
else:
	print f
	f.close()
	print f
