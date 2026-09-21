def ejercicio_uno():
    nombre = 'Maxi'
    edad = 35
    altura = 1.78
    es_programador = True
    print("nombre: ",  type(nombre), "edad: ", type(edad), "altura: ", type(altura), "es_programador: ", type(es_programador))
ejercicio_uno()
def ejercicio_dos():
    nombre_input = input("Ingrese su nombre: ")
    entero_input = int(input("Ingrese un numero entero: "))
    decimal_input = float(input("Ingrese un numero decimal: "))
    print(nombre_input)
    print(entero_input)
    print(decimal_input)
ejercicio_dos()
lista_numeros = [2,5,7,4,3]
def ejercicio_tres(lista):
    mayor = None
    print(type(mayor))
    for i in lista:
        if mayor == None:
            mayor = i
        elif i > mayor:
            mayor = i
    return mayor
numero_mayor = ejercicio_tres(lista_numeros)
print(type(numero_mayor))
print(f"El numero mayor es {numero_mayor}")