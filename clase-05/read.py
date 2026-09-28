import sqlite3

conexion = sqlite3.connect("tienda.db")

try:
    # Listado de productos que tienen un precio menor a 60_000 ordenados en forma ascendente
    cur = conexion.execute(
        "SELECT id, nombre, precio FROM productos WHERE precio <= ? ORDER BY precio ASC",
        (60_000,)
    )
    
    print('-------------')
    for identificador, nombre, precio in cur:
        print(identificador, nombre, precio)
    print('-------------')
    # Buscando un producto por ID
    encontrado = conexion.execute(
        "SELECT id, nombre, stock FROM productos WHERE id = ?", (1,)
    ).fetchone() # fetchall() -> para conjuntos pequeños de registros
    print(encontrado) # Si lo encuentra devuelve el registro (tupla) y sino un None
    print(encontrado if encontrado is not None else "No existe")    
finally:
    conexion.close()
