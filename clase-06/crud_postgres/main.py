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
        #identificadorUno = crear_producto("Auriculares", 32_000, 5)
        #identificadorDos = crear_producto("Teclado", 12_000, 3)
        #identificadorTres = crear_producto("Mouse", 10_000, 8)
        #print("Todos", listar_productos()) # Nos devuelve una lista de dicts
        
        #print("Creado Uno:", obtener_producto(1)) 
        #print("Creado Dos:", obtener_producto(2)) 
        #print("Creado Tres:", obtener_producto(3))
        
        # print(eliminar_producto(23)) # False
        # print(eliminar_producto(27)) # True
        # print(eliminar_producto(30)) # False
        # print(eliminar_producto(22)) # True
        
        #print(actualizar_producto(4, "Producto Editado", 222_222, 5))
        
    except Exception as e:
        print(e)
        
print(__name__)
if __name__ == "__main__":
    main()
    
