nombre = input("Ingrese su nombre: ")
producto = input("Ingrese el producto que desea comprar: ")
precio_unitario = float(input("Ingrese el precio por unidad: "))
cantidad = int(input("Ingrese la cantidad que desea comprar: "))

compra = {
    "nombre": nombre,
    "producto": producto,
    "precio_unitario": precio_unitario,
    "cantidad": cantidad,
}

subtotal = compra['precio_unitario'] * cantidad
compra['subtotal'] = subtotal

if compra['subtotal'] >= 50000:
    descuento = compra['subtotal'] * 0.10
    tiene_descuento = True    
else:
    descuento = 0
    tiene_descuento = False

total = compra['subtotal'] - descuento
compra['total'] = total

print('RESUMEN DE LA COMPRA')
print("Cliente:", compra["nombre"])
print("Producto:", compra["producto"])
print("Precio unitario: $", compra["precio_unitario"])
print("Cantidad:", compra["cantidad"])
print("Subtotal: $", compra["subtotal"])
if tiene_descuento:
    print("El cliente obtuvo un descuento del 10%.")
else:
    print("El cliente no obtuvo descuento.")
print("Total a pagar: $", compra['total'])