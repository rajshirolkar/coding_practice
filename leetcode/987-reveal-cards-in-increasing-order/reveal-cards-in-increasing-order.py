class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        q = deque()
        for card in sorted(deck, reverse=True):
            if q:
                q.appendleft(q.pop())
                # print("if ", q)
            q.appendleft(card)
            # print(q)
        return list(q)