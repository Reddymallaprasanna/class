class atm:
    def __init__(self,p):
        self.p = p
        self.balance=50000
        self.key=1234
    def check_pin(self):
        if self.p==self.key:
            print("**LOGIN SUCCESSFULL***")
        else :
            print("**INVALID PASSWORD**")
            print("**LOGIN FAILED***")
            exit()
    def withdraw(self):
        a=int(input("Enter amount to withdraw::"))
        if a<self.balance:
            print("AMOUNT WITHDRAWAL SUCCESSFULL")
            print("YOUR CURRENT BALANCE:",self.balance-a)
        else:
            print("**INSUFFICIENT BALANCE**")
p=int(input("Enter your key:"))
machine=atm(p)
machine.check_pin()
machine.withdraw()