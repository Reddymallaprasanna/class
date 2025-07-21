class calc:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("Calc obj was created.........")
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def __del__(self):
        print("Createrd calc object was deleted........")
a=int(input("Enter a number:"))
b=int(input("Enter another number:"))
c=calc(a,b)
print("Addition is:",c.add())
print("Subtraction is:",c.sub())
del calc    