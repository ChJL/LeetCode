#Tag: Stack, DFS
"""
Example 1:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:
Input: s = "3[a2[c]]"
Output: "accaccacc"

SOL: from discussion: https://leetcode.com/problems/decode-string/discuss/87662/Python-solution-using-stack
using stack, store number than string.
note that cur_n = cur_n*10 + int(ele), since the number may be larger than 10 100.
"""
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur = ""
        cur_n = 0
        
        for ele in s:
            if ele == "[":
                stack.append(cur_n)
                stack.append(cur)
                cur_n = 0
                cur = ""
            elif ele == "]":
                pre_s = stack.pop()
                num = stack.pop()
                cur = pre_s + cur * num
            elif ele.isdigit():
                cur_n = cur_n*10 + int(ele)
            else:
                cur += ele
        
        return cur