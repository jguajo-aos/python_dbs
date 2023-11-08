"""
Constantes:

Son valores que no cambian durante la ejecución del programa. Ejemplos: strings, números, caracteres

"""

# Constantes de tipo string
name = "Juan"
last_name = "Perez"

# Constantes de tipo numérico
age = 25
weight = 75.5

# Constantes de tipo caracter
gender = 'M'

# Constantes de tipo booleano
is_colombian = True

"""
Variables: 

Un lugar nombrado en memoria donde un programador puede almacenar datos y luego recuperarlos.

"""

name = "Juan"
age = 25


"""
Reglas de nombramiento de variables:

- No pueden empezar con números
- No pueden tener espacios
- No pueden tener caracteres especiales
- No pueden tener acentos
- No pueden tener ñ
- No pueden tener guiones medios

https://peps.python.org/pep-0008/

"""

# Bueno: spam, eggs, spam23, _speed, more_speed, Speed, SPEED, _Speed
# Malo: 23spam, #sign, var.12, more$, class

"""
Oraciones de asignación
"""

x = 2
x = x + 2
print(x)

"""
Nombres dicientes
"""

# Feo
abcd = 33
abcddd = 34
avfd = abcd + abcddd
print(avfd)

# bonito
a = 33
b = 34
c = a + b
print(c)

"""

Declaracion de asignación:

La declaración de asignación crea nuevas variables y les da valores.

"""
x = 2   
x = 3.9 * x * (1 - x)


"""
Expresiones numericas: =, +, -, *, /, **, %

"""

"""
Orden de evaluacion de expresiones:

1. Paréntesis
2. Exponentes
3. Division
4. Multiplicacion
5. Suma y resta

"""

x = 1 + 2 ** 3 / 4 * 5
print(x)

"""
Tipos de datos y sus operaciones:

- int
- float
- str

"""

a = "hello" + "world"
b = a + 1 # Que pasara?

# Podemos validar el tipo de dato con la funcion type()

"""
Tipo de conversiones:

- int()
- float()
"""

# Conversion de strings:

sval = "123"
ival = int(sval)
print(ival + 1)

"""
Convertir entrada de usuario:

- input()

"""

name = input("Enter your name: ")
print("Hello", name)