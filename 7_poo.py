
"""
Clases: son los modelos sobre los cuales se basan un objeto.
Objetos: son las instancias de una clase.
"""
# Clase automovil

class Auto:
    def __init__(self, marca, modelo, placa):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
    

taxi = Auto("Toyota", "Corolla", "P-123456")

print(taxi.marca)

# Clase Persona

class Persona:
    def __init__(self, nombre, apellido, edad, profesion):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.profesion = profesion
    
    def saludar(self):
        print("Hola, mi nombre es", self.nombre, self.apellido, "y tengo", self.edad, "años")
    
    def despedir(self):
        print("Adios, me voy a trabajar, soy", self.profesion)
    
    def dormir(self):
        print("Me voy a dormir")
    
    def comer(self):
        print("Me voy a comer")
    
claudio = Persona("Claudio", "Sánchez", 25, "Ingeniero")

print(claudio.nombre)

# Validacion de contraseña

class PasswordValidator:
    def __init__(self, password):
        self.password = password
        self.longitud_minima = 8
        self.debe_tener_mayuscula = False
        self.debe_tener_minuscula = False
        self.debe_tener_numero = False

    def verificar_longitud(self):
        return len(self.password) >= self.longitud_minima

    def verificar_requisitos(self):
        for caracter in self.password:
            if caracter.isupper():
                self.debe_tener_mayuscula = True
            elif caracter.islower():
                self.debe_tener_minuscula = True
            elif caracter.isdigit():
                self.debe_tener_numero = True

    def es_valida(self):
        self.verificar_requisitos()
        return (self.verificar_longitud() and
                self.debe_tener_mayuscula and
                self.debe_tener_minuscula and
                self.debe_tener_numero)

# Solicitar la contraseña al usuario
contrasena = input("Ingrese una contraseña: ")

# Crear un objeto de la clase PasswordValidator
validator = PasswordValidator(contrasena)

# Verificar si la contraseña es válida
if validator.es_valida():
    print("La contraseña es válida.")
else:
    print("La contraseña no cumple con los requisitos mínimos.")

# Calculadora

class Calculadora:
    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

    def multiplicacion(self, a, b):
        return a * b

    def division(self, a, b):
        if b == 0:
            return "Error: No se puede dividir por cero"
        return a / b

# Crear un objeto de la clase Calculadora
calculadora = Calculadora()

# Menú de la calculadora
while True:
    print("Opciones:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    opcion = input("Seleccione una opción (1/2/3/4/5): ")

    if opcion == "5":
        print("¡Adiós!")
        break

    if opcion in ("1", "2", "3", "4"):
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if opcion == "1":
            print("Resultado:", calculadora.suma(num1, num2))
        elif opcion == "2":
            print("Resultado:", calculadora.resta(num1, num2))
        elif opcion == "3":
            print("Resultado:", calculadora.multiplicacion(num1, num2))
        elif opcion == "4":
            print("Resultado:", calculadora.division(num1, num2))
    else:
        print("Opción no válida. Intente de nuevo.")