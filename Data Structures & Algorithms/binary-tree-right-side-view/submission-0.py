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
        
        queue = deque()
        
        right_view = []
        
        queue.append((0, root))

        prev_val = None
        prev_level = 0

        while len(queue) > 0:
            level, node = queue.popleft()

            if (level > prev_level):
                # Save prev node's value to right_view
                right_view.append(prev_val)
            
            prev_val = node.val
            prev_level = level

            if node.left:
                queue.append((level+1, node.left))
            if node.right:
                queue.append((level+1,node.right))

        # Add the final prev_value
        right_view.append(prev_val)
        
        return right_view
            


