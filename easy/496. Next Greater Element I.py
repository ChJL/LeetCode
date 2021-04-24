# Tag: stack
'''
You are given two integer arrays nums1 and nums2 both of unique elements, where nums1 is a subset of nums2.

Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, return -1 for this number.

 

Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]

Explanation:
For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
For number 1 in the first array, the next greater number for it in the second array is 3.
For number 2 in the first array, there is no next greater number for it in the second array, so output -1.

SOL: Use a stack (manipulate) and a dictionary (record right greater) on nums2
For example nums2 = [4,3,2,1,5,6]
the stack would be:
step1: [4], step2: [4,3], step3: [4,3,2], step4: [4,3,2,1], 
step5:  since 1<5 --> pop and store d[1] = 5 --> [4,3,2]
        since 2<5 --> pop and store d[2] = 5 --> [4,3]
        since 3<5 --> pop and store d[3] = 5 --> [4]
        since 4<5 --> pop and store d[4] = 5 --> []
        append 5 in stack --> [5]
step6:  since 5<6 --> pop and store d[5] = 6 --> []
        append 6 in stack --> [6]

'''
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        stack = []
        res = []
        for item in nums2:
            while stack and stack[-1] < item:
                d[stack.pop()] = item
            stack.append(item)
        
        for item in nums1:
            res.append(d.get(item, -1))
            
        return res