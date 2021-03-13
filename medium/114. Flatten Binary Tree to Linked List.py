# Tag: DFS
'''
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node 
in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.

Example1:
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

SOL: a solution from YT: https://www.youtube.com/watch?v=pduCoCDpZMg
with clear explanation
'''
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is not None:
            self.flatten(root.left)
            self.flatten(root.right)
            
            if root.left is not None:
                current = root.left
                while current.right is not None:
                    current = current.right
                current.right = root.right
                root.right = root.left
                root.left = None
        