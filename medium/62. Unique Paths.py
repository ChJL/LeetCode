#Tag: Dynamic Programming 
'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

SOL:
[1,1,1,1,1,1.......]
[1,2,3,4,..........]
[1,3,6,10,.........]
[1,4,10,20,........]
.
.
.

'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        DP = [[1 for i in range(n)] for j in range(m)]
        
        for i in range(1,m):
            for j in range(1,n):
                DP[i][j] = DP[i-1][j] + DP[i][j-1]
        
        return DP[m-1][n-1]
                