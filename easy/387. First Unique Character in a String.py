# Tag: Hash Table

'''
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:
s = "leetcode"
return 0.

s = "loveleetcode"
return 2.

SOL: 

O(N): using a dictionary to record the appeating times of each alphabet
O(N): choose first that only appears 1 time 

'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1
        d = collections.defaultdict(int)
        for ch in s:
            d[ch] += 1
        
        for i, ch in enumerate(s):
            if d[ch] < 2:
                return i
        
        return -1