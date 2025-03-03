import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.pivotArray([9,12,5,10,14,3,10],10))
    print(time.time() - start)

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lower = []
        equal = []
        greather = []
        for v in nums:
            if v < pivot:
                lower.append(v)
            elif v == pivot:
                equal.append(v)
            else:
                greather.append(v)
        return lower + equal + greather

        

if __name__ == '__main__':
    sys.exit(main())