class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        visit = set()

        for k, v in edges:
            graph[k].append(v)
            graph[v].append(k)
        
        # BFS approach
        que = deque([source])
        visit.add(source)
        while que:
            node = que.popleft()
            if node == destination:
                return True
            for nei in graph[node]:
                if nei not in visit:
                    visit.add(nei)
                    que.append(nei)
        return False
        
        # DFS Approach
        # def dfs(node):
        #     if node == destination:
        #         return True
        #     visit.add(node)
        #     for nei in graph[node]:
        #         if nei not in visit:
        #             if dfs(nei):
        #                 return True
        #     return False
        # return dfs(source)
