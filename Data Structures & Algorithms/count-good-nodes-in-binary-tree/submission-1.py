# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Recursive, keep track of the largest node you've seen on your current path
        if (root == None):
            return 0

        def helper(node, max_val):

            count = 0
            
            if (node.val >= max_val):
                count += 1
            
            new_max = max(max_val, node.val)
            
            if (node.left != None):
                count += helper(node.left, new_max)
            if (node.right != None):
                count += helper(node.right, new_max)

            return count 
        
        return helper(root, root.val - 1)
