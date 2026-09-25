def pedir_datos():
    nombre = pedir_ingreso("nombre")
    edad = int(input("Ingrese su edad: "))
    ciudad = pedir_ingreso("ciudad")
    dicc = {"nombre":nombre, "edad":edad, "ciudad":ciudad}
    return dicc
def pedir_ingreso(dato):
    return input(f"Ingrese su {dato}: ")
def guardar_datos_archivo(datos):
    with open("persona.txt", "w") as archivo:
        archivo.write(f"Nombre: {datos["nombre"]}\n")
        archivo.write(f"Edad: {datos["edad"]}\n")
        archivo.write(f"Ciudad: {datos["ciudad"]}\n")
    print("Se guardo el archivo\n")

def leer_datos_archivo():
    with open("persona.txt", "r") as archivo:
        for linea in archivo:
            print(linea.strip())
            
def start():
    datos = pedir_datos()
    guardar_datos_archivo(datos)
    leer_datos_archivo()
start()