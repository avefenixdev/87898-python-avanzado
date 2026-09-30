import requests

try:   
    respuesta = requests.get(
        "https://dummyjson.com/products/",
        params={"limit": 5, "skip": 0},
        timeout=(3.05, 10)
    )

    respuesta.raise_for_status()
    datos = respuesta.json()
    
    if not isinstance(datos, dict) or "products" not in datos:
        raise ValueError("La respuesta no tiene el formato esperado")
    #print(datos)
    for producto in datos["products"]:
        print(producto["id"], producto["title"])
        
except ValueError as error:
    print(f"Datos inesperados: {error}")

