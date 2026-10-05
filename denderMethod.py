class Employee:
    def __init__(self,name):
        self.name = name
    
    def __len__(self):
        i=0
        for c in self.name:
            i= i+1
        return i
    def __str__(self):
        return (f"The name of Employee is {self.name} str")

    def __repr__(self):
        return (f"Employee '('{self.name}')' ")

    def __call__(self):
        print("Hey i am good")

e = Employee("harry")
print(e.name)
#print(len(e.name))
#print(len(e))
print(str(e))
print(e)
print(repr(e))
e()



