print("~~~~ REGISTRO DE COMPRA ~~~~")
nombre = input("Ingrese su nombre: ")
producto = input("Ingrese el producto que desea comprar: ")
precio_unitario = float(input("Ingrese el precio unitario: $"))
cantidad = int(input("Ingrese la cantidad: "))

compra = {
    "cliente": nombre,
    "producto": producto,
    "precio_unitario": precio_unitario,
    "cantidad": cantidad
}

subtotal = precio_unitario * cantidad

if subtotal >= 50000:
    descuento = subtotal * 0.10
    total = subtotal - descuento
    obtuvo_descuento = True
else:
    descuento = 0
    total = subtotal
    obtuvo_descuento = False

print("\n=========== RESUMEN DE COMPRA ===========")
print(f"Cliente: {compra['cliente']}")
print(f"Producto: {compra['producto']}")
print(f"Precio unitario: ${compra['precio_unitario']}")
print(f"Cantidad: {compra['cantidad']}")
print(f"Subtotal: ${subtotal}")
print(f"Descuento: 10% si supera los $50000")
print(f"Total: ${total}")
if obtuvo_descuento:
    print("Obtuviste un descuento")
else:
    print("No obtuviste un descuento")