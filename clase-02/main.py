print('Clase 01 - Python Avanzado')

""" 
Crear un programa en Python que simule el registro de una compra (SIN FUNCIONES)

El programa debe:

1. Pedir al usuario su nombre (almaccenarlo en una variable) -> input()
2. Pedir el producto que desea comprar. -> input()
3. Pedir el precio unitario. -> input()
4. Pedir la cantidad.
5. Guardar los datos de la compra en un diccionario.
6. Calcular el subtotal (precio_unitario * cantidad)
7. Si el subtotal es mayor o igual a $50.000, aplicar un 10% de descuento (subtotal * 0.10)
8. Mostrar un resumen de la compra
9. Informar si el cliente obtuvo descuento

# DATOS DE ENTRADA ------------- #
Nombre: Ana
Producto: Teclado
Precio: 35000
Cantidad: 2

=========== RESUMEN DE COMPRA ========

Cliente: Ana
Producto: Teclado
Precio unitario: $35000
Cantidad: 2
Subtotal: $70000
Descuento: 10% si supera los $50000
Total: $63000

Obtuviste un descuento
"""

print("# ! Operadores... ")

print("# ! aritmeticos")

a = 10
b = 4

print(a + b)
print(a - b)
print(a * b)
print(a / b) 
print(a // b) # saca decimales. Devuelve el resultado entero -> 1.222222222 -> 1
print(a % b) # el resto de la división
print(a ** b) # eleva. potenciación. 10^4

print("# ! Comparación")
# devuelve un booleano luego de hacer la comparacicón
print( a == b) # False
print( a != b) # True
print( a > b) # True -> 10 > 4
print( a < b) # False -> 10 < 4
print( a >= b) # True -> 10 >= 4
print( a <= b) # False -> 10 <= 4

print("Lógicos -> and")

a = 10
b = 4

# and | or | not
# ------------------------ AND -> todas premisas deben ser verdaderas para que el resultaod sea verdadero
#           False
#      False and True
print(a == b and a != b)
#           True
#       True and True
print(a != b and a > b)

print("Lógicos -> or")
# ----------------------- OR -> Ambas premsisas deben ser falsas para que de como resultado false.
#           False
#      False or False
print(a < b or a <= b)
#          True
#      True or False
print(a != b or a < b)

print("Lógicos -> not")

print(not a != b) # True -> not True -> False

print("Ejemplo de operadores lógicos")

edad = 25
tiene_entrada = True
#                        True
#                  True     and  True
puede_ingresar = edad >= 18 and tiene_entrada
print(puede_ingresar) # True

edad = 15

es_menor = edad < 18
print(es_menor) # True
es_adulto = not es_menor
print(es_adulto) # False

print("Operador in")

frutas = ["manzana", "banana", "kiwi"]

print("pera" in frutas) # False
print("kiwi" in frutas) # True
print("piña" not in frutas) # True

# None

nombre = None

""" if nombre == None: # ! No es recomendable
    print('Es None: ', nombre) """ 

if nombre is None:
    print('No hay nombre')
    
apellido = 'Principe'

if apellido is not None:
    print('El contenido de la variable es: ', apellido)
    
""" 
None en python se asemeja a Null de JS. representa un valor que no tiene la variable a la cual le asigne None
"""

# Funciones útiles de Python

# * print() # Mostrar información
# * input() # Pedir datos
# * type() # Saber el tipo de dato
# * len() # Saber la cantidad de elementos
# * id() # obtener identificador del objeto id(nombre)
# * help() # Consultar documentación

# help(str)
# help(int)

# Conversión de tipos

int("25")          # 25
float("3.14")      # 3.14
str(100)           # "100"
bool(1)            # True
list("Python")     # ['P', 'y', 't', 'h', 'o', 'n']
tuple([1, 2, 3])   # (1, 2, 3)
set([1, 2, 2, 3])  # {1, 2, 3}

# Números

abs(-15)          # 15
round(3.14159, 2) # 3.14
pow(2, 3)         # 8
min(10, 5, 20)    # 5
max(10, 5, 20)    # 20
sum([10, 20, 30]) # 60

# Cadenas

texto = '    maxi prIncipe     ' # La variable texto es una instancia de la clase str
print(texto)
print(type(texto))

print(texto.upper()) # 'MAXI PRINCIPE'
print(texto.lower()) # 'maxi principe'
print(texto.capitalize()) # 'Maxi prIncipe'
print(texto.title()) # Maxi Principe

print(texto.strip()) # 'maxi prIncipe'
#print(texto.lstrip()) # 'maxi prIncipe     '
#print(texto.rstrip()) # '    maxi prIncipe'

cadena = 'Hola mundo'

print(cadena.find('mundo'))
print(cadena.find('chau')) # -1
print(cadena.index('mundo'))
# print(cadena.index('chau')) # substring not found

print('# ! REMPLAZAR')

print(cadena.replace('mundo', 'Maxi'))

print('# ! Crear una lista de elementos a partir de un cadena')

oracion = 'Hola que tal. Vengo a volar!'

palabras = oracion.split() # ' ' de separador

print(palabras)

csv = 'pedro,gomez,22'

print('# ! Crear una cadena de elementos a partir de una lista')

usuario = csv.split(',')

print(usuario)

print(' '.join(usuario))

# https://www.w3schools.com/Python/python_ref_string.asp

print('# ! startwith() y endswith()')

archivo = 'documento.pdf'

print(archivo.startswith('doc')) # True
print(archivo.endswith('.pdf')) # True
print(archivo.endswith('.exe')) # False

print('# ! -------------------- FUNCIONES -----------------------')

print('# ! Funciones con retorno')

""" cliente = input('Ingrese el nombre del cliente: ')
print('Bienvenido', cliente)
cliente = input('Ingrese el nombre del cliente: ')
print('Bienvenido', cliente)
cliente = input('Ingrese el nombre del cliente: ')
print('Bienvenido', cliente)
cliente = input('Ingrese el nombre del cliente: ')
print('Bienvenido', cliente)
cliente = input('Ingrese el nombre del cliente: ')
print('Bienvenido', cliente) """

def bienvenida_cliente():
    cliente = input('Ingrese el nombre del cliente: ') 
    saludo = f"Bienvenido {cliente}" 
    return saludo

""" print(bienvenida_cliente())
print(bienvenida_cliente())
print(bienvenida_cliente())
print(bienvenida_cliente()) """

print('# ! Funciones con parametros y retorno')

def sumar(a, b):
    return a + b

resultado = sumar(4, 5)
print(resultado)
print(resultado - resultado * .50)
print(sumar(7, 10))
print(sumar(16, 12))
print(sumar(22, 44))

print('# ! Funciones con parametros por defecto')

def saludar(nombre, saludo="Hola"):
    return f"{saludo} {nombre}"

print(saludar('Cinthia'))
print(saludar('Sabrina', 'Bienvenida'))

print('Funciones con *args (argumentos variables)')

def recibe_argumentos(num1, num2, num3, num4):
    print(num1)
    print(num2)
    print(num3)
    print(num4)
    print(num1 + num2 + num3 + num4)

# recibe_argumentos(1, 3, 4, 5)

def sumar(*argumentos): # args -> (num1, num2, num3, numN) <-- tupla
    print(argumentos)
    total = sum(argumentos)
    return total 

def promedio(*argumentos): 
    total = sum(argumentos)
    cantidad = len(argumentos)
    return total / cantidad
    
print(sumar(2, 3, 4, 5, 6, 7)) # 6
print(sumar(2, 3)) # 2
print(sumar(2, 83, 3, 43)) # 4
print('------')
print(promedio(3, 46, 43, 32))
print(promedio(2, 44))
print(round(promedio(65, 33, 12, 22, 23, 44), 2))

print('Funciones con **kwargs (argumentos nombrados) -> diccionarios')

def mostrar_datos(**datos):
    print(datos)
    
    
mostrar_datos(nombre="Juan", edad=30, ciudad="Buenos Aires")

""" 
# Desafío 1 — Sistema de calificaciones

Crear un programa que permita:

1. ingresar alumnos; [ { nombre: 'Juan', notas: [8,7,9] }, {}, {} ]
2. ingresar notas;
3. calcular promedio -> asumo que el alumno tenga 3 notas
4. determinar estado:
   - aprobado; -> mayor o igual a 6
   - desaprobado;
5. mostrar alumno con mayor promedio;
6. mostrar promedio general.

**Condición:** utilizar funciones y estructuras de datos.

-> Una lista de diccionarios.

-> ingresar_alumnos() (El nombre del alumno y las notas)
-> calcular_promedio(notas)
-> determinar_estado(promedio) # Si esta aprobado o no
-> mostrar_alumno(alumnos)
-> obtener_mejor_alumno(alumnos)
-> calcular_promeido_general(alumnos)
"""

def calcular_promedio(notas):
    sumatoria = sum(notas)
    cantidad = len(notas)
    promedio = sumatoria / cantidad
    promedio_rendondeado = round(promedio)
    return promedio_rendondeado

def determinar_estado(promedio):
    if promedio >= 6:
        return "Aprobado"
    else: 
        return "Desaprobado"
        

def ingresar_alumnos():
    
    alumnos = []
    
    cantidad = int(input("¿Cuántos alumnos desea ingresar? "))
    
    for i in range(cantidad): 
        print(f"Alumno {i + 1}")
        
        nombre = input("Nombre: ")
        
        notas = []
        
        for j in range(3):
            nota = float(input(f"Nota {j + 1}: "))
            notas.append(nota)
        
        # print(nombre)
        # print(notas)
        promedio = calcular_promedio(notas)
        estado = determinar_estado(promedio)
        
        alumno = {
            "nombre": nombre,
            "notas": notas,
            "promedio": promedio,
            "estado": estado
        }
        
        alumnos.append(alumno)
        
    # print(alumnos)
    return alumnos

def mostrar_alumno(alumno):
    print(f"Nombre: {alumno['nombre']}")
    print(f"Notas: {alumno['notas']}")
    print(f"Promedio: {alumno['promedio']}")
    print(f"Estado: {alumno['estado']}")
    print()

def mostrar_alumnos(alumnos):
    print('\n--- Alumnos ---')
    
    for alumno in alumnos:
       mostrar_alumno(alumno)

def obtener_mejor_alumno(alumnos):
    mejor = alumnos[0] # 8.0
    
    for alumno in alumnos:
        if alumno['promedio'] > mejor['promedio']:
            mejor = alumno
            
    return mejor

def calcular_promedio_general(alumnos):
    suma = 0
    
    for alumno in alumnos:
        suma += alumno['promedio']
        
    cantidad_alumnos = len(alumnos)
    return suma / cantidad_alumnos

# Programa principal

def start():
    alumnos = ingresar_alumnos()
    mostrar_alumnos(alumnos)
    mejor_alumno = obtener_mejor_alumno(alumnos)
    print('---_ MEJOR ALUMNO _---')
    mostrar_alumno(mejor_alumno)
    promedio_general = calcular_promedio_general(alumnos)
    print(f"Promedio general: {promedio_general:.2f}")

# start()

print('# ! Gestión de errores (Excepciones)')
# Un programa puede encontrarse con situaciones inesperadas

# * El usuario indroduce texto cuando esperamos un número
# * Un archivo no existe
# * Intentamos dividr por cero.
# * Accedemos a posiciones inexistentes
# * Una clave no existe en un diccionario

print('Inicio del programa')

numero = 10
divisor = 0 # ZeroDivisionError: division by zero

# resultado = numero / divisor
print('# ! try/except')

try: # se intentan
    resultado = numero / divisor
except ZeroDivisionError:
    print('No se puede dividir por cero')
    divisor = 5
    resultado = numero / divisor
    print(resultado)
    
print('Fin del programa')

print('# ! Casteo inválido')
""" print('Inicio del programa')
try:
    edad = int(input("Ingrese su edad: ")) # ValueError: invalid literal for int() with base 10: 'Maxi'
    print(edad)
except ValueError:
    print('Debe ingresar un número')
    
print('Fin del programa') """

print('# ! Varias excepciones')

print('Inicio de programa')
try: 
    numero = int(input("Ingrese número: "))
    resultado = 100 / numero
    print(f"{resultado:.2f}")
except ValueError:
    print("Debe ingresar un número")
except ZeroDivisionError:
    print('El número no puede ser cero')
        
print('Fin de programa')