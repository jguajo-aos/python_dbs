"""
Listas:

Estructura de datos que permite almacenar una coleccion ordenada de elementos

"""

# Crear una lista vacia
lista = []

# Crear una lista con elementos
lista = [1, 2, 3, 4, 5]
lista = ["Hola", "Mundo", "!"]

# Acceder a un elemento de la lista
print(lista[0]) # Hola
print(lista[1]) # Mundo
print(lista[2]) # !
print(list[-1]) # !

print(lista[3]) # Error: IndexError: list index out of range

print(lista[:2])    # ['Hola', 'Mundo']

# Agregar un elemento al final de la lista
lista.append(6)

# Modificar elementos de la lista
lista[0] = "Nuevo elemento"

# Longitud de la lista
print(len(lista)) # 5

# Insertar elementos en una posicion especifica
lista.insert(0, "Nuevo elemento")

# Eliminar elementos

# Eliminar el ultimo elemento de la lista
lista.remove("Nuevo elemento") # Elimina el primer elemento que coincida con el valor especificado

# Eliminar el ultimo elemento de la lista
lista.pop() # Elimina el ultimo elemento de la lista, si no se especifica un indice

# Eliminar un elemento de la lista por su indice
del lista[0] # Elimina el elemento de la posicion 0

# Eliminar todos los elementos de la lista
lista.clear()

# Eliminar la lista por completo
del lista # Elimina la variable lista

# Ordenar una lista
lista = [3, 5, 1, 4, 2]
lista.sort() # Ordena la lista de menor a mayor
lista.sort(reverse=True) # Ordena la lista de mayor a menor

# Invertir una lista
lista.reverse()

# Copiar una lista
lista2 = lista.copy() # Copia la lista en una nueva variable

# Unir dos listas
lista3 = lista + lista2 # Une las dos listas en una nueva lista

# Iterar sobre una lista
for elemento in lista:
    print(elemento) # 1, 2, 3, 4, 5

# Iterar sobre una lista con indices
for i in range(len(lista)):
    print(lista[i]) # 1, 2, 3, 4, 5

# Iterar sobre una lista con indices y elementos
for i, elemento in enumerate(lista):
    print(i, elemento) # 0 1, 1 2, 2 3, 3 4, 4 5

# Buscar un elemento en una lista
if 3 in lista:
    print("El elemento 3 esta en la lista") # El elemento 3 esta en la lista

# Contar cuantas veces se repite un elemento en una lista
print(lista.count(3)) # 1

# Obtener el indice de un elemento en la lista
print(lista.index(3)) # 2


# Extender una lista
lista2 = [6, 7, 8, 9, 10]
lista.extend(lista2) # Agrega los elementos de lista2 a lista

# Funcion max() y min()
print(max(lista)) # 10
print(min(lista)) # 1

# Funcion sum()
print(sum(lista)) # 55



