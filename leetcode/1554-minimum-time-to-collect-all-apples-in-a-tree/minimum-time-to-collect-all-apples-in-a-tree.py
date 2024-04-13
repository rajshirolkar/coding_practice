class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj_list = defaultdict(list)

        for k, v in edges:
            adj_list[k].append(v)
            adj_list[v].append(k)
            
        def fx(vtx, par):
            steps = 0
            for child in adj_list[vtx]:
                if child == par:
                    continue
                child_steps = fx(child, vtx)
                if child_steps or hasApple[child]:
                    steps += 2 + child_steps
            return steps
        return fx(0, -1)