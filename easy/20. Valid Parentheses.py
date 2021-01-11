# Tag: Stack
'''

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 
Example 2:

Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([)]"
Output: false

'''


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = { ")":"(", "}":"{", "]":"[" }
        
        for i in s:
            if i in mapping:
                if stack:
                    top_element = stack.pop()
                else:
                    return 0
                
                if top_element != mapping[i]:
                    return 0
            else:
                stack.append(i)
        # if the stack is empty, return true. Otherwise, false.
        return not stack
            