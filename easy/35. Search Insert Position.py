'''
Given a sorted array of distinct integers and a target value, 
return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4

SOL: Binary search
'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) -1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] > target:
                r = mid -1
            elif nums[mid] < target:
                l = mid +1
            else:
                return mid
        if nums[mid] >= target:
            return mid
        else:
            return mid+1