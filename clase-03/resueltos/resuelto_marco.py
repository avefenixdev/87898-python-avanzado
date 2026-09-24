def validar_edad(edad):
    if edad <= 18:
        raise ValueError("Debe ser mayor de edad")
def crear_usuario(nombre, edad,ciudad, profesion):
    print(f"Nombre: {nombre} \nEdad: {edad} \nCiudad: {ciudad} \nProfesion: profesion")
def calcular_promedio(notas):
    return round(sum(notas)/len(notas),2)
def cargar_notas(tam):
    notas = []
    for i in range(tam):
            nota = int(input(f'Ingrese la nota {i+1}: '))
            notas.append(nota)
    return notas

def sistemaNotas():
    try:
        nombre = input('Ingrese el nombre: ')
        edad = int(input('Ingrese la edad: '))
        ciudad = input('Ingrese la ciudad: ')
        profesion = input('Ingrese la profesion: ')
        validar_edad(edad)
        datos_usuario = {
            "nombre": nombre,
            "edad":edad,
            "ciudad": ciudad,
            "profesion": profesion
        }
        tam = 3
        notas = cargar_notas(tam)
        
        promedio = calcular_promedio(notas)
    except ValueError as error:
        print('ERROR:', error)
    else:
        print('========================')
        crear_usuario(**datos_usuario)
        print(notas)
        print(f'Promedio: {promedio}')
        print('========================')
sistemaNotas()