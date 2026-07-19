from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Put everything into a queue and go in that order
        if (root == None):
            return []
            
        queue = deque()
        level_list = []
        queue.append((0, root))

        while queue:
            level, node = queue.popleft()
            if (node.left != None):
                queue.append((level+1, node.left))
            if (node.right != None):
                queue.append((level+1, node.right))

            if (len(level_list) < level + 1):
                level_list.append([])
            
            level_list[level].append(node.val)

        return level_list
