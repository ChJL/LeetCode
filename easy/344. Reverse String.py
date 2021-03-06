# Tag: Two Pointers
'''

Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

 

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

SOL: Simply use two pointers and exchange the values.

'''
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)//2 -1
        i = 0
        j = len(s) -1
        
        while i <=n:
            tmp = s[j]
            s[j] = s[i]
            s[i] = tmp
            i+=1
            j-=1
        return s