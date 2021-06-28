'''
Given the root of a binary tree, return the preorder traversal of its nodes' values.
'''
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def preorder(node, lis):
            if not node:
                return
            lis.append(node.val)
            preorder(node.left, lis)
            preorder(node.right, lis)
            
        preorder(root, res)
        return res