#encoding: utf-8 

print "\n"
print "+ FUNCIÓN LAMBDA \n"
print "++ Funciones anónimas. Se pueden usar con map, filter y reduce."
print "++ Se puede utilizar para no ensuciar el código de funciones pequeñas y sin sentido."
print "++ ."
print "\n"

li = [1,-2,1,-4]
lo = [5,3,6,7]
s = "Hoola Mundo"

suma = lambda n,m:n+m

print "map: ", map(suma, li, lo)
print "filter: ", filter(lambda n: n=='o', s)
print "reduce: ", reduce(suma, lo)
print suma(3,4)