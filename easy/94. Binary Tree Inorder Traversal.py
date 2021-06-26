'''
Given the root of a binary tree, return the inorder traversal of its nodes' values.

SOL: inorder : recursive.
'''
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def inorder(root, lis):
            if root:
                inorder(root.left, lis)
                lis.append(root.val)
                inorder(root.right, lis)
        inorder(root, res)
        return res
            
            