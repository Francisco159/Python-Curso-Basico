### CLASSES

class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self, name, lastname, alias = "sin alias"):  # constructor de clase
        self.full_name = f"{name} {lastname} ({alias})" # variable publica
        self.__name = name          # variable privada
        self.__lastname = lastname  # variable privada
        
    def get_name(self):
        return self.__name
    
    def walk(self):
        print(f"{self.full_name} is walking")
    
my_person = Person("Jinwoo", "Sung")
print(my_person.full_name)
my_person.walk()

my_other_person = Person("Jinwoo", "Sung", "Jin")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Jinwoo Sung (Jinu)"
print(my_other_person.full_name)

print(my_other_person.get_name())