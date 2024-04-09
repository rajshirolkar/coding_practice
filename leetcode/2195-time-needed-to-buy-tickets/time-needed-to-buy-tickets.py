class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        for i, n in enumerate(tickets):
            if i <= k:
                time += min(n, tickets[k])
            else:
                time += min(n, tickets[k]-1)
        return time
