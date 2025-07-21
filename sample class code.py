#sample class code
'''del method/class variable with constant access '''
class rks():
    class_var=0
    def __init__(self,var):
        rks.class_var+=10
        self.var=var
        print("Object Variable:", var)
        print("Class Variable:", rks.class_var)
ocj1=rks(11)
obj2=rks(12)
obj3=rks(13)