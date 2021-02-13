# Tag: Math 
'''
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example 1:
Input: 6
Output: true
Explanation: 6 = 2 × 3

Example 2:
Input: 8
Output: true
Explanation: 8 = 2 × 2 × 2

Example 3:
Input: 14
Output: false 
Explanation: 14 is not ugly since it includes another prime factor 7.

SOL: easily check if there are modulo of 2,3 or 5; 
if no then devided num by 2,3,5 respectively until there is a num cannot devided by 2,3,5


'''
class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 1:
            return 1
        if num == 0:
            return 0
        while not num%2:
            num = num/2
        while not num%3:
            num = num/3
        while not num%5:
            num = num/5
        
        return 1 if num == 1 else 0
                