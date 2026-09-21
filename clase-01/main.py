print('Clase 01 - Python Avanzado')

"""
! Python es un lenguaje

* Alto nivel.
* Interpretado.
* Dinámicamente tipado. -tipado dinámico- (Fuertemente tipado -tipado estático-)
* Sitaxis sencilla.
* Multiproposito -> Inicialmente se usaba para scripting
* Gran comunidad

! Nos permite hacer

* Desarrollo Web
* Ciencia de datos
* Scripting (Administración de sistema)
* Backend
* Cyber Seguridad
* Video Juegos
* Automatizaciones
* Inteligencia artificial
* App de escritorio

! Links útiles
* https://www.python.org.ar/
* https://pypi.org/
"""

"""
! print -> Permite imprimir en terminal/consola
"""

print('Hola tarolas')

print( 10 + 20 )

nombre = "Maxi"
version = 3.14

print(nombre)
print(version)

""" IMPORTANTE: El programa ser interpretado. Las sentencias se ejecutan de arriba para abajo y de izquierda a derecha """

""" ! VARIABLES """

nombre = "Luis"; """ cadena """
edad = 33; """ número entero """
edad = 1.80; """ número decimal """

""" Podemos en Python cambiar el valor de una variable """

""" ! Reasignación """

print(edad)
edad = 22;
print(edad);
edad = 44;
print(edad);

contador = 0;
contador = contador + 1
contador = contador + 1

print(contador); """ 2 """

contador += 1

print(contador); """ 3 """

print('Entrada de datos por el usuario')

nombre = input('Ingrese su nombre: ')

print("Hola", nombre, "!")
print("Hola " + nombre + '!')
print(f"Hola {nombre}!") # <---- Está es la que vamos a usar
print("Hola %s!" % nombre)

""" Ingresamos la edad """

edad_input = input('Edad:')
print(type(edad_input)); """ cadena """
print(edad_input) # 22

""" ¿Cómo averiguamos el tipo de dato de una variable"""
""" Con la función type() """

print(""" Casteando la edad """)

edad_ingresada = int(input("Edad: ")) # Casteamos la cadena a un entero
print(type(edad_ingresada)) # número
print(edad_ingresada)


""" ¿Qué tipos de datos tiene Python? """

""" 
* int
* float
* str
* bool
* None

type()
"""

""" 
Ejercicio 1 - Usando type()

nombre = 'Maxi'
edad = 35
altura = 1.78
es_programdor = True

////////////////////////
Ejercicio 2 - Casteo

Ingresar un nombre - ¿Hay que castearlo?

Ingresan un número entero ¿Hay que castearlo? ¿Cómo lo casteo?


Ingresan un número decimal ¿Hay que castearlo? ¿Cómo lo casteo?

Ejercicio 3 - None

Explicar con sus palabras, investigando para que podría servir el tipo None.
Hacer ejemplo del uso de None y utilizar el type

"""

print(' # ! Estructuras de datos')


"""
* Listas -> (list) -> Guardan varios valores en un orden fijo -> []

* Tuplas (tuple) -> Son parecidas a la listas pero tiene un orden y aceptan repetidos -> () 

* Diccionarios (dict) -> Guardan datos en parejas de clave, valor. No siguen un orden especifico {}

* Conjuntos (set) -> Guardan elementos únicos sin orden. No permiten que se repita un valor. -> {}
"""

print('Listas - (list)')
# Una lista sirve para cuando tenemos varios elementos y el orden importa. Es una estructura indexada la lista.

print('Imprimiendo la lista')
frutas = ["manzana", "banana", "pera", "naranja"]

print(frutas)

print('Accediendo a una posición especial')
print(frutas[0]) # manzana
print(frutas[2]) # pera

print('Modificar banana de la lista')

frutas[1] = "kiwi" # banana va a ser remplazado por kiwi

print(frutas)

print('Agregando un valor a lista')

frutas.append('frutilla')

print(frutas)

""" 
! ¿Cuándo usar la listas?

* Cuando tenemos elementos similares
alumnos = ["Juan", "Pedro", "Ana", "Lucía"]
precios = [1500, 2000, 3500, 1200]
notas = [8, 7, 10, 6]

* Cuando necesito matener una secuencia
pasos = [
    "Iniciar sesión",
    "Seleccionar producto",
    "Pagar",
    "Confirmar pedido"
]

* Muchos elementos y quiero manejarlos como una secuencia.
"""

print('Tuplas (tuple)')
# Es parecida a una lista pero no se puede modificar después de crearla.

coordenadas = (10, 20)

print('Accediendo a los valores')

print(coordenadas[0]) # 10 <--- latitud
print(coordenadas[1]) # 20 <--- longitud
#     red green blue
rgb = (255, 0, 0) # rojo

print('Mostrando rgb')

print(rgb)
print(rgb[0]) # red
print(rgb[1]) # green
print(rgb[2]) # blue

print('Datos de una persona dentro de una tupla')
#          'nombre'
#            0      1       2 
persona = ('Maxi', 22, 'Argentina')

print(persona[0]) # Maxi
print(persona[1]) # 22
print(persona[2]) # Argentina

dias_semana = (
    "lunes",
    "martes",
    "miercoles",
    "jueves",
    "viernes",
    "sábado",
    "domingo"
)

for dia in dias_semana:
    print(dia)
    

print('Desempaquetado de una tupla') # destructuracción

def obtener_usuario():
    tuplaUsuario = ("Maxi", 22)
    #return "Maxi", 22
    return tuplaUsuario

nombre, edad = obtener_usuario()
print(nombre, edad)
tuplaUsuario = ("Maxi", 33)
nombre, edad = tuplaUsuario
print(nombre, edad)

# ! ¿Cuándo usar una tupla?
# * Cuando hay varios valores relacionados
# * Orden definido
# * Cuando no queres que la colección sea modificada

# ! dict (Diccionarios)
# * Almacena información a través de claves y valores
usuario = {
    "nombre": "Maxi",
    "edad": 35,
    "profesion": "Docente"
}

print(usuario)

print('Accedemos a través de las claves')
print(usuario["nombre"]) # bracket notation
print(usuario["edad"]) # bracket notation
print(usuario["profesion"]) # bracket notation

print('Modificamos el valor de alguna clave (edad)')

usuario["edad"] = 22
print(usuario)

print('Agregar una key al objeto')

usuario['ciudad'] = "Buenos Aires"
print(usuario)

# ! ¿Cuándo usamos un diccionario
# * Cuando necesitamos representar una entidad mediante propiedades (caracteristicas)
# * Cuando tengo información definidad mediante clave/valor.

print('set -> Conjunto')
# * Voy a usar un set cuando quiera tener dentro elementos únicos

numeros = { 3, 4, 5, 3, 2, 4, 5, 6, 8, 50}

print(numeros) # duplicados desaparecen

# Caso de uso tipico

usuarios = [
    "Juan",
    "Pedro",
    "Juan",
    "Ana",
    "Pedro"
]

print(usuarios) # Lista

usuarios_unicos = set(usuarios) # una lista en un set

print(usuarios_unicos) # Solo me quedaron los usuarios que no se repiten

print('Operaciones de conjuntos')

python = { "Juan", "Pedro", "Ana" }
javascript = { "Pedro", "Ana", "Lucía" }

print('# personas que hicieron ambos cursos')

print(python & javascript)

print('# personas que conocen Python o Javascript')

print(python | javascript)

# ! ¿Cuándo usamos un set?

# * evitar duplicados
# * comprobar pertenencia
# * realizar operaciones de conjuntos

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