#Tag: Math 
'''
Given a column title as appear in an Excel sheet, return its corresponding column number.
For example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    
SOL:
26 decimal.
note: In Python, the ord() function accepts a string of unit length as an argument and returns the Unicode equivalence of the passed argument.


'''
class Solution:
    def titleToNumber(self, s: str) -> int:
        s_inv = s[::-1]
        ans = 0
        j = 0
        for i in s_inv:
            ans += 26**j*(ord(i) -65 +1)
            j+=1
        return ans