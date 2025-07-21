class Numbers:
    def __init__(self,myList):
        self.myList=myList
    def __getitem__(self,index):
        return self.myList[index]
    def __setitem__(self,index,val):
        self.myList[index]=val
numList=Numbers([1,2,3,4,5,6,7,8,9,10])
print(numList[3])
numList[5]=60
print(numList.myList)