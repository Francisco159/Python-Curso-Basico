### FUNCTIONS

def my_function():
    print("Hello from a function")
    
my_function()
my_function()
my_function()

def sum_two_values(first_number, second_number):
    print(first_number + second_number)
    
sum_two_values(5, 10)
sum_two_values(23534,235523)
sum_two_values("5", "10")

def sum_two_values_with_return(first_number, second_number):
    return first_number + second_number

suma = sum_two_values_with_return(5, 10)
print(suma)

def print_name(name, lastname):
    print(f"{name} {lastname}")
    
print_name("Jinwoo", "Sung")
print_name(lastname = "Sung", name = "Jinwoo")

def print_name_with_default(name, lastname, alias = "No alias"):
    print(f"{name} {lastname} {alias}")
    
print_name_with_default("Jinwoo", "Sung")
print_name_with_default("Jinwoo", "Sung", "Jin")

def print_text(*text):
    for element in text:
        print(element)
    
print_text("Hello", "World", "This", "is", "a", "test")