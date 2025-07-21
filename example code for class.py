'''code to ass the sum of rows in a 2-D list'''
# Define a 2-D list
class RowSum:
    def __init__(self,matrix):
        self.matrix=matrix
    def __getitem__(self,row):
        return sum(self.matrix[row])
    def __setitem__(self,row,new_values):
        self.matrix[row]=new_values

m=RowSum([[1,2], [3,4] ,[5,6]])
#sum of 0 index row value=3
#sum of 1 index row value=11
print("Sum of Row 0:",m[0])
print("Sum of Row 2:",m[2])
m[1]=[10,20]
#sum of 1 index row value=30
print("New sum of row 1:",m[1])