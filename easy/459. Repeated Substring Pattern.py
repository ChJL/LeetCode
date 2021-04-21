#Tag: string
'''
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.
Example 1:

Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.

Example 2:
Input: s = "aba"
Output: false

SOL:

If there is such pattern, the original string could be represented as following:
    origin_str = pattern + pattern + ... + pattern =  m * pattern; 

With doubling:
    origin_str + origin_str = 2 * m * pattern;

After removing head and rear:
    new_str = pattern_wo_head + (2m-2) * pattern + pattern_wo_rear 

'''
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s+s)[1:-1]