# Ejercicio Fizz-Buzz

"""
Descripcion:
Escribe un programa que muestre por consola (con un print) los numeros
del 1 a 100 (ambos incluidos y con un salto de linea entre cada impresion),
sustituyendo los siguientes:
- Multiplos de 3 por la palabra "fizz"
- Multiplos de 5 por la palabra "buzz"
- Multiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".    
"""

for element in range(100):
    number = element + 1
    
    if ((number % 3) == 0) == True and ((number % 5) == 0) == True:
        print("fizzbuzz")
    elif ((number % 3) == 0) == True:
        print("fizz")
    elif ((number % 5) == 0) == True:
        print("buzz")
    else:
        print(number)