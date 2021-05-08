'''
We want to reformat the string s such that each group contains exactly k characters, 
except for the first group, which could be shorter than k but still must contain at least one character. 
Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.

Return the reformatted license key.

 

Example 1:

Input: s = "5F3Z-2e-9-w", k = 4
Output: "5F3Z-2E9W"
Explanation: The string s has been split into two parts, each part has 4 characters.
Note that the two extra dashes are not needed and can be removed.
'''
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.upper()
        s = s.replace("-","")
        mod = len(s)%k
        dev = len(s)//k
        
        first_s = ""
        if mod:
            first_s = s[:mod]
            s = s[mod:]
        
        i = 0
        res =""
        tmps = ""
        while i < len(s):
            if i%k == (k-1):
                tmps = tmps+s[i]
                res = res + "-" + tmps
                tmps = ""
            else:
                tmps = tmps+s[i]
            
            i+=1
        
        if mod:
            res = first_s + res
        else:
            res = res[1:]
        return res
"""
Other elegant sol:

    S = S.replace("-", "").upper()[::-1]
    return '-'.join(S[i:i+K] for i in range(0, len(S), K))[::-1]
"""