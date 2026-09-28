import sqlite3
# Creamos base de datos
conexion = sqlite3.connect("tienda.db")

print(conexion)

try:
    # Creamos tabla
    conexion.execute(
        """
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL,
                precio REAL NOT NULL CHECK (precio >= 0),
                stock INTEGER NOT NULL DEFAULT 0 CHECK (stock >= 0)
            )
        """
    )
    conexion.commit()
finally:
    conexion.close()