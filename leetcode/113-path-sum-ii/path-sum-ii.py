# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        def dfs(node, pathsum, path):
            if not node:
                return
            pathsum += node.val
            path = path[::]
            path.append(node.val)
            if not node.left and not node.right:
                if pathsum == targetSum:
                    res.append(path)
                return
            if node.left:
                dfs(node.left, pathsum, path)
            if node.right:
                dfs(node.right, pathsum, path)
            return
        dfs(root, 0, [])
        return res