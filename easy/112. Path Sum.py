# Tag: DFS
'''
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path 
such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

SOL: a solution from leetcode discussion.
'''
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return 0
        
        if not root.left and not root.right and root.val == targetSum:
            return 1
        
        targetSum -= root.val
        
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)