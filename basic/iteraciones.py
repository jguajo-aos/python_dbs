"""
While: ejecuta un bloque de código mientras la condición sea verdadera
"""

# Ejecute mientras el valor de un numero sea mayor a 0

numero = 10
while numero > 0:
    print(numero)
    numero -= 1 # numero = numero - 1
print("Fin del ciclo")

"""
break: termina el ciclo si la condición se cumple
"""

while True:
    linea = input('> ')
    if linea == 'fin':
        break
    print(linea)
print('¡Terminado!')

"""

continue: finaliza la iteración actual y continua con la siguiente
"""

while True:
    linea = input('> ')
    if linea[0] == '#':
        continue
    if linea == 'fin':
        break
    print(linea)
print('¡Terminado!')

"""
for

"""
import time

amigos = ['Jose', 'Juan', 'Pedro']

inicio = time.time()
for amigo in amigos:
    print('Feliz año nuevo:', amigo)

fin = time.time()

tiempo_transcurrido = fin - inicio

print(f"Tiempo transcurrido: {tiempo_transcurrido} segundos")


"""
Acciones en un loop
"""

zork = 0
print('Antes', zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + 1
    print(zork, thing)
print('Después', zork)




for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + 1
    print(zork, thing)
print('Después', zork)


mi_lista = [1, 2, 3, 4, 5]

for indice, valor in enumerate(mi_lista):
    print(f"El indice es: {indice} y el valor es: {valor}")

"""
Calcular el total de una lista
"""

zork = 0
print('Antes', zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + thing
    print(zork, thing)
print('Después', zork)

"""
Encontrar el valor promedio de una lista
"""

count = 0
sum = 0
print('Antes', count, sum)
for value in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('Después', count, sum, sum / count)


"""

Filtrar en un loop
"""
print('Antes')
for value in [9, 41, 12, 3, 74, 15]:
    if value > 20:
        print('Mayor a 20', value)
print('Después')

"""

Usar una variable booleana
"""

found = False  
print('Antes', found)
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found = True
    print(found, value)
print('Después', found)


"""
range
"""

for numero in range(5):
    print(numero)


for numero in range(1, 10, 2):
    print(numero)


filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))
for fila in range(filas):
    for columna in range(columnas):
        print("*", end="")
    print("")


import random

filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))
for fila in range(filas):
    for columna in range(columnas):
        print(random.randint(1, 10), end="")
    print("")
