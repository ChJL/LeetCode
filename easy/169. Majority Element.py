#Tag: Hash Table, D&C, Array 
'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 
Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

SOL:
my ori sol: use dictionary to record appearance times, return max one
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = collections.defaultdict(int)
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
                
        return max(d, key = d.get)
SOL2: Sorting, and return the mid value
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
        
SOL3: Boyer-Moore Voting Algorithm
If we had some way of counting instances of the majority element as +1 and instances of any other element as -1, summing them would make it obvious that the majority element is indeed the majority element.


'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #sol 3
        count = 0
        candidate = None
        
        for i in nums:
            if count == 0:
                candidate = i
                count +=1
            elif i == candidate:
                count +=1
            else:
                count -=1
        return candidate