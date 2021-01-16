# Tag: Dynamic Programming
'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, 
which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.

Example 1:

Input: grid = [ [1,3,1],
                [1,5,1],
                [4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12

SOL: easy DP, each grid record the min path sum at current step.
'''
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        DP = [ele for ele in grid]
        for j in range(1,n):
            DP[0][j] = DP[0][j-1] + DP[0][j]
        for i in range(1,m):
            DP[i][0] = DP[i-1][0] + DP[i][0]
            
        for i in range(1, m):
            for j in range(1,n):
                if DP[i-1][j] < DP[i][j-1]:
                    DP[i][j] =  DP[i-1][j] + DP[i][j]
                else : 
                     DP[i][j] =  DP[i][j-1] + DP[i][j]
        
        return DP[-1][-1]