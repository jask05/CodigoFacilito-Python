#encoding: utf-8 
print "\n"
print "+ ENTRADA DE ARCHIVOS\n"
print "++ "
print "\n"

try:
	f = open("34_entrada_archivos_ejemplo.txt", "r")
except:
	exit()
	print "Error!"

print "\n+ Se puede establecer en read() el nº de bytes a leer.\n"

# print f.read(50)

lineas = f.readlines()

# print "-> readline(): ", f.readline()
# print "Nueva línea (vacía): ", f.readline()
# print "Tercera línea: ", f.readline()

# while True:
# 	print f.readline()
# 	if f.readline() == "":
# 		break

# for l in lineas:
# 	print "=>", l, "\n\n"

print lineas