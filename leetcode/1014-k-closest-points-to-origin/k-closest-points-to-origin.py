class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for x,y in points:
            distances.append((x**2+y**2, x, y))
        heapq.heapify(distances)
        res = []
        while k > 0:
            k-=1 
            dist, x, y = heapq.heappop(distances)
            res.append([x,y])
        return res