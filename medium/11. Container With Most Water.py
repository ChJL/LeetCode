# Tag: two pointer
'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). 
Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
Example 2:

Input: height = [1,1]
Output: 1

Example 3:
Input: height = [4,3,2,1,4]
Output: 16

Example 4:
Input: height = [1,2,1]
Output: 2

SOL: official solution at leetcode page:
We take two pointers, one at the beginning and one at the end of the array constituting the length of the lines. 
Futher, we maintain a variable maxarea to store the maximum area obtained till now. 
At every step, we find out the area formed between them, update maxarea and move the pointer pointing to the shorter line towards the other end by one step. (move the pointer with shorter line)

'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        i = 0
        j = len(height) -1
        
        while j != i:
            if height[i] > height[j]:
                tmparea = (j - i) * height[j]
                j -= 1
            else:
                tmparea = (j - i) * height[i]
                i += 1
            if tmparea > maxarea:
                maxarea = tmparea
                
        return maxarea