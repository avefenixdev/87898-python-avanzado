print("Clase 06 - Python Avanzando")

import json

## Serializar y deserializar un diccionario de python a un json y viceversa

producto = { "nombre": "Teclado", "activo": True, "detalle": None, "precio": 2_200 }
texto = json.dumps(producto, ensure_ascii=False) # transformar un dic en json(str)
recuperar_dic = json.loads(texto) # transformar un json(str) a un dic
print(texto)
print(recuperar_dic)
# Averiguar tipos
print(type(texto).__name__)
print(type(recuperar_dic).__name__)

# peticiones (trabajar con el protocolo http)
# https://pypi.org/project/requests/
# pip install requests # python -m pip install requests

import requests # 

# https://dummyjson.com/

response = requests.get(
    "https://dummyjson.com/products/1",
    timeout=(3.05, 10)
)

response.raise_for_status()
producto = response.json() # Obtengo un objeto que luego a json

print("Estado:", response.status_code) # un entero con el estado 1xx a 5xx
print("Tipo:", response.headers.get("Content-Type")) # cabeceras de la petición
print("Nombre", producto["title"])
print("Categoría", producto["category"])
print("Precio", producto["price"])

