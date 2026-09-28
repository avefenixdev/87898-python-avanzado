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

