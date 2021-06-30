# recursive
'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
SOL: from official sol on leetcode

'''
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def ismirror(t1,t2):
            if t1==None and t2==None:
                return 1
            if t1==None or t2==None:
                return 0
            return (t1.val == t2.val) and ismirror(t1.left, t2.right) and ismirror(t1.right, t2.left)
        return ismirror(root, root)