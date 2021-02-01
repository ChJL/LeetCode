# Tag: Array
'''
You are given a sorted unique integer array nums.

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. 
That is, each element of nums is covered by exactly one of the ranges, 
and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
 

Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

SOL:
use 2 variable to store "front" and "back", make sure the nums in the interval are continuous. 
if the next val can't be the one fit the continuous rule, store only one value in ans list.

Another elegant sol from leetcode discussion:
    
    ans = []
    r = []

    for i in nums:
        if i-1 not in r :
            r =[]
            ans.append(r)
        r[1:] = [i]
    
    return ["->".join(map(str,r)) for r in ans]

'''
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) < 1:
            return []
        
        ans = []
        f = nums[0]
        b = nums[0]

        for i in nums[1:]:
            if i == b+1 :
                b = i
            else:
                if f == b:
                    ans.append(str(f))
                else:
                    ans.append(str(f) + "->" + str(b))
                
                f = i
                b = i
        
        # the last interval in the list        
        if f == b:
            ans.append(str(f))
        else:
            ans.append(str(f) + "->" + str(b))
        
        return ans