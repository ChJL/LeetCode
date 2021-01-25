# Tag: Two Pointers
'''
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Input: "hello"
Output: "holle"

Example 2:
Input: "leetcode"
Output: "leotcede"

Note:
The vowels does not include the letter "y".

SOL: transfer string into a list, Using two pointers and operate the values in the list.

'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = {'a','e','i','o','u','A','E','I','O','U'}
        
        i = 0
        j = len(s) -1
        ls = list(s)
        
        while i < j:
            if ls[i] in vowel and ls[j] in vowel:
                tmp = ls[j]
                ls[j] = ls[i]
                ls[i] = tmp
                j -=1
                i +=1
            elif ls[i] in vowel:
                j -=1
            elif ls[j] in vowel:
                i +=1
            else:
                i +=1
                j -=1
                
        return "".join(ls)
        