# EJERCICIO: ANAGRAMA

"""
Escribe una funcion que reciba dos palabras (string)
y retorne verdadero o falso (Bool) segun sean o no
anagramas.
- Un anagrama consiste en formar una palabra 
reordenando TODAS las letras de otra palabra inicial.
- No se hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.     
"""

# Definicion de funciones
def es_anagrama(palabra_1: str, palabra_2: str):
    list_palabra_1 = list(palabra_1.upper())
    list_palabra_2 = list(palabra_2.upper())
    
    list_palabra_1.sort()
    list_palabra_2.sort()
    
    if palabra_1.upper() == palabra_2.upper():
        print("Son palabras iguales por lo que No forman un anagrama")
    
    elif list_palabra_1 == list_palabra_2:
        print(f"Las palabras {palabra_1} y {palabra_2} si forman un anagrama")
    

# Defincinoes de variables
palabra_1 = "Roma"
palabra_2 = "Amor"

#llamada de las funciones
es_anagrama(palabra_1, palabra_2)