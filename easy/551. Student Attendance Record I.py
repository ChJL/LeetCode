# Tag: String
'''
The student is eligible for an attendance award if they meet both of the following criteria:

The student was absent ('A') for strictly fewer than 2 days total.
The student was never late ('L') for 3 or more consecutive days.
Return true if the student is eligible for an attendance award, or false otherwise.


one line SOL: 
return s.count('A') < 2 and 'LLL' not in s

'''
class Solution:
    def checkRecord(self, s: str) -> bool:
        
        countA = 0
        pre = ""
        countL = 0
        for i in s:
            if countA >=2 or countL >=3:
                return 0
            if i =="A":
                countA += 1
            elif i == "L":
                if pre != "L":
                    countL = 1
                else:
                    countL += 1
            pre = i
        
        if countA >=2 or countL >=3:
            return 0
        
        return 1