'''
Given an array of integers and an integer k, find out whether there are two distinct indices 
i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false

SOL: using dictionary to store the idx: value -> idx
so that when duplicate value occur, can find the difference by using current idx and the idx in the dictionary

'''

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict_idx = {}
        for i in range(len(nums)):
            if nums[i] in dict_idx:
                if i - dict_idx[nums[i]] <= k:
                    return 1
                dict_idx[nums[i]] = i
            else:
                dict_idx[nums[i]] = i
        return 0