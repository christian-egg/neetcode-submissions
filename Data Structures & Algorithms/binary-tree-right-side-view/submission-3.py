from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Assuming we traverse the tree from left to right
        # We want the final node traversed of each level
        # Let's do a breadth-first search where queue stores (level, node)
        # And keep track of when we switch levels
        if root is None:
            return []
        
        queue = deque([root])
        
        right_view = []

        while queue:
            rightmost = None
            q_len = len(queue)

            for i in range(q_len):
                node = queue.popleft()
                
                rightmost = node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            if rightmost:
                right_view.append(rightmost)

        return right_view

