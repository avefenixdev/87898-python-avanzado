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

# Clases de 3 productos (PC, Monitor, Mouse) 1-2 caracteresticas

class Animal:
    
    def __init__(self, nombre, edad, peso):
        # Atributos
        self.__nombre = nombre
        self.__edad = edad
        self.__peso = peso
    
    def comer(self):
        print(f"{self.__nombre} está comiendo")
        
    def dormir(self):
        print(f"{self.__nombre} está durmiendo")
        
    def hacer_sonido(self):
        print(f"{self.__nombre} está haciendo un sonido")
    
    # Getter de nombre
    @property
    def nombre(self):
        return self.__nombre
    # Setter de nombre
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
        
    # Getter de edad
    @property
    def edad(self):
        return self.__edad
    # Setter de edad
    @edad.setter
    def edad(self, nuevo_edad):
        self.__edad = nuevo_edad
        
    # Getter de peso
    @property
    def peso(self):
        return self.__peso
    # Setter de peso
    @peso.setter
    def peso(self, nuevo_peso):
        self.__peso = nuevo_peso

# HERENCIA ---- Nos permite heredar de una Clase Base. Clase Padre

class Tigre(Animal):
    
    def __init__(self, nombre, edad, peso):
        super().__init__(nombre, edad, peso)
    
    # poo -> sobreescritura
    def hacer_sonido(self):
        print(f"{self.nombre} ruge")
        
class Leon(Animal):
    
    def __init__(self, nombre, edad, peso, tiene_melena):
        super().__init__(nombre, edad, peso)
        self.__tiene_melena = tiene_melena
    
    def hacer_sonido(self):
        print(f"{self.nombre} ruge fuertemente")
        
    # Getter de tiene_melena
    @property
    def tiene_melena(self):
        return self.__tiene_melena
    # Setter de tiene_melena
    @tiene_melena.setter
    def tiene_melena(self, nuevo_tiene_melena):
        self.__tiene_melena = nuevo_tiene_melena
        
class Gato(Animal):
    
    # sobreescribimos el constructor de animal
    def __init__(self, nombre, edad, peso, es_mascota, color):
        super().__init__(nombre, edad, peso)
        self.__es_mascota = es_mascota
        self.__color = color
    
    def hacer_sonido(self):
        print(f"{self.nombre} maúlla")
        
    # Getter de es_mascota
    @property
    def es_mascota(self):
        return self.__es_mascota
    # Setter de es_mascota
    @es_mascota.setter
    def es_mascota(self, nuevo_es_mascota):
        self.__es_mascota = nuevo_es_mascota
        
    # Getter de color
    @property
    def color(self):
        return self.__color
    # Setter de color
    @color.setter
    def color(self, nuevo_color):
        self.__color = nuevo_color
        
# Programa principal

tigre = Tigre("Tiger", 8, 150)
leon = Leon("Alex", 5, 190, True)
gato = Gato("Garfield", 3, 5, True, "Naranjoso")

# Atributos
print(tigre.nombre) 
print(tigre.peso)

print(leon.nombre)
print(leon.tiene_melena)

print(gato.nombre)
print(gato.color)
print(gato.es_mascota)

# setters
gato.nombre = "Chatran"
print(gato.nombre)

# Métodos

tigre.hacer_sonido()
leon.hacer_sonido()
gato.hacer_sonido()