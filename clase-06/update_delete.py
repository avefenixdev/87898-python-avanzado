import requests

URL = 'https://dummyjson.com/products/1'
TIMEOUT = (3.05, 10)

original = requests.get(URL, timeout=TIMEOUT)
original.raise_for_status()
remplazo = original.json() # Producto original
remplazo['title'] = "Nombre de prueba" # producto editado

# Actualizando el producto (Cambiando el nombre)
respuesta = requests.put(URL, json=remplazo, timeout=TIMEOUT)
respuesta.raise_for_status()
producto_editado = respuesta.json()
print(producto_editado)
print("PUT:", respuesta.status_code)

print("-----------------------------")
# Borrado de producto
respuesta = requests.delete(URL, timeout=TIMEOUT)
respuesta.raise_for_status()
if respuesta.status_code != 204 and respuesta.content:
    producto_eliminado = respuesta.json()
    print(producto_eliminado)
    print("DELETE:", respuesta.status_code)
