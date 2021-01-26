# Tag: Bit manipulation

'''
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.

Example 1:
Input: n = 16
Output: true

Example 2:
Input: n = 5
Output: false

Example 3:
Input: n = 1
Output: true

SOL: look at the following code:
condition1 : to judge all n > 0
condition2 : to judge n is 2^x
condition3 : to judge if the "1" is in odd position in bin

con2 ex:
    n = 4:  0b100
    n-1 = 3:0b011
    thus, n & n-1 = 0 -> n is a 2^x

con3 ex: 
    n = 4 : 0b100
    len(bin(n)) = 5 : 0b101
    5 & 1 = 1
    
    otherwise, take n = 8
    len(bin(n)) = 6
    6 & 1 = 0

'''
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return (n > 0) and (not(n & n-1)) and len(bin(n)) & 1