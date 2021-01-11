# Tag : Array
'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 4:
Input: nums = [-1]
Output: -1
====================================
Solution:
nums = [-2,1,-3,4,-1,2,1,-5,4]
f =    [-2,1,-2,4,3,5,6,1,5]
f[i] = f[i-1]+num[i] if f[i-1]>0 else num[i]
(if take No. i item into consideration in the last place)
it's a 1D dp

'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        Lenofnums = len(nums)
        tmp_sum = nums[0]
        ans = nums[0]
        
        if len(nums) ==1:
            return ans
        
        for i in range(1,Lenofnums):
            if tmp_sum < 0:
                tmp_sum = nums[i]
            else:
                tmp_sum= nums[i]+tmp_sum
            if tmp_sum > ans:
                ans = tmp_sum
        return ans