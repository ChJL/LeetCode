# Tag: Greedy
'''
Given a string s and a string t, check if s is subsequence of t.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?


Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false

SOL: Use two pointer and a while loop, count the numbers if the alphabet is match,
if the count == len of string: return 1
else return 0

'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return 1
        if not t:
            return 0
        
        len_s = len(s)
        i = 0
        j = 0
        count =0
        while(i<len(s) and j<len(t)):
            if s[i] == t[j]:
                i+=1
                j+=1
                count +=1
            else:
                j+=1
        
        if count == len_s:
            return 1
        return 0
        