# Tag: Dynamic Programming
'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

SOl: 
simple 1d-DP
n = [0,1,2,3,4,5,6,.....]
f = [0,1,2,(1+2),2+(1+2) , (1+2)+(2+1+2) , ]
f[i] = f[i-2] + f[i-1]

'''
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        tmp_1 = 1
        tmp_2 = 2
        ans = 0
        if n > 2:
            for i in range(3,n+1):
                ans = tmp_1 + tmp_2
                tmp_1 = tmp_2
                tmp_2 = ans
        return ans