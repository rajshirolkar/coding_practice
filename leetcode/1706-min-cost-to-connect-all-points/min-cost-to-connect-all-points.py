class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points) 
        visit = set()
        minHeap = [(0,0)]
        # heapq.heapify(minHeap)
        total_cost = 0

        while len(visit) < N:
            cost, curr = heapq.heappop(minHeap)
            if curr in visit:
                continue
            visit.add(curr)
            total_cost += cost
            x, y = points[curr]

            for i in range(N):
                if i not in visit:
                    x1, y1 = points[i]
                    next_cost = abs(x-x1) + abs(y-y1)
                    heapq.heappush(minHeap, (next_cost, i))
        return total_cost
        