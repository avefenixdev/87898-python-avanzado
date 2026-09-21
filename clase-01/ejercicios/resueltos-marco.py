""" Ejercicio 1 """
nombre = 'Maxi'
edad = 35
altura = 1.78
es_programdor = True
print(f'{nombre} --- {type(nombre)}')
print(f'{edad} --- {type(edad)}')
print(f'{altura} --- {type(altura)}')
print(f'{es_programdor} --- {type(es_programdor)}')
""" Ejercicio 2 """
nombreUser = input('Ingrese su nombre: ')
print(f'{nombreUser} --- {type(nombre)}')
print('Cuando ingresamos un nombre no hay que castearlo ya que el input devuelve un str por defecto. En cambio, si ingresamos un numero si hay que hacer un casteo ya que en vez de devolver un int va a devolver un str')
edadUser = int(input('Ingrese su edad: '))
print(f'{edadUser} --- {type(edadUser)}')
""" Ejercicio 3  """
print('el tipo de datos none sirve para representar que no hay nada dentro de una variable, que el dato es nulo')
datoNulo = None
print(f'{datoNulo} --- {type(datoNulo)}') # NoneType