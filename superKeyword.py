class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id


class Programmer(Employee):
    def __init__(self,name,id,lang):
        super().__init__(name,id)
        self.lang = lang

Rohan = Employee("Rohan",420)
harry = Programmer("Harry",2345,"Python")
print(harry.name)
print(harry.id)
print(harry.lang)