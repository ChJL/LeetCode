'''
Given an integer, convert it to a roman numeral.

Example 1:
Input: num = 3
Output: "III"

Example 2:
Input: num = 4
Output: "IV"

Example 3:
Input: num = 9
Output: "IX"

Example 4:
Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.

Example 5:
Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

'''
class Solution:
    def intToRoman(self, num: int) -> str:
        dict_roman = {1: "I", 4: "IV", 5: "V", 9: "IX", 
                 10: "X", 40: "XL", 50: "L", 90: "XC", 
                 100: "C",400: "CD", 500: "D", 900: "CM", 
                 1000: "M"}
        
        level = 1
        ans = ""
        while num:
            curr = num % 10
            if curr*level in dict_roman.keys():
                ans = dict_roman[curr*level] + ans
            elif curr > 5:
                curr = curr - 5
                ans = dict_roman[5*level] + dict_roman[level]*curr + ans
            else:
                ans = dict_roman[level]*curr + ans
            
            num = num // 10
            level *= 10
        
        return ans

'''

# Huahua Solution
# https://zxi.mytechroad.com/blog/simulation/leetcode-12-integer-to-roman/
class Solution:
    def intToRoman(self, num: int) -> str:
        roman = [[1000,"M"],[900,"CM"],[500,"D"],[400,"CD"],
                 [100,"C"],[90,"XC"],[50,"L"],[40,"XL"],[10,"X"],
                 [9,"IX"],[5,"V"],[4,"IV"],[1,"I"]]
                
        index = 0
        ans = ""
        while num:
            if num >= roman[index][0]:
                ans = ans + roman[index][1]
                num -= roman[index][0]
            else:
                index +=1
        return ans
'''