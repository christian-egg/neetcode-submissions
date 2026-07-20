# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    answer = None
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Depth first search
        # Have is_p_descendant and is_q_descendant variables
        # The first node found to have both be true is the answer

        
        def helper(node, p, q):
            # First check if current node is p/q
            # Then run recursive subtasks
            # return value will be (ANSWER, is_p_descendant, is_q_descendant)
            if (node == None):
                return (False, False)

            is_p_desc = False
            is_q_desc = False
            
            if (node.val == p.val):
                is_p_desc = True
            elif (node.val == q.val):
                is_q_desc = True
            
            if (node.left != None):
                left_results = helper(node.left, p, q)
            else:
                left_results = (False, False)
            
            if (self.answer != None):
                return (True, True)

            if (node.right != None):
                right_results = helper(node.right, p, q)
            else:
                right_results = (False, False)
            
            if (self.answer != None):
                return (True, True)

            if (left_results[0] or right_results[0]):
                is_p_desc = True
            
            if (left_results[1] or right_results[1]):
                is_q_desc = True

            if (is_p_desc and is_q_desc and self.answer == None):
                self.answer = node
            
            return (is_p_desc, is_q_desc)

        helper(root, p, q)
        return self.answer