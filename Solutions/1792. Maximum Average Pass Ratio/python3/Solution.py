import sys
import time
import heapq
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.maxAverageRatio([[1,2],[3,5],[2,2]], 2))
    print(time.time() - start)

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:

        max_heap = [((passed + 1) / (total + 1) - passed / total, passed, total) for passed, total in classes]
        heapq.heapify(max_heap)
        for _ in range(extraStudents):
            g, passed, total = heapq.heappop(max_heap)
            heapq.heappush(max_heap, ((passed + 1) / (total + 1) - passed / total, passed, total))

        return sum(passed / total for _, passed, total in max_heap) / len(classes)

if __name__ == '__main__':
    sys.exit(main())