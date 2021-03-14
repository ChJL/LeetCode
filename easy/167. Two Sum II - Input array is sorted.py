# Two pointers
'''
Given an array of integers numbers that is already sorted in ascending order, 
find two numbers such that they add up to a specific target number.

Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, 
where 1 <= answer[0] < answer[1] <= numbers.length.

You may assume that each input would have exactly one solution and you may not use the same element twice.

Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]

SOL: simple two pointers prob, when sum of two pointer > target, r--. when sum < target, l++.
'''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo = 0
        hi = len(numbers) - 1
        
        while (numbers[lo] + numbers[hi] != target):
            if numbers[lo] + numbers[hi] < target:
                lo +=1
            if numbers[lo] + numbers[hi] > target:
                hi -=1
        
        res = [lo+1, hi+1]
        return res