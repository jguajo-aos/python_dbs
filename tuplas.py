"""
Tuplas

Estructura de datos que permite almacenar una coleccion ordenada de elementos
Son usadas especialmente cuando se necesita inmutabilidad o asegurar
de que los datos no cambien

"""

# Creacion de una tupla vacia
tupla = ()

# Creacion de una tupla con elementos
tupla = (1, 2, 3, 4, 5)

# Acceder a un elemento de la tupla
print(tupla[0]) # 1

# Longitud de la tupla
print(len(tupla)) # 5

# Modificar elementos de la tupla
tupla[0] = 6 # Error: TypeError: 'tuple' object does not support item assignment

# Eliminar elementos de la tupla
del tupla[0] # Error: TypeError: 'tuple' object doesn't support item deletion

# Eliminar la tupla por completo
del tupla # Elimina la variable tupla

# Copiar una tupla
tupla2 = tupla.copy()

# Unir dos tuplas
tupla2 = (6, 7, 8, 9, 10)
tupla3 = tupla + tupla2

# Contar elementos de una tupla
print(tupla.count(1))

# Obtener el indice de un elemento de la tupla
print(tupla.index(1))

# Convertir una lista en una tupla
lista = [1, 2, 3, 4, 5]
tupla = tuple(lista)

# Convertir una tupla en una lista
tupla = (1, 2, 3, 4, 5)
lista = list(tupla)

# Ordenar una tupla
tupla = (3, 5, 1, 4, 2)
tupla = tuple(sorted(tupla)) # Ordena la tupla de menor a mayor

# Invertir una tupla
tupla = (1, 2, 3, 4, 5)
tupla = tupla[::-1] # Invierte la tupla

# Crear una tupla con un solo elemento
tupla = (1, ) # Si no se agrega la coma, el elemento se interpreta como un entero

# Desempaquetado de tuplas
tupla = (1, 2, 3, 4, 5)
a, b, c, d, e = tupla

# Comprension de tuplas
cuadrados = tuple(i**2 for i in range(1, 11))

# Crear una tupla a partir de una cadena
tupla = tuple("Hola mundo")
print(tupla) # ('H', 'o', 'l', 'a', ' ', 'm', 'u', 'n', 'd', 'o')

# Crear una tupla a partir de una cadena
tupla = tuple("Hola mundo".split())

# Crear una tupla a partir de una cadena
tupla = tuple("Hola mundo".split("a"))

