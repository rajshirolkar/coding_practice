class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        visit = set()

        for k, v in edges:
            graph[k].append(v)
            graph[v].append(k)
        
        def dfs(node):
            if node == destination:
                return True
            visit.add(node)
            for nei in graph[node]:
                if nei not in visit:
                    if dfs(nei):
                        return True
            return False
        return dfs(source)
