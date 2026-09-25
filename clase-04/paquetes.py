import requests # este es el paquete(modulo) de requests

# https://pokeapi.co/ # Servicio Rest API que nos entrega pokemones y sus caracteristicas
# https://fakestoreapi.com/ # Servicio Rest Api que nos entrega los endopoints de un fake ecommerce
respuesta = requests.get(
    "https://fakestoreapi.com/products/1"
)

productoID1 = respuesta.json()

print(productoID1)