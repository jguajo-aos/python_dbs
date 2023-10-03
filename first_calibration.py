""""
Problema: Calcular el descuento de una compra

Instrucciones:

1. El usuario realiza 4 compras. Ejecutar el proceso hasta un maximum de 4 compras.
2. Por cada compra, ingresar el nombre del producto, el precio y la cantidad.
3. Calcular el total de la compra. Aplicar un descuento del 10% si el total es igual o superior a $100.
4. Mostrar el total de la compra (con o sin descuento).
"""


productos = []
precios = []
cantidades = []
max_productos = 4  # Máximo de 4 productos permitidos

while len(productos) < max_productos:
    producto = input("Ingrese el nombre del producto (o 'fin' para terminar): ")
    if producto.lower() == "fin":
        break
    precio = float(input(f"Ingrese el precio de {producto}: "))
    cantidad = int(input(f"Ingrese la cantidad de {producto}: "))

    productos.append(producto)
    precios.append(precio)
    cantidades.append(cantidad)

# Calcular el total de la compra
total = sum(precio * cantidad for precio, cantidad in zip(precios, cantidades))

# Aplicar un descuento del 10% si el total es igual o superior a $100
if total >= 100:
    descuento = total * 0.10
    total_con_descuento = total - descuento
    print(f"Total de la compra (con descuento del 10%): ${total_con_descuento:.2f}")
else:
    print(f"Total de la compra (sin descuento): ${total:.2f}")
