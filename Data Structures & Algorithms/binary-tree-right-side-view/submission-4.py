# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Depth-first traversal but always taking the right node first
        # First node of each level seen is added to result list
        # Use length of result list to track recorded depth
        if root is None:
            return []

        res = []

        def dfs(node, depth, res):
            if (depth == len(res)):
                res.append(node.val)
            
            if node.right:
                dfs(node.right, depth+1, res)
            if node.left:
                dfs(node.left, depth+1, res)

        dfs(root, 0, res)
        return res