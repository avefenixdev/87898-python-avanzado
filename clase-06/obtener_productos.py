import requests

def obtener_productos(producto_id):
    
    try:
        respuesta = requests.get(
            f"https://dummyjson.com/products/{producto_id}",
            timeout=(3.05, 10)
        )
        respuesta.raise_for_status()
        producto = respuesta.json()
        
        if not isinstance(producto, dict) or 'title' not in producto:
            raise ValueError("La respuesta no tiene el formato esperado")
        return producto
    except ValueError as error:
        print(f"Datos inesperados. {error}")


print(obtener_productos(1))