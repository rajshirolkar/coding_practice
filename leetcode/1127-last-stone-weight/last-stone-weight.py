class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_stones = [-s for s in stones]
        heapq.heapify(max_stones)
        
        while len(max_stones) > 1:
            y = -1 * heapq.heappop(max_stones)
            x = -1 * heapq.heappop(max_stones)
            if x != y:
                z = y-x
                heapq.heappush(max_stones, -z)
        return -max_stones[0] if max_stones else 0