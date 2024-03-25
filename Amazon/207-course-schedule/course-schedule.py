class Solution:
    def canFinish(self, numCourses: int, preq: List[List[int]]) -> bool:
        alst = defaultdict(list)
        for i in preq:
            alst[i[0]].append(i[1])
        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            if alst[crs] == []:
                return True
            
            visited.add(crs)
            for pre in alst[crs]:
                if not dfs(pre): return False
            visited.remove(crs)
            alst[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True