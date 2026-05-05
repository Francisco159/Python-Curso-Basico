### DICTIONARIES

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {
    "Name": "Jinwoo",
    "lastname": "Sung",
    "Age": 19,
    1: "Python"
}

my_dict = {
    "Name": "Jinwoo",
    "lastname": "Sung",
    "Age": 19,
    "Language": {"Python", "C++", "Java"},
    1: 1.80
}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Name"])

my_dict["Name"] = "Hades"
print(my_dict["Name"])

my_dict["City"] = "Seoul"
print(my_dict)

del my_dict["City"]
print(my_dict)

print("City" in my_dict)
print("Language" in my_dict)
print("Sung" == my_dict["lastname"])

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ["Name", "lastname", "Age"]
my_new_dict = dict.fromkeys(my_list)
print(my_new_dict)
my_new_dict = dict.fromkeys(("Name", "lastname", "Age"))
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)

my_values = my_dict.values()
print(type(my_values))
print(my_new_dict.values())
print(tuple(my_dict))
print(set(my_dict))
print(list(my_dict.values()))