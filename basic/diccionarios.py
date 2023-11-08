"""
Diccionarios:

Estructura de datos que permite almacenar una coleccion desordenada de elementos mediante pares
clave-valor

"""

# Crear un diccionario vacio
diccionario = {}

# Crear un diccionario con elementos
diccionario = {
    "clave1": "valor1", 
    "clave2": "valor2", 
    "clave3": "valor3"
}

# Acceder a un elemento del diccionario
print(diccionario["clave1"]) # valor1

# Agregar un elemento al diccionario
diccionario["clave4"] = "valor4"

# Modificar un elemento del diccionario
diccionario["clave1"] = "Nuevo valor" # Modifica el valor de la clave1

# Longitud de un diccionario
print(len(diccionario)) # 4

# Eliminar elementos del diccionario
del diccionario["clave1"] # Elimina el elemento con la clave1

# Eliminar todos los elementos del diccionario
diccionario.clear() # Elimina todos los elementos del diccionario

# Eliminar el diccionario por completo
del diccionario # Elimina la variable diccionario

# Copiar un diccionario
diccionario2 = diccionario.copy()

# Unir dos diccionarios

diccionario2 = {
    "clave5": "valor5", 
    "clave6": "valor6", 
    "clave7": "valor7"
}
diccionario3 = {**diccionario, **diccionario2}

# Obtener las claves de un diccionario
print(diccionario.keys()) # dict_keys(['clave2', 'clave3', 'clave4'])

# Obtener los valores de un diccionario
print(diccionario.values()) # dict_values(['valor2', 'valor3', 'valor4'])

# Obtener los pares clave-valor de un diccionario
print(diccionario.items()) # dict_items([('clave2', 'valor2'), ('clave3', 'valor3'), ('clave4', 'valor4')])

# Obtener un elemento del diccionario
print(diccionario.get("clave2")) # valor2

# Obtener un elemento del diccionario
print(diccionario["clave2"]) # valor2

# Obtener un elemento del diccionario
print(diccionario["clave5"]) # Error: KeyError: 'clave5'

# Obtener un elemento del diccionario
print(diccionario.get("clave5")) # None

# Obtener un elemento del diccionario
print(diccionario.get("clave5", "No existe")) # No existe

# Comprobar si una clave existe en el diccionario
print("clave2" in diccionario) # True

# Convertir de diccionario a lista
lista = list(diccionario.items()) # Convierte el diccionario en una lista de tuplas


# Comprension de diccionarios
cuadrados = {i: i**2 for i in range(1, 11)}
