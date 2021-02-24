# Tag: Array
'''
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
The digits are stored such that the most significant digit is at the head of the list,
and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.
Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

Example 3:
Input: digits = [0]
Output: [1]

==========
SOL: simply plus one with actural integer, and change it into list.
'''
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        tmp_sum = 0
        for i in digits:
            tmp_sum *= 10
            tmp_sum += i
        tmp_sum += 1
        
        res = [int(x) for x in str(tmp_sum)]
        return res
        