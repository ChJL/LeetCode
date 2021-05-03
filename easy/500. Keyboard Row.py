'''
Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".

Example 1:
Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]

Example 2:
Input: words = ["omk"]
Output: []

SOL: create 3 dicitonary. then iteratively compare if the diff exist.
'''
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        d = {}
        for i in "qwertyuiopQWERTYUIOP":
            d[i] = 1
        for i in "asdfghjklASDFGHJKL":
            d[i] = 2
        for i in "zxcvbnmZXCVBNM":
            d[i] = 3
        res = []
        
        for w in words:
            flag = 0
            pre = d[w[0]]
            for s in w:
                if d[s] != pre:
                    flag = 1
                    break
            if not flag:
                res.append(w)
        return res