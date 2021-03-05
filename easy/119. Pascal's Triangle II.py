# Tag: Array
'''
SOL:
Another beautiful sol on leetcode:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0]+row, row+[0])]
        return row
        
    explain:
    [1,2,1]
    --> [0,1,2,1] + [1,2,1,0] = [1,3,3,1]

'''
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        tmp1 = [1]
        tmp2 = [1,1]
        if rowIndex == 0:
            return tmp1
        if rowIndex == 1:
            return tmp2
        
        for i in range(1,rowIndex):
            tmp = []
            for j in range(i+2):
                if j !=0 and j!= i+1:
                    tmp.append(tmp2[j-1]+tmp2[j])
                else:
                    tmp.append(1)
            tmp2 = tmp
            
        return tmp2