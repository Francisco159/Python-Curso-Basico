### Lists

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [19, 24, 62, 30, 30, 17, 25]

print(my_list)
print(len(my_list))

my_other_list = ["Sung", "Jinwoo", 19, 1.80, "Coreano"]
print(my_other_list)

print(type(my_other_list))
print(type(my_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
print(my_other_list.count("Sung")) # cuenta cuantas veces aparece el elemento "Sung" en la lista
# print(my_other_list[6])  nos da un error porque el indice 6 no existe en la lista
#print(my_other_list[-6])  nos da un error porque el indice -6 no existe en la lista

lastname, name, age, height, country = my_other_list
print(name)

# concatenar listas
print(my_list + my_other_list)

# Funciones en listas
my_other_list.append("sungjinwoo10@gmail.com") # agrega un elemento al final de la lista
print(my_other_list)
my_other_list.insert(5, "85 KG") # agrega un elemento en la posicion 5 de la lista
print(my_other_list)
my_other_list[5] = "90 KG" # modifica el elemento en la posicion 5 de la lista
print(my_other_list)
my_other_list.remove("90 KG") # elimina el elemento "90 KG" de la lista
print(my_other_list)
my_list.remove(30) # elimina la primera aparicion del elemento 30 de la lista
print(my_list)

print(my_list.pop()) # elimina el ultimo elemento de la lista y lo devuelve
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element) # elimina el elemento en la posicion 2 de la lista y lo devuelve
print(my_list)

del my_list[1] # elimina el elemento en la posicion 1 de la lista
print(my_list)

my_new_list = my_list.copy() # crea una copia de la lista

my_list.clear() # elimina todos los elementos de la lista
print(my_list)
print(my_new_list)

my_new_list.reverse() # invierte el orden de los elementos de la lista
print(my_new_list)

my_new_list.sort() # ordena los elementos de la lista de menor a mayor
print(my_new_list)

print(my_new_list[1:2])