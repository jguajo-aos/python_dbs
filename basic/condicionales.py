
"""
Conditionals

"""
x = 5
if x < 10:
    print('Smaller')
if x > 20:
    print('Bigger')

print('Finish')

"""
if 

else

"""

"""
if

elif

elif

else

"""

x = 2
if x < 2:
    print('small')
elif x < 10:
    print('Medium')
else:
    print('LARGE')
print('All done')


# A que linea nunca entrara el codigo?
x = 20
if x < 2:
    print("Below 2")
elif x >= 2:
    print("Two or more")
else:
    print("Something else")


"""
Try and except

"""

# Error

astr = 'Hello Bob'
istr = int(astr)
print('First', istr)
# Que pasara?


astr = 'Hello Bob'
try:
    istr = int(astr)
except:
    istr = -1

print('First', istr)

try:
    # Solicitar al usuario que ingrese un número
    divisor = int(input("Ingrese un número para dividir 10: "))

    # Realizar la división
    resultado = 10 / divisor

    # Mostrar el resultado
    print(f"El resultado de la división es: {resultado}")

except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
except ValueError:
    print("Error: Ingrese un número válido.")
except Exception as e:
    print(f"Error inesperado: {e}")
    