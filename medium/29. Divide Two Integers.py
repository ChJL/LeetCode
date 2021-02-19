# Tag: Bit manipulation
'''
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

Example 1:
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.

Example 2:
Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.

SOL: substract the dividend by multiple of divisor. ex: dividend - divisor*1 - divisor*2 - divisor*4 ....
using << 1 to get multiple


'''
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive = (dividend > 0) == (divisor > 0)
        # a / b
        a , b = abs(dividend), abs(divisor)
        res = 0
        
        while a >= b:
            multitmp, i = b, 1
            # minus the dividend by 1,2,4,8,16.... *divisor using << 1
            while a >= multitmp:
                a -= multitmp
                res += i
                
                multitmp <<= 1
                i <<= 1
        
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)
    
        