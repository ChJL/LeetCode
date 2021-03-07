# Tag: DFS, BFS
'''
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 2

Example 2:
Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5

SOL: see the code, in this prob, bfs would be faster.
'''

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # DFS

        # leaf
        if not root:
            return 0
        
        # one side have no child, should take another side
        if not root.left or not root.right:
            return 1 + max(self.minDepth(root.left),self.minDepth(root.right))
        
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

    def minDepth_bfs(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        d = 0
        current = [root]
        
        while current:
            d +=1
            next_level = []
            for node in current:
                left = node.left
                right = node.right
                
                if not left and not right:
                    return d
                if left:
                    next_level.append(left)
                if right:
                    next_level.append(right)
                    
            current = next_level
        
        return d