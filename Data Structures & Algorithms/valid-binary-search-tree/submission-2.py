# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Recursive, need current node, max, and min

        def helper(node, min_val, max_val):
            if (node == None):
                return True
            if (node.val <= min_val or node.val >= max_val):
                return False
            
            left_result = helper(node.left, min_val, node.val)
            right_result = helper(node.right, node.val, max_val)
            return (left_result and right_result)

        
        return helper(root, -1001, 1002)
            