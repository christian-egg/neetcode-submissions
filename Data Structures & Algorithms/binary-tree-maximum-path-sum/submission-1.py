# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0        
        
        # passable by reference max variable
        max_sum = [float("-inf")]

        def helper(root):
            # Helper will return the best path down where this node is at one end
            # Will also calculate best path in this sub-tree containing root
            # Will also update max_sum if new best path is found

            left_sum = helper(root.left) if root.left else 0
            right_sum = helper(root.right) if root.right else 0

            cross_path_sum = max(left_sum, 0) + root.val + max(right_sum, 0)

            if cross_path_sum > max_sum[0]:
                max_sum[0] = cross_path_sum
            
            return root.val + max(left_sum, right_sum, 0)
 

        helper(root)
        return max_sum[0]



