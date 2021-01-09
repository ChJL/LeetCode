'''
Tag: Bit Manipulation

Description:
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
Example 1:

    Input: a = 1, b = 2
    Output: 3

Example 2:

    Input: a = -2, b = 3
    Output: 1
==============================
Explanation:

Make sure our integers are strictly 32 bits
Juggle between 32 bit, two's complements.

Mask is tracking the maximum value for an int as well as being the limiter for the loop. 
So, b & mask basically is checking if there are any bits left to compute within the int range on each iteration of the loop.

for example -2 in python is -0b10
we need to transform to the 2's complement scheme which could be used in our solution
thus, 
-2 & mask
would return 0b11111111111111111111111111111110

We set mask = 0xffffffff
in bin form is : 0b11111111111111111111111111111111

Therefore, all integer will be restricted in 32bits, and could be manipulate via this solution



'''

class Solution:
    def getSum(self, a: int, b: int) -> int:
        diff = 0
        carry = 0
        mask = 0xffffffff
        while b & mask :
            diff = a ^ b
            carry = (a & b) << 1
            a = diff 
            b = carry
        
        return a & mask if b > mask else a 
            