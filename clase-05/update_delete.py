import sqlite3

conexion = sqlite3.connect("tienda.db")

try:
    # Actualizando el precio del producto con el ID: 1
    cursor = conexion.execute(
        "UPDATE productos SET precio = ? WHERE id = ?", (55_000, 1)
    )
    print("Producto con ID: 1 - Actualizado", cursor.rowcount)
    
    
    
    
    conexion.commit()
    
    
except sqlite3.Error:
    conexion.rollback()
    raise
finally:
    conexion.close()