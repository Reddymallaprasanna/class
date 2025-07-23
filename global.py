def op(x):
    return x**3
class abc():
    def __init__(self,val):
        self.val=val
    def display(self):
        print("Given number:",self.val)
    def modify(self):
        self.val=op(self.val)
n=int(input("Enter the value:"))
o=abc(n)
o.display()
o.modify()
o.display()