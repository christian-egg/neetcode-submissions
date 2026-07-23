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
        # First is answer, second is whether or not it has been found yet
        res = [0, False]

        def dfs(node, num_smaller, res):
            if node == None or res[1]:
                return 0


            left = dfs(node.left, num_smaller, res)
            total_num_smaller = num_smaller + left
            right = dfs(node.right, total_num_smaller + 1, res)

            if (not res[1] and k == total_num_smaller + 1):
                res[0] = node.val
                res[1] = True
            
            return left + right + 1
        
        dfs(root, 0, res)
        return res[0]