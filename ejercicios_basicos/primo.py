# NUMEROS PRIMOS

"""
Escribe un programa que se encargue de comprobar si un numero es primo o no.
Hecho esto, imprime los numeros primos entre el 1 y 100
"""

def verificar_primo(number: int):
    count_div = 0
    for element in range(number):
        if (number % (element + 1)) == 0:
            #print(f"number:{number}, divisor:{element + 1}")
            count_div += 1
    
    if count_div == 2:
        return True
    else:
        return False

def es_primo(number: int):
    if verificar_primo(number) == True:
        print(f"El numero {number} SI es numero primo")
    else:
        print("El numero {number} NO es numero primo")

def imprimir_primos_entre_1_y_100():
    for element in range(100):
        if verificar_primo(element + 1) == True:
            print(element + 1, end=" ")

# CODIGO PRINCIPAL
if __name__ == "__main__":
    es_primo(5)
    imprimir_primos_entre_1_y_100()