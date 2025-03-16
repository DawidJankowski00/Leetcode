import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.repairCars([4,2,3,1],10))
    print(time.time() - start)

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l = 1
        r = min(ranks) * cars * cars

        def helper(time):
            counter = 0
            for r in ranks:
                counter += int(((time/r) ** 0.5))
                if counter >= cars:
                    return True
            return False

        while l < r:
            mid = (r+l) // 2
            if helper(mid):
                r = mid
            else:
                l = mid + 1
        return l
        

if __name__ == '__main__':
    sys.exit(main())