# Tag: Recursion

'''
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        #Base case 1: passed leaf node, reutrn empty list.
        if not root:
            return []
        
        #Base case 2: leaf node, reutrn list of the current leaf node value value as string
        if not root.left and not root.right:
            return [str(root.val)]
        
        #Merge all the ararays of strings that come back from the left and right children.
        
        paths = [str(root.val)+'->'+ i for i in self.binaryTreePaths(root.left)]
        paths += [str(root.val)+'->'+ i for i in self.binaryTreePaths(root.right)]
        
        return paths
        