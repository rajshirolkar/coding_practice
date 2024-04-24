class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq  = Counter(tasks)
        maxHeap = [-cnt for cnt in freq.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque() # pairs of [-cnt, idleTime]
        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = heapq.heappop(maxHeap)
                cnt += 1
                if cnt:
                    q.append([cnt, time+n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time

