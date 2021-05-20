# Tag: Tree
'''
Given the root of a binary search tree (BST) with duplicates, 
return all the mode(s) (i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.
Example1:
1
  \
   2
  /
 2
Input: root = [1,null,2,2]
Output: [2]

SOL: inorder traversal all node, and record the val:count in a hash table. Afterward, find max in the dict.

'''
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        self.d = {}
        
        def search(node):
            if node:
                if node.val not in self.d:
                    self.d[node.val] = 1
                else:
                    self.d[node.val] += 1
                search(node.left)
                search(node.right)
        search(root)
        
        res = []
        maxim = 0
        for key, value in self.d.items():
            if value > maxim:
                maxim = value
                res = []
                res.append(key)
            elif value == maxim:
                res.append(key)
        return res