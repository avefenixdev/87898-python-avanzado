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