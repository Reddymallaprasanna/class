'''

write a code to view memory information in a class,which gives the type of the class,
and size of the class objects,and the size of instance
use:
const,package- sy for size of
ex:
given value of number=10
take class A

'''
import sys
class A:
    n=int(input("enter a number:"))
a=A()
print(type(A))
print(sys.getsizeof(A))
print(sys.getsizeof(a))