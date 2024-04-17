# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def dfs(node, pathsum):
            # if not node:
            #     if pathsum == targetSum:
            #         return True
            #     return False
            if not node:
                return False
            pathsum += node.val
            if not node.left and not node.right:
                if pathsum == targetSum:
                    return True
                return False


            return dfs(node.left, pathsum) or dfs(node.right, pathsum)
        return dfs(root, 0)