# Tag: Binary Search
'''
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Example 1:
Input: x = 4
Output: 2

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.

SOL: simple binary search, notice that the ans is in r.
'''
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        
        while l <= r:
            mid = l + (r-l)//2
            if mid*mid > x:
                r = mid -1 
            else :
                l = mid +1
                
        return r
            