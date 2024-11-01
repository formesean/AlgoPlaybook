# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        def isBalanced(p, q):
            if not p and not q:
                return True
                # balanced since both are null
            
            if (p and not q) or (q and not p):
                return False
                # not balanced if either p or q is null

            if p.val != q.val:
                return False
            
            return isBalanced(p.left, q.left) and isBalanced(p.right, q.right)
        
        return isBalanced(p, q)
            
