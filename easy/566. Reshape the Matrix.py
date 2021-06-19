'''
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix 
into a new one with a different size r x c keeping its original data.

Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]


'''
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        one_row = []
        m = len(mat)
        n = len(mat[0])
        if r*c != m*n:
            return mat
        for i in mat:
            for j in i:
                one_row.append(j)
        pos = 0
        res = []
        for i in range(r):
            tmp = []
            for j in range(c):
                tmp.append(one_row[pos])
                pos += 1
            res.append(tmp)
        return res