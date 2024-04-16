# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root, None)
        
        que = deque([root])
        cur_depth = 1
        while que:
            if cur_depth == depth-1:
                break
            
            for _ in range(len(que)):
                cur_node = que.popleft()

                if cur_node.left:
                    que.append(cur_node.left)
                if cur_node.right:
                    que.append(cur_node.right)
                
            cur_depth += 1
        
        for node in que:
            cur_left = node.left
            node.left = TreeNode(val, cur_left, None)

            cur_right = node.right
            node.right = TreeNode(val, None, cur_right)
        
        return root