print("Paradigma orientado a objetos")

""" 
La **Programación Orientada a Objetos (POO)** es un paradigma que
propone organizar un programa alrededor de objetos.

Un objeto representa una entidad que posee:

-   **estado:** los datos que almacena;
-   **comportamiento:** las operaciones que puede realizar.

"""

""" 
Cuenta Bancaria
    Estados
        titular
        saldo
        numero
        
    Comportamientos
        despositar()
        retirar()
        consultar_saldo()

"""

class Persona:
    
    # Método constructor -> Siempre se ejecuta cuando creo una instancia
    # En JAVA cuando haciamos new se creaba la instancia y ejecuta el método constructor. En Python no tenemos esa palabra reservada.
    # this -> self
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        print(f"Hola, soy {self.nombre}")
    
    # sobreescribiendo el método __str__ de Object
    def __str__(self):
        return f"{self.nombre} tiene {self.edad} años"
        
        
persona1 = Persona("Romina", 25)
persona2 = Persona("Laura", 34)

print(persona1 is persona2)
print(persona1)
print(persona2)

persona1.saludar()
persona2.saludar()

# Otra clase más para poder crear Objetos

class Rectangulo:

    # atributos
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    # métodos
    def calcular_area(self):
        return self.ancho * self.alto
    
    def calcular_perimetro(self):
        return 2 * (self.ancho + self.alto)
    
    # sobreescribiendo __str__ de object
    def __str__(self):
        return f"El ancho es de {self.ancho} y el alto es de {self.alto}"
    

rectangulo1 = Rectangulo(10, 5)
rectangulo2 = Rectangulo(53, 20)

print(f"Area rectangulo 1: {rectangulo1.calcular_area()}")
print(f"Area rectangulo 2: {rectangulo2.calcular_area()}")
print(f"Perimetro del rectangulo 1: {rectangulo1.calcular_perimetro()}" )
print(f"Perimetro del rectangulo 2: {rectangulo2.calcular_perimetro()}" )
print(rectangulo1)
print(rectangulo2)

# Enunciado.
# 1. Crear una clase (molde) producto
# 2. Tiene tener un constructor para inicializar el nombre, categoria y precio del producto
# 3. aplicar_descuento() -> Tiene que tener el comportamiento para poder aplicar descuento.
# Producto con 10% de descuento
# descuento = precio * porcentaje / 100 
# precio = precio - descuento
# 4. mostrar() -> Otro comportamiento que va a mostrar en la consola El nombre del producto, 
# la categoría y el precio con descuento
# 5. Crear el __str__ para mostrar el nombre y el precio.

# Averiguar como hacer herencia en Python y como crear una clase abstracta. (Googlear buscando la solución con la IA)