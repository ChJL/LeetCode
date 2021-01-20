# Tag: Recursion
'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

SOL: Simple DFS recursion.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        def depth(node):
            if not node:
                return 0
            ls = depth(node.left)
            rs = depth(node.right)
            return max(ls,rs) +1
        
        return depth(root)