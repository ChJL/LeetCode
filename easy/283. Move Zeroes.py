# Tag: Array
'''

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

SOL 1: 
only use one pointer, if the val is zero: pop it, and append a zero in the tail.
otherwise: i += 1
     -> 
        i=0
        j=0
        n = len(nums)
        while i < n:
            if nums[i] ==0:
                nums.pop(i)
                nums.append(0)
                n -= 1
            else:
                i += 1
SOL 2:
see the code followed, 
i will be the pos of first zero, or the pos equals to j if nums[i] == nums[j] initially

btw, I prefer sol 1
'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
