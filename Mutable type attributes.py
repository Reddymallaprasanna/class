'''Mutable type attributes
code to illustrate multiple attributes by calling a class for its specifications 
FOR EXAMPLE:
n=21,32,43,54,65
even list:[32,54]
odd list:[21,43,65]
 '''
class number:
    odd=[]
    even=[]
    def __init__(self,n):
        self.n=n
        if n%2==0:
            number.even.append(n)
        else:
            number.odd.append(n)
n1=number(21)
n2=number(32)
n3=number(43)
n4=number(54)
n5=number(65)
print("Even Mutable list:",number.even)
print("Odd Mutable List:",number.odd)