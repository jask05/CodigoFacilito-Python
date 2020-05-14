# -*- coding: utf-8 -*-

print "+ No tienen índice si no CLAVE"
print "+ Matrices asociativas"
print "+ Como CLAVE no se pueden utilizar diccionarios ni listas."
print "+ Se puede modificar el valor PERO NO la clave."
print "+ No se puede hacer 'slicing'. d[0:2] no está permitido. No existe índices, por eso no se puede. \n"


d = {
	"Clave1": [1,2,3],
	"Clave2": True,
	"Clave3": "Hola",
	4: "Sería el 4"
}

print d["Clave2"]
print d[4]

d[4] = "Sería el 4+1 si eso"
print d[4]

