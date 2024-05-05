class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        for s, e, w in times:
            adj_list[s].append((e, w))

        # print(adj_list)
        paths = []
        vis = set()
        total_time = 0
        heapq.heappush(paths, (0, k))
        
        while paths and len(vis) < n:
            # print(paths)
            curr_time, src = heapq.heappop(paths)
            total_time = curr_time
            if src in vis:
                continue
            vis.add(src)
            # print(time_dict)
            for nxt, wt in adj_list[src]:
                if nxt not in vis:
                    heapq.heappush(paths, (curr_time + wt, nxt))
        
        return total_time if len(vis) == n else -1