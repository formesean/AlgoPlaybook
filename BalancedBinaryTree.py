# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        balanced = [True]

        def helper(root):
            if not root:
                return True
            
            left_height = helper(root.left)     # get left height
            right_height = helper(root.right)   # get right height

            if left_height is None or right_height is None:
                return

            if abs(left_height - right_height) > 1: # balanced when <= 1
                balanced[0] = False                 # not balanced since calculated height is > 1
                return
            
            return 1 + max(left_height, right_height) # return the height
        
        helper(root)
        return balanced[0]
        
