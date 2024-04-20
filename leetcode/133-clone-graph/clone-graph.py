"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # DFS approach
        # new_dict = {}
        # if not node:
        #     return None

        # def dfs(node):
        #     if node.val in new_dict:
        #         return new_dict[node.val]
            
        #     copy_node = Node(node.val)
        #     new_dict[node.val] = copy_node
        #     for nei in node.neighbors:
        #         copy_node.neighbors.append(dfs(nei))
        #     return copy_node
        # return dfs(node)

        """
        BFS Approach
            {
                1: node1;
                2: node2;
                3: node3;
                4: node4;
            }

            1 -> 2, 4
            2 -> 3, 1
            3 -> 2, 4
            4 -> 3, 1
        """
        if node is None:
            return None

        node_dict = {node.val: Node(node.val)}
        start = node
        q = deque([start])
        while q:
            n = q.popleft()
            new_node = node_dict[n.val]

            for nei in n.neighbors:
                if nei.val in node_dict:
                    new_node.neighbors.append(node_dict[nei.val])
                else:
                    new_nei_node = Node(nei.val)
                    node_dict[nei.val] = new_nei_node
                    new_node.neighbors.append(new_nei_node)
                    q.append(nei)
        # print(node_dict)
        return node_dict[node.val]