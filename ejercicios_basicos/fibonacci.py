# FIBONACCI


""" Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
  la que el siguiente siempre es la suma de los dos anteriores.
  0, 1, 1, 2, 3, 5, 8, 13...
"""

def fibonacci(number_iter: int):
    number_one = 0
    number_two = 1
    for element in range(number_iter):
        print(number_one, end=" ")
        number_one, number_two = number_two, number_one + number_two
    
fibonacci(50)