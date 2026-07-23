# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # DFS, helper function returns number of elements down a branch
        # Helper function also provides number of elements smaller than current
        res = [0]

        def dfs(node, num_smaller, res):
            if node == None:
                return 0

            left = dfs(node.left, num_smaller, res)
            total_num_smaller = num_smaller + left
            right = dfs(node.right, total_num_smaller + 1, res)

            if (k == total_num_smaller + 1):
                res[0] = node.val
            
            return left + right + 1
        
        dfs(root, 0, res)
        return res[0]