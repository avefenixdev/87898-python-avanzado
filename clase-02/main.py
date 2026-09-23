print('Clase 01 - Python Avanzado')

""" 
Crear un programa en Python que simule el registro de una compra

El programa debe:

1. Pedir al usuario su nombre (almaccenarlo en una variable) -> input()
2. Pedir el producto que desea comprar. -> input()
3. Pedir el precio unitario. -> input()
4. Pedir la cantidad.
5. Guardar los datos de la compra en un diccionario.
6. Calcular el subtotal
7. Si el subtotal es mayor o igual a $50.000, aplicar un 10% de descuento
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

