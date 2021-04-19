'''
Given a positive integer num, output its complement number. The complement strategy is to flip the bits of its binary representation.

Example 1:
Input: num = 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

SOL: ex: 111 ^ 101 = 010
SO we try to find 111 from 101, and then do the xor

'''
class Solution:
    def findComplement(self, num: int) -> int:
        i = 1
        while i <= num:
            i= i << 1
        return (i-1) ^ num