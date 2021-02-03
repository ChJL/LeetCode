# Tag: Recursion
'''
Given the root of a binary search tree and the lowest and highest boundaries as low and high, 
trim the tree so that all its elements lies in [low, high]. T
rimming the tree should not change the relative structure of the elements that will remain in the tree 
(i.e., any node's descendant should remain a descendant). It can be proven that there is a unique answer.

Return the root of the trimmed binary search tree. Note that the root may change depending on the given bounds.

SOL: 
code1: from official solution:
When node.val > high, we know that the trimmed binary tree must occur to the left of the node. Similarly, when node.val < low, the trimmed binary tree occurs to the right of the node. Otherwise, we will trim both sides of the tree.

code2 : same way:
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        # 每一层的Condition
        if not root: return root
        if root.val > high: return self.trimBST(root.left, low, high)
        if root.val < low: return self.trimBST(root.right, low, high)

        # 再区间内，正常的Recursion
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        
        # 返回给parent一个区间调整完以后的subtree
        return root
'''
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        def trim(node):
            if not node:
                return None
            elif node.val > high:
                return trim(node.left)
            elif node.val < low:
                return trim(node.right)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node
        return trim(root)