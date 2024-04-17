# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        self.depth = float(inf)
        if not root:
            return 0
        def dfs(node, depth):
            if node:
                if not node.left and not node.right:
                    self.depth = min(self.depth, depth)
                else:
                    dfs(node.left, depth + 1)
                    dfs(node.right, depth + 1)
            return
        dfs(root, 1)
        return self.depth