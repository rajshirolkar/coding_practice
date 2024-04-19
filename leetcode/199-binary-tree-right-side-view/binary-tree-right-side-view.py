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
            rightSide = None
            for i in range(que_len):
                node = que.popleft()
                if node:
                    rightSide = node
                    que.append(node.left)
                    que.append(node.right)
            if rightSide:
                res.append(rightSide.val)
        return res