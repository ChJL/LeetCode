# Tag: Tree
'''
Given the root of a Binary Search Tree (BST), 
return the minimum absolute difference between the values of any two different nodes in the tree.
Example1:
  4
  /\
 2  6
 /\
1  3
Input: root = [4,2,6,1,3]
Output: 1

SOL: inorder traversal, calculate the diff and keep record the minimum one.
'''
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.minimum = float('inf')
        self.prev = float('inf')
        
        def inorder(node):
            if node:
                inorder(node.left)
                self.minimum = min(self.minimum, abs(node.val - self.prev))
                self.prev = node.val
                inorder(node.right)
        inorder(root)
        return self.minimum