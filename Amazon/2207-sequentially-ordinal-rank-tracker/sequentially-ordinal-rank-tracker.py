from sortedcontainers import SortedList
class SORTracker:

    def __init__(self):
        self.sort_list = SortedList()
        self.query_count = 0

    def add(self, name: str, score: int) -> None:
        self.sort_list.add((-score, name))

    def get(self) -> str:
        res = self.sort_list[self.query_count][1]
        self.query_count += 1
        return res


# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()