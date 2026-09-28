from database import inicializar
from productos import (
    actualizar_producto,
    crear_producto,
    eliminar_producto,
    listar_productos,
    obtener_producto
)

def main():
    
    try:
        inicializar() # creando la tabla si existe
        identificadorUno = crear_producto("Auriculares", 32_000, 5)
        identificadorDos = crear_producto("Teclado", 12_000, 3)
        identificadorTres = crear_producto("Mouse", 10_000, 8)
        
        print("Creado Uno:", obtener_producto(identificadorUno)) # 10
        print("Creado Dos:", obtener_producto(identificadorDos)) # 11
        print("Creado Tres:", obtener_producto(identificadorTres)) # 12
        print("No existe:", obtener_producto(55)) # Nos devuelve None
        print("Todos", listar_productos()) # Nos devuelve una lista de dicts
        # Editamos el 12
        print("Actualizando:", actualizar_producto(identificadorTres, "Ariculares", 42_000, 4))
        # Borramos el 10
        print("Luego:", obtener_producto(identificadorTres))
        print("Eliminado:", eliminar_producto(identificadorUno))
        print("Luego:", obtener_producto(identificadorUno)) # 10 -> None
    except Exception as e:
        print(e)
        
print(__name__)
if __name__ == "__main__":
    main()
    
