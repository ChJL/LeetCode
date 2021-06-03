'''
We define a harmonious array as an array where the difference 
between its maximum value and its minimum value is exactly 1.

Example 1:
Input: nums = [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].

Example 2:
Input: nums = [1,2,3,4]
Output: 2

Example 3:
Input: nums = [1,1,1,1]
Output: 0

SOL: hash table record the count of each number, 
find the maximum for (i and i+1) in the dict
'''
# Tag: Hash Table
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        # drop the case like [1,1,1,1]
        if len(d) ==1:
            return 0
        
        res = []
        for i in nums:
            if i+1 in d:
                res.append(d[i]+d[i+1])
        
        if res:
            return max(res)
        else:
            # the cases that there is no harminious sub (e.g., [1,3,5,7,9])
            return 0