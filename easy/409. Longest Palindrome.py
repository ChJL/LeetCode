# Tag : Hash Table
'''
Example 1:
Input: s = "abccccdd"
Output: 7
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.

SOL: 
First, record all the alphat appear time in a dict.
Second, go through dict sum all the even value and (odd -1) value
Third judge if odd value is exist, if so - > plus one, else: just remain the same sum and output.
(The reason: if their is odd value exist we should plus since the one can be put in the middle of string)
for instance: 
"aaabbcc" -> bca a acb, 
"aabbcc" -> abccba,
Therefore, if odd appear time exist in dict, we should +1 to make palindorme the longest one.


'''
class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = collections.defaultdict(int)
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        total = 0
        count_odd = 0
        for key in d:
            if not d[key] % 2:
                total += d[key]
            else:
                total += d[key] -1
                count_odd += 1
        
        if count_odd:
            total +=1
        
        return total