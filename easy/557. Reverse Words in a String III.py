# Tag: string
'''
Given a string s, reverse the order of characters in each word within 
a sentence while still preserving whitespace and initial word order.

Example 1:
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Example 2:
Input: s = "God Ding"
Output: "doG gniD"


SOL: split -> reverse 
one line: 
return ' '.join([w[::-1] for w in s.split(' ')])
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        l_s = s.split()
        res = ""
        for i in l_s:
            tmp = i[::-1]
            res = res + tmp + " "
        return res[:-1]
                