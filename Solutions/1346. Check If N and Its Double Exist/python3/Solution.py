from collections import defaultdict
import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.checkIfExist([-2,0,10,-19,4,6,-8]))
    print(time.time() - start)

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        elems = defaultdict(int)
        for item in arr:
            elems[item] += 1
        for item in arr:
            if item == 0:
                if elems[item*2] > 1:
                    return True
            elif elems[item*2]:
                return True
        return False

        

if __name__ == '__main__':
    sys.exit(main())