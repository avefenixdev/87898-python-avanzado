def calcular_total(precio, cantidad):
    subtotal = precio * cantidad
    descuento = subtotal * 0.10
    total = subtotal - descuento
    return total


precio = 1000
cantidad = 3

resultado = calcular_total(precio, cantidad)

print(f"Total: ${resultado}")