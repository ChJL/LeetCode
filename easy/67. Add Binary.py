# Tag: String
'''
Given two binary strings a and b, return their sum as a binary string.
Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

=====
SOL: ref on leetcode discussion. use list and pop function! elegant!
'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = list(a)
        b = list(b)
        res = ""
        carry = 0
        
        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())
                
            res = str(carry%2) + res
            carry //= 2
        
        return res