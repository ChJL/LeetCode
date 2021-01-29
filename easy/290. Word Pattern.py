#Tag: Hash Table
'''
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false

Example 4:
Input: pattern = "abba", s = "dog dog dog dog"
Output: false

SOL:
0. return 0 if length are different

1. if pattern wasn't in dict AND the word wasn't used: 
    insert new ele in dict
    and append the word in list
2.  if pattern wasn't in dict AND the word was already used: return false
3.  if pattern isn't matched to the word in the dict(value): return false


'''

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # a dictionary {a: dog, b: cat .....}
        d = collections.defaultdict(str)
        
        # a list recording the word already used, so that if the word is used and the pattern cannot be a new one.
        used = []
        word = s.split()
        
        # return false if the length are different
        if len(word) != len(pattern):
            return 0
        
        for i, ch in enumerate(pattern):
            if ch not in d and word[i] not in used:
                d[ch] = word[i]
                used.append(word[i])
            elif ch not in d and word[i] in used:
                return 0
            elif d[ch] != word[i]:
                return 0
        return 1
            