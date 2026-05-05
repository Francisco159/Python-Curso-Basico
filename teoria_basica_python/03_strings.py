### STRINGS

my_string = "my string"
my_other_string = 'my other string'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_string = "este es un string\ncon salto de linea"
print(my_new_string)

my_new_string = "\teste es un string con tabulacion"
print(my_new_string)

my_new_string = "\\teste es un string\\ncon escapado"
print(my_new_string)

# Formateo de strings
name, lastname, age = "Sung", "Jinwoo", 19
print("mi nombre es {} {} y tengo {} años".format(name, lastname, age))
print("mi nombre es %s %s y tengo %d años" %(name, lastname, age))
print("mi nombre es " + name + " " + lastname + " y tengo " + str(age) + " años")
print(f"mi nombre es {name} {lastname} y tengo {age} años")

# Desempaquedao de caracteres

lenguaje = "python"
a, b, c, d, e, f = lenguaje
print(a)
print(b)

# Division de strings

lenguaje_slice = lenguaje[1:3] # nos da el rango de 1 a 3 sin incluir el 3
print(lenguaje_slice)

lenguaje_slice = lenguaje[1:] # nos da el rango de 1 hasta el final del string
print(lenguaje_slice)

lenguaje_slice = lenguaje[-2] # empieza por el final del string y nos da el segundo caracter
print(lenguaje_slice)

lenguaje_slice = lenguaje[0:6:2] # nos da el rango de 0 a 6 sin incluir el 6 y con un paso de 2
print(lenguaje_slice)

# Reversar un string

reverser_lenguaje = lenguaje[::-1]
print(reverser_lenguaje)

# Funciones 
print(lenguaje.capitalize()) # convierte la primera letra en mayuscula
print(lenguaje.upper()) # convierte todas las letras en mayuscula
print(lenguaje.count("t")) # cuenta cuantas veces aparece el caracter "t"
print("23".isnumeric()) # verifica si el string es un numero
print(lenguaje.lower()) # convierte todas las letras en minuscula
print(lenguaje.upper().isupper()) # verifica si todas las letras son mayusculas
print(lenguaje.startswith("py")) # verifica si el string empieza con "py"