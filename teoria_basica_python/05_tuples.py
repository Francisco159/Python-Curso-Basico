### TUPLES

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (19, 1.80, "Sung", "Jinwoo", "Sung")
my_other_tuple = (19, 29, 40, 55)

print(my_tuple)
print(type(my_tuple))
print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Sung"))
print(my_tuple.index(1.80))

# my_tuple[0] = 20 nos da un error porque las tuplas son inmutables
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple) # concatenar tuplas

print(my_sum_tuple[2:5]) # slicing de tuplas

my_list = list(my_tuple) # convertir tupla a lista
print(type(my_list))

my_list[4] = "South Korea" # modificar el elemento en la posicion 4 de la lista
my_list.insert(1, 'azul') # agregar un elemento en la posicion 1 de la lista
my_tuple = tuple(my_list) # convertir lista a tupla
print(my_tuple) 

del my_tuple # eliminar la tupla