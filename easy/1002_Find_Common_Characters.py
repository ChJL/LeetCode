# 1002 Find Common Character
'''
Given an array A of strings made only from lowercase letters, return a list of all characters 
that show up in all strings within the list (including duplicates).  
For example, if a character occurs 3 times in all strings but not 4 times, 
you need to include that character three times in the final answer.
'''

'''
Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
'''

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        from collections import Counter
        res = Counter(A[0])
        for i in range(1,len(A)):
            res = res & Counter(A[i])
        return res.elements()

# note that counter elements() return a itertool, yet this method still works.            