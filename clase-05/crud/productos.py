from database import conectar

# CRUD -> CREATE | READ | UPDATE | DELETE
def crear_producto(nombre, precio, stock):
    conexion = conectar()
    
    try:
        # Preparar la consulta
        cursor = conexion.execute(
            "INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)",
            (nombre, precio, stock)
        )
        # Ejecutamos la query
        conexion.commit()
        return cursor.lastrowid # el id lo crea la base de datos.
        
    except Exception:
        conexion.rollback()
        raise # lanzar hacía arriba en el stack del error
    finally:
        conexion.close()
  
    
def listar_productos():
    print()
    
def obtener_producto(identificador):
    print()

def actualizar_producto(identificador, nombre, precio, stock):
    print()
    
def eliminar_producto(identificdor):
    print()