# Tag: Two Pointers
'''
Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]

Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]

SOL: 2 pointers, but from tail to head.
'''
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        
        while j>=0:
            if i<0 or nums2[j] > nums1[i]:
                nums1[i+j+1] = nums2[j]
                j -=1
            else:
                nums1[i+j+1] = nums1[i]
                i -=1
            
            