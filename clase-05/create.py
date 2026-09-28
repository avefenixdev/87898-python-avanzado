import sqlite3

conexion = sqlite3.connect("tienda.db")


try:
    cursor = conexion.execute(
        "INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)",
        ("Teclado", 50_000, 10) # le tengo que pasar una tupla
    )
    # ? <--- se los conoce como marcadores (placeholder)    
    print("ID insertado:", cursor.lastrowid)
    conexion.commit()
except sqlite3.Error:
    conexion.rollback() # Volver para atrás si falló. Revierte la transacción
    raise
finally:
    conexion.close()