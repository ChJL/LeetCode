'''
Given an integer num, return a string of its base 7 representation.
Example 1:
Input: num = 100
Output: "202"

Example 2:
Input: num = -7
Output: "-10"

'''
class Solution:
    def convertToBase7(self, num: int) -> str:
        is_neg = 0
        if num<0:
            is_neg = 1
            num = -num
        if num ==0:
            return "0"
        
        res =""
        while num>0:
            res =  str(num%7) + res
            num = num//7
        
        return "-"+res if is_neg else res