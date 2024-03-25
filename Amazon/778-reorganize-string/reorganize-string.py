class Solution:
    def reorganizeString(self, s: str) -> str:
        sc = Counter(s)
        res = ''
        maxHeap = [[-cnt,char] for char,cnt in sc.items()]
        heapq.heapify(maxHeap) # O(n)
        prev = None

        while maxHeap or prev:
            # if there is a previous char but heap is empty then invalid
            if prev and not maxHeap:
                return ""
            # add most frequent char except the previous
            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1

            # push the prev value again to heap as we can consider it now
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            # ignore the current character for next iteration
            if cnt != 0:
                prev = [cnt, char]

        return res
