import heapq


class SmallestInfiniteSet:

    def __init__(self):
        self.min_num = 1
        self.nums = []

    def popSmallest(self) -> int:
        if self.nums:
            return heapq.heappop(self.nums)
        self.min_num += 1
        return self.min_num - 1

    def addBack(self, num: int) -> None:
        if self.min_num > num and num not in self.nums:
            heapq.heappush(self.nums, num)