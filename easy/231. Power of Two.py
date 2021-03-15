'''
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2^x.

Example 1:
Input: n = 1
Output: true
Explanation: 2^0 = 1

Example 2:
Input: n = 16
Output: true
Explanation: 24 = 16

Example 3:
Input: n = 3
Output: false

SOL: ex: n=4 = 0100
        n=3 = 0011
        4&3 = 0000
'''
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return 0
        return 1 if not (n & (n-1)) else 0