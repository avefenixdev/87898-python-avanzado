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
    except requests.exceptions.ContentDecodingError:
        print("La respuesta no contiene JSON válido")
    except requests.exceptions.Timeout:
        print("Se agotó el tiempo de espera")
    except requests.exceptions.RequestException as error:
        print(f"Falló la comunicación: {error}")
    except ValueError as error:
        print(f"Datos inesperados. {error}")
    return None

if __name__ == "__main__":
    producto = obtener_productos(1)
    if producto is not None:
        print(producto['title'])