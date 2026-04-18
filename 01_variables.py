# variables

#variable de tipo string
my_string_variable = "my string variable"
print(my_string_variable)
    
#variable de tipo entero   
my_int_variable = 45
print(my_int_variable)

# usar funcion str() para convertir un numero a string
my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)

#variable de tipo booleano
my_bool_variable = True
print(my_bool_variable)

#imprimir con diferentes parametros en print()
print(my_string_variable, my_int_variable, my_bool_variable)
print("Este es el valor de mi variable booleana: ", my_bool_variable)

# Algunas Funciones del sistema
print(len(my_int_to_str_variable)) # longitud de la variable

# variables en  una sola linea
name, lastname, alias, age = "John", "Doe", "JD", 30
print(name, lastname, alias, age)

# usar input() para pedir datos al usuario en consola
"""first_name = input("What is your first name? ")
age = input("how old are you? ")
print("Your name is: ", first_name)
print("Your age is: ", age)"""

# cambiar el valor de una variable
name = 35
lastname = "Smith"

# forma de especificar el tipo de dato que queremos que sea una variable. NOTA: aun con esto el tipo puede camnbiar
address: str = "mi direccion"