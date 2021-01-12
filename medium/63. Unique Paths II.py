# Tag: Dynamic Programming
'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and space is marked as 1 and 0 respectively in the grid.

Example 1:
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

SOL: similar to Unique Paths, but take obstacles into consideration


'''

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        DP = [[1 for i in range(n)] for j in range(m)]
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    DP[i][j] = -1
                    
                if j == 0 and i > 0 and DP[i-1][0] == -1:
                    DP[i][j] = -1
                if i == 0 and j > 0 and DP[0][j-1] == -1:
                    DP[i][j] = -1

        for i in range(1,m):
            for j in range(1,n):
                if DP[i][j] == -1:
                    DP[i][j] = -1
                elif DP[i-1][j] == -1 and DP[i][j-1]== -1:
                    DP[i][j] = 0
                elif DP[i-1][j] == -1:
                    DP[i][j] = DP[i][j-1]
                elif DP[i][j-1]== -1:
                    DP[i][j] = DP[i-1][j]
                else:
                    DP[i][j] = DP[i-1][j] + DP[i][j-1]

        return DP[-1][-1] if DP[-1][-1] > 0 else 0