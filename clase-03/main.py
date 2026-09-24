print("Clase 03 - Python Avanzado")

""" print("Inicio de programa")
try:
    numero = int(input("Ingrese un número: "))
    divisor = int(input("Ingrese el divisor: "))
    resultado = numero / divisor
    print(resultado)
except ValueError as error:
    print("Debe ingresar un número. ERROR:", error)
except ZeroDivisionError as error:
    print("El divisor no puede ser cero. ERROR:", error)
print("Fin de programa") """

print('bloque else') # se ejecuta cuando el bloque 'try' termina correctamente

""" print("Inicio de programa")
try:
    numero = int(input("Numero: "))
except ValueError:
    print("Número inválido")
else:
    print("Número correcto")
    print(numero)
print("Fin de programa") """

print('bloque finally') # Se ejecuta siempre en el flujo normal de ejecución, tanto no hay una excepcion o si hay una excepción

print("Inicio de programa")
try:
    print('# Abro el archivo.')
    print('# Intento escribir en el archivo -> Falla <---- No función, se lanza la excepción')
    
except Exception:
    print('# No se pudo escribir el archivo')
finally:
    print('# Cierro el archivo')
    
print("Fin de programa")

""" 
try:
    # código que puede generar una excepción
except ValueError:
    # manejar ValueError
except ZeroDivisionError:
    # manejar ZeroDivisionError
else:
    # se ejecuta si no hubo excepción
finally:
    # siempre se ejecuta
"""

print("Lanzar excepciones con 'raise'")
# Permite generar una excepción manualmente -> el throw (js)

try:
    
    edad = -5

    if edad < 0:
        raise ValueError('La edad no puede ser negativa')

except ValueError as error:
    print('ERROR:', error)
    
# Dentro de funciones

def validar_edad(edad):
    if edad <= 18:
        raise ValueError("Debe ser mayor de edad")

# bloque principal
print('Inicio del programa')
try:
    validar_edad(20)
    print('Siguiente paso')
except ValueError as error:
    print('ERROR:', error)
print('Fin del programa')  
