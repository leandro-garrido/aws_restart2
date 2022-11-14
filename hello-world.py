"""
Your module description
"""

# print('Hello World!')

integer = 4 # numeros enteros
flotantes = 3.14 # numeros decimales
booleanos= True # True o False
cadenas = 'Hola mundo!'

edad = input('Ingresa tu edad: ')
print(type(edad))
edad = int(edad)
# str(x) / float(x) / bool(x) / int(x)
print(type(edad))
if edad > 18:
    print('pasa capo')
else:
    print('nop')
    