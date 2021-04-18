'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.
Example 1:
Input: x = 1, y = 4

Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.
SOL: to be short, count the 1 in x^y

this sol is from discussion: 
We are asked to find the number of positions, where x and y have equal bits. It is the same as finding number of 1 bits in number t = x^y. 
There is efficient way to find number of 1 bits in any number, using t = t&(t-1) trick: 
this operation in fact removes the last 1 bit from t. 
So, we just apply this rule in loop and increment our counter Out.

Complexity is O(k), where k is Hamming distance between numbers x and y, memory is O(1). 
Note, that it works (twice?) faster than usual bit counts, which have always 32 iterations.
'''
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        t, out = x^y, 0
        while t:
            t, out = t& (t-1), out+1
        return out