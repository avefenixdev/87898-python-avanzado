from database import conectar

# CRUD -> CREATE | READ | UPDATE | DELETE
def crear_producto(nombre, precio, stock):
    with conectar() as conexion:
        # Preparar la consulta
        fila = conexion.execute(
            "INSERT INTO productos (nombre, precio, stock) VALUES (%s, %s, %s) RETURNING id",
            (nombre, precio, stock)
        ).fetchone()
        return fila["id"]
    
def listar_productos():
    with conectar() as conexion:
        filas = conexion.execute(
            "SELECT id, nombre, precio, stock FROM productos ORDER BY id"
        ).fetchall()
        return filas
        
def obtener_producto(identificador):
    with conectar() as conexion:
        return conexion.execute(
            "SELECT id, nombre, precio, stock FROM productos WHERE id = %s",
            (identificador,)
        ).fetchone()

def actualizar_producto(identificador, nombre, precio, stock):
    conexion = conectar()
    try:
        cursor = conexion.execute(
            """ UPDATE productos SET nombre = %s, precio = %s, stock = %s
               WHERE id = %s """,
            (nombre, precio, stock, identificador)
        )
        conexion.commit()
        return cursor.rowcount > 0
    except Exception:
        conexion.rollback()
        raise
    finally:
        conexion.close()
    
def eliminar_producto(identificador):
    conexion = conectar()
    try:
        cursor = conexion.execute(
            "DELETE FROM productos WHERE id = %s", (identificador,)
        )
        conexion.commit()
        return cursor.rowcount > 0
    except Exception:
        conexion.rollback()
        raise
    finally:
        conexion.close()