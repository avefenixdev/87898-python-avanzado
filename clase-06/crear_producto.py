import requests

producto = { "title": "Mouse", "price": 50, "stock": 15 }

try: 
    
    respuesta = requests.post(
        "https://dummyjson.com/products/add",
        json=producto,
        timeout=(3.05, 10)
    )

    respuesta.raise_for_status()

    #if respuesta.status_code == 201:
    if respuesta.status_code == requests.codes.created:
        creado = respuesta.json()
        print("Estado:", respuesta.status_code)
        print("Identificador simulado:", creado["id"])
        print("Nombre:", creado["title"])
    else: 
        print("Respuesta exitosa con otro estado:", respuesta.status_code)
    
except requests.exceptions.Timeout:
    print("El servidor tardó demasiado tiempo en responder")
except requests.exceptions.HTTPError as error:
    print("Error HTTP:", error.response.status_code)
    print("Detalle:", error.response.text)
    