class Producto:
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
    def aplicar_descuento(self):
        porcentaje = 0.10
        descuento = self.precio * porcentaje 
        return self.precio - descuento
    def mostrar(self):
        return f"{self.nombre}, {self.categoria}, {self.aplicar_descuento()}"
    
    def __str__(self):
        return f"{self.nombre}, {self.precio}"
pc = Producto("PC", "Informatica", 3000)
monitor = Producto("Monitor", "Informatica", 2500)
mouse = Producto("PC", "Informatica", 1000)
print(pc.nombre)
print(pc.mostrar())
print(pc)