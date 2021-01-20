# Tag: Recursion
'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

SOL: judging if it is balanced in the recursing process. If it is not, return all asap. 
# http://zxi.mytechroad.com/blog/leetcode/leetcode-110-balanced-binary-tree/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.flag = True
        def balance(node):
            if not node:
                return 0
            if not self.flag:
                return 0
            rs = balance(node.right)
            ls = balance(node.left)
            if abs(rs-ls) >1:
                self.flag = False
                return 0
            return max(rs , ls)+1
        
        balance(root)
        return self.flag