# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        que = deque()
        que.append(root)

        while que:
            que_len = len(que)
            level = []
            for i in range(que_len):
                node = que.popleft()
                if node:
                    que.append(node.left)
                    que.append(node.right)
                    level.append(node.val)
            if level:
                res.append(level[-1])
        return res