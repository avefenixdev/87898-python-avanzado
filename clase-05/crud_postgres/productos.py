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
    conexion = conectar()
    try:
        # filas === cursor
        filas = conexion.execute(
            "SELECT id, nombre, precio, stock FROM productos ORDER BY id"
        ).fetchall()
        return [dict(fila) for fila in filas] # retorno una lista de dicts (un array de objetos de js)
    finally:
        conexion.close()
    
def obtener_producto(identificador):
    conexion = conectar()
    try:
        # preparo la consulta y ejecuto la consulta
        # fila === cursor
        fila = conexion.execute(
            "SELECT id, nombre, precio, stock FROM productos WHERE id = ?",
            (identificador,)
        ).fetchone()
        return dict(fila) if fila is not None else None # retorno un dict (objeto de js)
    finally:
        conexion.close()

def actualizar_producto(identificador, nombre, precio, stock):
    conexion = conectar()
    try:
        cursor = conexion.execute(
            """ UPDATE productos SET nombre = ?, precio = ?, stock = ?
               WHERE id = ? """,
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
            "DELETE FROM productos WHERE id = ?", (identificador,)
        )
        conexion.commit()
        return cursor.rowcount > 0
    except Exception:
        conexion.rollback()
        raise
    finally:
        conexion.close()