# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def helper(root, depth):
        # Count depth and return whether root is balanced
            left_bal, left_depth = helper(root.left, depth+1) if root.left else (True, depth)
            right_bal, right_depth = helper(root.right, depth+1) if root.right else (True, depth)

            max_depth = max(left_depth, right_depth)

            if not (left_bal and right_bal):
                return (False, max_depth)
            elif abs(left_depth - right_depth) > 1:
                return (False, max_depth)
            else:
                return (True, max_depth)

        is_bal, max_depth = helper(root, 0)

        return is_bal