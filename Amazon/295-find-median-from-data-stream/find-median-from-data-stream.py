class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.maxheap = []  # Max heap (simulated with negative values)
        self.minheap = []  # Min heap

    def addNum(self, num: int) -> None:
        """
        Adds a number into the data structure.
        """
        heappush(self.maxheap, -num)  # Add to max heap
        # Move the largest element of max heap to min heap
        heappush(self.minheap, -heappop(self.maxheap))

        # If maxheap has more elements, move the smallest element of large to small
        if len(self.minheap) > len(self.maxheap):
            heappush(self.maxheap, -heappop(self.minheap))

    def findMedian(self) -> float:
        """
        Returns the median of current data stream
        """
        # If the heaps have equal size, the median is the average of the two heap's top elements
        if len(self.maxheap) == len(self.minheap):
            return (-self.maxheap[0] + self.minheap[0]) / 2.0
        # If the maxheap has more elements, return the top element
        elif len(self.maxheap) > len(self.minheap):
            return -self.maxheap[0]
        # Otherwise, return the top element of the minheap
        else:
            return self.minheap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()