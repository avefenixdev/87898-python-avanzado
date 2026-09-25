def pedir_datos():
    nombre = input("Ingresa un nombre: ")
    edad = input("Ingresa una edad: ")
    ciudad = input("Ingresa una ciudad: ")
    return nombre, edad, ciudad
def guardar_datos_archivo(nombre, edad, ciudad):
    with open("personas.txt", "w") as archivo:
        archivo.write(f"Nombre: {nombre}\n")
        archivo.write(f"Edad: {edad}\n")
        archivo.write(f"Ciudad: {ciudad}\n")
    print("Cargaste exitosamente los datos")
def leer_datos_archivo():
    print("Los datos guardados son: ")
    with open("personas.txt", "r") as archivo:
        for linea in archivo:
            print(linea.strip())
            
## Código principal de la aplicación
def start():
    nombre, edad, ciudad = pedir_datos()
    guardar_datos_archivo(nombre, edad, ciudad)
    leer_datos_archivo()
    
start()