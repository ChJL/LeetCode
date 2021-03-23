# Tag : recursive
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
SoL: from huahua
'''
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        sum_ = 0
        if root.left and not root.left.left and not root.left.right:
            sum_ = root.left.val
        
        return sum_ + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)