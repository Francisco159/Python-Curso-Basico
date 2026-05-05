### LOOPS

# While
my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else: # Es opcional
    print("La condicion es mayor o igual que 10")
    
print("La ejecucino continua")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Mi condicion es 15")
        break
    print(my_condition)
    
# For

my_list = [19, 24, 62, 30, 30, 17, 25]
my_tuple = (19, 1.80, "Sung", "Jinwoo", "Sung")
my_set = {"Kotlin", "Python", "Java", "C#"}
my_other_dict = {
    "Name": "Jinwoo",
    "lastname": "Sung",
    "Age": 19,
    1: "Python"
}

for element in my_list:
    print(element)

for element in my_tuple:
    print(element)

for element in my_set:
    print(element)

for element in my_other_dict:
    print(element)
    if element == "Age":
        break
else:
    print("Se han recorrido todos los elementos del diccionario")
    
for element in my_other_dict:
    print(element)
    if element == "Age":
        continue
    print("se ejecuta")    
else:
    print("Se han recorrido todos los elementos del diccionario")