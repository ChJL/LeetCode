# Tag: String
'''
Given an arbitrary ransom note string and another string containing letters from all the magazines, 
write a function that will return true if the ransom note can be constructed from the magazines ; 
otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true

SOL: 
Method 1
1. sort the strings, and store in lists
2. use two pointers to compare the element, if all of elements in ransomNote can be go through -> true

Method 2
set (ransomNote)
if ransomNote.count(ele) > magzine.count(ele): return 0
# much Faster than method 1

for i in set(ransomNote):
    if ransomNote.count(i) > magazine.count(i):
        return False
return True

'''
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r  = list(ransomNote)
        m  = list(magazine)
        
        r.sort()
        m.sort()
        
        i = 0
        j = 0
        
        while i < len(r) and j < len(m):
            if r[i] == m[j]:
                i+=1
                j+=1
            else: 
                j+=1
        return 1 if i == len(r) else 0