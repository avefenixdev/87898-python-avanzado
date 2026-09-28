from pathlib import Path
import sqlite3

RUTA_DB = Path(__file__).with_name("tienda.db")
# print(RUTA_DB) # ruta absoluta al archivo de la db
print(__file__) # ruta absoluta a donde está el script actual.
print(Path(__file__)) # ruta absoluta sin el nombre del script (archivo).

def conectar():
    conexion = sqlite3.connect(RUTA_DB)
    conexion.row_factory = sqlite3.Row # config driver -> podamos acceder por medio fila["nombre"]
    return conexion

def inicializar():
    conexion = conectar()
    
    try:
        # Preparando la consulta
        conexion.execute(
            """
                CREATE TABLE IF NOT EXISTS productos (
                    id INTEGER PRIMARY KEY,
                    nombre TEXT NOT NULL,
                    precio REAL NOT NULL CHECK ( precio >= 0 ),
                    stock INTEGER NOT NULL DEFAULT 0 CHECK ( stock >= 0 )
                )             
        """)
        # Corriendo la consulta
        conexion.commit()
    finally:
        # Cerramos conexión
        conexion.close()
