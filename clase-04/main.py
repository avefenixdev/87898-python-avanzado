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

# 3 productos (PC, Monitor, Mouse) 1-2 caracteresticas

class Animal:
    
    def __init__(self, nombre, edad, peso):
        # Atributos
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
    
    def comer(self):
        print(f"{self.animal} está comiendo")
        
    def dormir(self):
        print(f"{self.nombre} está durmiendo")
        
    def hacer_sonido(self):
        print(f"{self.nombre} está haciendo un sonido")

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
        self.tiene_melena = tiene_melena
    
    def hacer_sonido(self):
        print(f"{self.nombre} ruge fuertemente")
        
class Gato(Animal):
    
    # sobreescribimos el constructor de animal
    def __init__(self, nombre, edad, peso, es_mascota, color):
        super().__init__(nombre, edad, peso)
        self.es_mascota = es_mascota
        self.color = color
    
    def hacer_sonido(self):
        print(f"{self.nombre} maúlla")
        
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

# Métodos

tigre.hacer_sonido()
leon.hacer_sonido()
gato.hacer_sonido()