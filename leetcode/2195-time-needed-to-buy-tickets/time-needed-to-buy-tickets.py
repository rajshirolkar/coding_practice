class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        for i, n in enumerate(tickets):
            if i <= k:
                if n <= tickets[k]:
                    time += n
                else:
                    time += tickets[k]
            else:
                if n < tickets[k]:
                    time += n
                else:
                    time += tickets[k]-1
        return time
