#encoding: utf-8 

print "+ Funciones \n"
print " ++ Si se le pone un asterisco + nombre al final se la función se convierte en TUPLA"
print " ++ Si NO se pone ningún valor, solo utilizaría los dos primeros"
def mi_funcion(cad,v=2,*algomas):
	print cad * v
	for cadena in algomas:
		print "Imprimiendo tupla: " + cadena

mi_funcion("hola",4,"primero", "adios", "cadenas")

print "\n"
print " ++ Se puede guardar en un diccionario agreandno un * de más \n"

def mi_funcion_dos(cad,v=2,**dic):
	print cad * v
	print dic["cadenaextra"]
	print dic["cadenademas"]
	print dic["cdna"]

mi_funcion_dos("Python",5,cadenaextra= "Hola",cadenademas="Adios",cdna="Otra prueba")

print "\n"
print " ++ Regresar valores \n"
def mi_funcion_tres(num1,num2):
	return num1 + num2

num1=4
num2=5

resultado_suma = mi_funcion_tres(num1,num2)
print "El resultado de " + str(num1) + " + " + str(num2) + " es: " + str(resultado_suma)
