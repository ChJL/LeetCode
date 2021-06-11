'''
Example 1:

Input: candyType = [1,1,2,2,3,3]
Output: 3
Explanation: Alice can only eat 6 / 2 = 3 candies. Since there are only 3 types, she can eat one of each type.

SOL: simple hash table
'''
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        d = {}
        count = 0
        maxicanit = len(candyType)//2
        for i in candyType:
            if i not in d:
                d[i] = 1
                count +=1
            if count > maxicanit:
                return maxicanit
        return count