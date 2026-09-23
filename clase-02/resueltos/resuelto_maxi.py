compras = {}
nombre = input("Ingrese su nombre: ")
producto = input("¿Qué producto desea comprar?")
precio_unitario = float(input("Precio unitario?: ")) # float
cantidad = int(input("¿Cuantos desea comprar?: "))
compras['cliente'] = nombre
compras['producto'] = producto
compras['precio'] = precio_unitario
compras['cantidad'] = cantidad
compras['subtotal'] = compras['precio'] * compras['cantidad']
compras['total'] = compras['subtotal']
if compras['subtotal'] >= 50000:
    compras['total'] = compras['subtotal'] - compras['subtotal'] * 0.10
print("===============\n",
      "Datos de entrada\n")
print(f" Nombre: {compras['cliente']}\n Producto: {compras['producto']}\n Precio: {compras['precio']}\n Cantidad: {compras['cantidad']}")

print("=========== RESUMEN DE COMPRA ========")
print(f"Cliente: {compras['cliente']}\n Producto: {compras['producto']}\n Precio unitario: {compras['precio']}\n Cantidad: {compras['cantidad']}")
print(f"Subtotal: ${compras['subtotal']}\n Descuento: 10% si supera los $50000 \nTotal: ${compras['total']}")