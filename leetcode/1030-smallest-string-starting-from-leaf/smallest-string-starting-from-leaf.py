# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        
        res = []
        def dfs(node, s):
            if node:
                prefix = chr(node.val + 97)

                if not node.left and not node.right:
                    res.append(prefix + s)
                    return
                
                if node.left:
                    dfs(node.left, prefix+s)
                if node.right:
                    dfs(node.right, prefix+s)
                return
            return
        dfs(root, '')
        res.sort()
        return res[0]