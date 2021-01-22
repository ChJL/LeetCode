'''
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, 
and it should return false if every element is distinct.

Example 1:
Input: [1,2,3,1]
Output: true

Example 2:
Input: [1,2,3,4]
Output: false

SOL: simply use the "set" in python
or do sorting and then if nums[i] = nums[i+1]--> duplicate
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        new_set = set(nums)
        if len(new_set) < len(nums):
            return 1
        return 0