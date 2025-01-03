import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.insert([[1,3],[6,9]],[2,5]))
    print(time.time() - start)

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        intervals.append(newInterval)
        intervals.sort()
        start, stop = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= stop:
                if intervals[i][1] > stop:
                    stop = intervals[i][1]
            else:
                result.append([start, stop])
                start, stop = intervals[i]
        result.append([start, stop])
        return result
        

if __name__ == '__main__':
    sys.exit(main())