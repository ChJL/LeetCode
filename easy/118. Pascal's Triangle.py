# Tag: Array
'''
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]

SOL: simple array minipulation
'''
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res =[]
        for i in range(numRows):
            tmp =[]
            for j in range(i+1):
                if j != 0 and j!= i:
                    tmp.append(res[-1][j-1]+res[-1][j])
                else:
                    tmp.append(1)
            res.append(tmp)
        
        return res