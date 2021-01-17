# Tag: two pointers
'''
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.
Example 1:

Input: x = 121
Output: true
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Example 4:
Input: x = -101
Output: false

SOL: two pointers, one from 0, another from end to compare the character.
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        i = 0
        j = len(s) -1
        count = 0
        if s[0] == "-":
            return 0
        
        while i < len(s):
            if s[i] == s[j]:
                count +=1
            i += 1
            j -= 1
        
        if count == len(s):
            return 1
        return 0