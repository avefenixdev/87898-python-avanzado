class Producto:
    
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
    
    def aplicar_descuento(self):
        descuento = self.precio * 10 / 100
        self.precio = self.precio - descuento
    
    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Categoría: {self.categoria}")
        print(f"Preci: ${self.precio}")
    
    def __str__(self):
        return f"{self.nombre} - ${self.precio}"

class PC(Producto):
    
    def __init__(self, nombre, categoria, precio, procesador, ram):
        super().__init__(nombre, categoria, precio)
        self.procesador = procesador
        self.ram = ram

class Monitor(Producto):
    
    def __init__(self, nombre, categoria, precio, pulgadas, resolucion):
        super().__init__(nombre, categoria, precio)
        self.pulgadas = pulgadas
        self.resolucion = resolucion

class Mouse(Producto):
    
    def __init__(self, nombre, categoria, precio, dpi):
        super().__init__(nombre, categoria, precio)
        self.dpi = dpi

pc = PC("PC Gamer", "Computacion", 1_500_000, "AMD Ryzen 7 9800X3D", "32 GB")
monitor = Monitor("Monitor Samsung", "Perifericos", 400_000, 24, "Full HD")
mouse = Mouse("Mouse Logitech", "Perifericos", 60_000, 12_000)

print(pc.nombre)
print(pc.procesador)
print(pc.ram)

print(monitor.nombre)
print(monitor.pulgadas)
print(monitor.resolucion)

print(mouse.nombre)
print(mouse.dpi)

pc.aplicar_descuento()
monitor.aplicar_descuento()
mouse.aplicar_descuento()

pc.mostrar()
monitor.mostrar()
mouse.mostrar()
