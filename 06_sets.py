### SETS

my_set = set()
my_other_set = {}

print(type(my_set)) # <class 'set'>
print(type(my_other_set)) # Inicialmente <class 'dict'>

my_other_set = {"Sung", "Jinwoo", 19, 1.80}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("Hades")
print(my_other_set)  # un set no es una estructura ordenada

my_other_set.add("Hades") # un set no permite elementos duplicados
print(my_other_set)

print("Hades" in my_other_set) # True
print("Hodes" in my_other_set) # False

my_other_set.remove("Hades")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set 
#print(my_other_set) # NameError: name 'my_other_set' is not defined

my_set = {"Sung", "Jinwoo", 19, 1.80}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Kotlin", "Python", "Java", "C#"}

my_new_set = my_set.union(my_other_set)
print(my_new_set)

print(my_new_set.difference(my_set))