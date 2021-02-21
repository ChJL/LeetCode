# Tag: DFS, Recursion
'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

SOL: officail sol1 on leetcode:
The simplest strategy here is to use recursion. Check if p and q nodes are not None, and their values are equal. 
If all checks are OK, do the same for the child nodes recursively.

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        if p is None and q is None:
            return 1
        
        if p is None or q is None:
            return 0
        
        if p.val != q.val:
            return 0
        
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left) 