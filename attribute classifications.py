
class abc:
    def __init__(self,vare1,vare2):
        self.vare1=vare1
        self.vare2=vare2
    def display(self):
        print("Variable 1:",self.vare1)
        print("Variable 2:",self.vare2)
n1=int(input("Enter n1:"))
n2=float(input("Enter n2:"))
o=abc(n1,n2)
print("Object.__dict__::",o.__dict__)
print("Object.__doc__::",o.__doc__)
print("Class.__name__::",abc.__name__)
print("Object.__module__::",o.__module__)
print("Class.__base__::",abc.__base__)