from collections import defaultdict
import heapq
from typing import List

class NumberContainers:

    def __init__(self):
        self.tab = {}
        self.index = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        self.tab[index] = number
        heapq.heappush(self.index[number], index)

    def find(self, number: int) -> int:
        if number not in self.index:
            return -1
        while self.index[number]:
            i = self.index[number][0]
            if self.tab[i] == number:
                return i
            heapq.heappop(self.index[number])
        return -1
