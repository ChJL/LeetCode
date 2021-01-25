# Tag: Two pointers
'''
Given two arrays, write a function to compute their intersection.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]

Note:
Each element in the result must be unique.
The result can be in any order.

SOL: simply use set and two pointers,

or there is another easy solution:
n1 = set(nums1)
n2 = set(nums2)
return list(n1&n2)

'''
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = set(nums1)
        n2 = set(nums2)
        
        n1 = sorted(n1)
        n2 = sorted(n2)
        
        i = 0
        j = 0
        ans = []
        
        while i < len(n1) and j < len(n2):
            if n1[i] < n2[j]:
                i += 1
            elif n1[i] > n2[j]:
                j += 1
            else:
                ans.append(n1[i])
                i+=1
                j+=1
        return ans