# Tag: Array
'''
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.

SOL: official solution2 in leetcode page:
Reverse on Diagonal and then Reverse Left to Right
That is, Transpose and then Reverse

'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # transpose:
        n = len(matrix)
        for i in range(n):
            for j in range(i,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        # Reverse
        for i in range(n):
            for j in range(n//2):
                matrix[i][j], matrix[i][-1-j] = matrix[i][-1-j], matrix[i][j]
                