class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dgraph = defaultdict(list)
        visit = set()

        for course, preq in prerequisites:
            dgraph[course].append(preq)
        
        def dfs(node):
            if node in visit:
                return False
            if len(dgraph[node]) == 0:
                return True 
            visit.add(node)
            for nei in dgraph[node]:
                if not dfs(nei):
                    return False
            visit.remove(node)
            dgraph[node] = []
            return True
            

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
