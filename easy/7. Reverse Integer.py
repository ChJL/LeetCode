# Tag: Math
'''
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

Example 4:
Input: x = 0
Output: 0

SOL: take modulo 10 loop, and multiply 10 in each step

'''
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        flag = 0
        if x < 0:
            flag = 1
            x = -x
        newnum = 0
        while x !=0:
            newnum = newnum*10 + x%10
            x = x // 10
            
        if flag:
            newnum = newnum * (-1)
        if newnum > 2147483647:
            return 0
        if newnum < -2147483648:
            return 0
        
        return newnum
            
        