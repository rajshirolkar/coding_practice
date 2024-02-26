# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def fx(p, q):
            if p and q:
                if p.val != q.val:
                    return False
                return fx(p.left, q.left) and fx(p.right, q.right)
            if not p and not q:
                return True
            return False
        return fx(p,q)