def pedir_nombre():
    return input("Ingrese su nombre: ")
def pedir_edad():
    try:
        edad = int(input("Ingrese su edad:"))
    except:
        print("Edad invalida")
    return edad
def pedir_ciudad():
    return input("Ingrese su ciudad: ")
def pedir_profesion():
    return input("Ingrese su profesion: ")
def crear_perfil(**perfil):
    return perfil # diccionario
def pedir_notas():
    notas = []
    for i in range(3):
        try:
            nota = float(input("Ingrese sus 3 notas: "))
            notas.append(nota)
        except:
            print("Error de valor")
    return notas
def calcular_promedio(notas):
    return round(sum(notas)/len(notas))

def start():
    nombre = pedir_nombre()
    edad = pedir_edad()
    ciudad = pedir_ciudad()
    profesion = pedir_profesion()
    perfil = crear_perfil(
        nombre=nombre,
        edad = edad,
        ciudad=ciudad,
        profesion=profesion
    )
    perfil['notas'] = pedir_notas()
    perfil['promedio'] = calcular_promedio(perfil['notas'])
    print("=====================")
    print(f"Nombre: {perfil['nombre']}")
    print(f"Edad: {perfil['edad']}")
    print(f"Ciudad: {perfil['ciudad']}")
    print(f"Profesión: {perfil['profesion']}")
    print(f"Notas: {perfil['notas']}")
    print(f"Promedio: {perfil['promedio']}")
    print("=====================")
    
start()