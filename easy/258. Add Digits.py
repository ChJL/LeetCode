#Tag: Math
'''
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.
Follow up:
Could you do it without any loop/recursion in O(1) runtime?

SOL:
it's a math problem about digital root:
There is a known formula to compute a digital root in a decimal numeral system
dr10(n) = 0, if n = 10
dr10(n) = 9, if n = 9k
dr10(n) = n mod 9, if n != 9k


'''
class Solution:
    def addDigits(self, num: int) -> int:
        return 0 if num == 0 else (num -1)%9 +1