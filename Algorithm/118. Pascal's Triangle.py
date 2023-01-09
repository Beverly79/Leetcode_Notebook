class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l = [0] * numRows # creating empty slots for each row
        for i in range(1,numRows+1):
            l[i-1] = [0] * i # create empty slots for this row
            l[i-1][0] = 1 # first and last should be 0
            l[i-1][-1] = 1
            for j in range(1,i-1): # start from the 
                l[i-1][j] = l[i-2][j-1] + l[i-2][j] 
        return l
