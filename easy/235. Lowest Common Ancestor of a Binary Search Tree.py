'''
Tag: DFS
Given a binary search tree (BST), 
find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: 
“The lowest common ancestor is defined between two nodes p and q as the lowest node in T 
that has both p and q as descendants (where we allow a node to be a descendant of itself).”

'''
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # iterative, sol from leetcode sol
        
        pval = p.val
        qval = q.val
        node = root
        
        while node:
            parent_val = node.val
            
            if pval>parent_val and qval>parent_val:
                node = node.right
            elif pval<parent_val and qval<parent_val:
                node = node.left
            else:
                return node
        