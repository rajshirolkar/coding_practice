# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        que = deque()
        que.append(root)

        while que:
            que_len = len(que)
            cur_level = []

            for _ in range(que_len):
                node = que.popleft()
                if node:
                    cur_level.append(node.val)
                    que.append(node.left)
                    que.append(node.right)
            if cur_level:
                res.append(cur_level)
        return res