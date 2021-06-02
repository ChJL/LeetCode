# Tag: string
'''
We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".

Given a string word, return true if the usage of capitals in it is right.

SOL: mysol used dict and count the appear times of Upper and Lower.
Other: Regex: 
    return re.fullmatch(r"[A-Z]*|.[a-z]*", word)
'''
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        d = {}
        
        for i in 'qwertyuiopasdfghjklzxcvbnm':
            d[i] = 0
        for i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
            d[i] = 1
        flag = 0
        count = 0
        if d[word[0]] == 1:
            flag = 1
        for i in word:
            count += d[i]
        if not count:
            return 1
        if count == len(word):
            return 1
        if count == 1 and flag:
            return 1
        return 0
    