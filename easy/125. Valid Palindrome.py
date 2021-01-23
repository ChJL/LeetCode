# Tag: two pointers
'''
Given a string, determine if it is a palindrome, 
considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.
Example 1:
Input: "A man, a plan, a canal: Panama"

Output: true
Example 2:
Input: "race a car"
Output: false

SOL: 1. extract the alpha and number using regex
    2. s == s[::-1] # where s[::-1] is reversed order of s

'''

import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        regex = re.compile('[^a-zA-Z0-9]')
        
        s = regex.sub('', s)
        s = s.lower()
        
        return s == s[::-1]