nombre = input("Nombre: ")
try:
    edad = int(input("Edad: "))
    if edad <= 0:
        raise ValueError('La edad no puede ser 0 o menor, vuelva a introducir su edad')
except ValueError as error:
    print("ERROR:", error)
    edad = int(input("Edad: "))
ciudad = input("Ciudad: ")
profesion = input("Profesión: ")
perfil = {
    "nombre": nombre,
    "edad": edad,
    "ciudad": ciudad ,
    "profesion": profesion
}
def calcularPromedio(notas):
    return sum(notas) / len(notas)
notas = []

for i in range(3):
    try:
        nota = float(input("Ingrese una nota: "))
        if nota < 0:
            raise ValueError('La nota debe ser mayor a 0, vuelva a ingresar su nota')
    except ValueError as error:
        print("ERROR:", error)
        nota = float(input("Ingrese una nota: "))
    finally:
        notas.append(nota)
promedio = calcularPromedio(notas)
print("-----------------------------------------")
print("Nombre:", perfil["nombre"])
print("Edad:", perfil["edad"])
print("Ciudad:", perfil["ciudad"])
print("Profesión:", perfil["profesion"])
print("Notas:", notas)
print("Promedio:", promedio)
print("-----------------------------------------")