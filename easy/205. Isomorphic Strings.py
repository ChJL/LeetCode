# Hash Table
'''
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character, but a character may map to itself.

 

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true

SOL: using dictionary to record the mappings, if the mapping is conflicted to previous one -> false

'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = collections.defaultdict(str)
        d2 = collections.defaultdict(str)
        j = 0
        for i in s: 
            if i not in d:
                d[i] = t[j]
            elif d[i] != t[j]:
                return 0
            j += 1
        
        y = 0
        for x in t:
            if x not in d2:
                d2[x] = s[y]
            elif d2[x] != s[y]:
                return 0
            y +=1
        
        return 1