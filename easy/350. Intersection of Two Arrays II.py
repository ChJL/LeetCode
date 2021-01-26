# Tag: Two Pointers
'''
Given two arrays, write a function to compute their intersection.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.

SOL: sort 2 list. use two pointers to compare the values. if match -> record in a list.

'''

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = sorted(nums1)
        n2 = sorted(nums2)
        
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
                i += 1
                j += 1
        
        return ans