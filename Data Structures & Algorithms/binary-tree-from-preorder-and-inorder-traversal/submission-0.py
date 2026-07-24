# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        
        # Pre-order is Root -> Left -> Right
        # Basically goes left as possible (while still adding its nodes) before going right

        # In-order is Left -> root -> Right
        # First node in in-order will be the end of the left -> left -> ... -> left path
        # Next node will be the prev node's parent

        # Use hash table to store indices in [Pre, In] format
        
        preorder_pos = [0]

        inorder_dict = {}

        for i in range(len(inorder)):
            inorder_dict[inorder[i]] = i
        
        # In-order splits tree by its root
        def dfs(left, right):
            if (preorder_pos[0] >= len(preorder) or left > right):
                return None
            
            root_val = preorder[preorder_pos[0]]
            preorder_pos[0] += 1

            split_idx = inorder_dict[root_val]

            left_child = dfs(left, min(split_idx - 1, right))
            right_child = dfs(max(split_idx + 1, left), right)

            return TreeNode(root_val, left_child, right_child)

        return dfs(0, len(preorder) - 1)


