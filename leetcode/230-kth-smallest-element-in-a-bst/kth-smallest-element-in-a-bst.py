# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # self.res = []
        self.k = k
        self.ans = 0
        def dfs(node):
            if not node:
                return None
            
            dfs(node.left)
            # self.res.append(node.val)
            self.k -= 1
            if self.k == 0:
                self.ans = node.val
                return
            dfs(node.right)
        dfs(root)
        # return self.res[k-1]
        return self.ans