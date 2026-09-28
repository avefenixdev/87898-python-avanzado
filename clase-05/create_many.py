import sqlite3

try:
    with sqlite3.connect("tienda.db") as conexion:
        conexion.executemany(
            "INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)",
            [("Mouse", 18_000, 8), ("Monitor", 210_000, 3)]
        )
    
except sqlite3.Error as error:
    print(f"Error al insertar productos: {error}")

# https://docs.python.org/3/library/sqlite3.html