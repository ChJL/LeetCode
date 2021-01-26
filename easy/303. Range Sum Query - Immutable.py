# Tag: dynamic Programming
'''
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int i, int j) Return the sum of the elements of the nums array in the range [i, j] 
inclusive (i.e., sum(nums[i], nums[i + 1], ... , nums[j]))
 

Example 1:
Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]

Output
[null, 1, -1, -3]

SOL: simple 1d DP, store the sum at current element.
'''

class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = []
        self.num =nums
        tmp = 0
        for i in range(len(nums)):
            tmp = tmp + nums[i]
            self.arr.append(tmp)

    def sumRange(self, i: int, j: int) -> int:
        return self.arr[j] - self.arr[i] + self.num[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)