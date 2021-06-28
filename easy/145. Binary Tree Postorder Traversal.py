'''
Given the root of a binary tree, return the postorder traversal of its nodes' values.
'''
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def postorder(node, lis):
            if not node:
                return
            postorder(node.left, res)
            postorder(node.right, res)
            lis.append(node.val)
        postorder(root, res)
        
        return res