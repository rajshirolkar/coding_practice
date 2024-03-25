# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not k:
            return [target.val]
        
        graph = defaultdict(list)
        que = deque([root])

        # add nodes in the graph
        while que:
            node = que.popleft()
            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)

                que.append(node.left)
            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)

                que.append(node.right)
        
        que = deque([(target, 0)])
        visit = set([target])
        res = []
        while que:
            node, dist = que.popleft()

            if dist == k:
                res.append(node.val)
            else:
                for i in graph[node]:
                    if i not in visit:
                        visit.add(i)
                        que.append((i, dist+1))
        return res