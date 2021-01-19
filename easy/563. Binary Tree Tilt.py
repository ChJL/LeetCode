# Tag: Recursion
'''
Given the root of a binary tree, return the sum of every tree node's tilt.

The tilt of a tree node is the absolute difference between the sum of all left subtree node values and all right subtree node values. 
If a node does not have a left child, then the sum of the left subtree node values is treated as 0. 
The rule is similar if there the node does not have a right child.

SOL: method from HuaHua:
    # https://zxi.mytechroad.com/blog/tree/leetcode-563-binary-tree-tilt/
    
    Define a function, input node, return two value: 
    1. total sum of tilt in all subtree at current node. 2. sum of values of all subtrees at current node
    recursively call the functions.
    
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        
        def findtilt(node):
            if not node:
                return 0, 0
            tl, sl = findtilt(node.left)
            tr, sr = findtilt(node.right)
            return tl + tr + abs(sl-sr) , sl+sr+node.val
        
        return findtilt(root)[0]