import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.doesValidArrayExist([1,1,0]))
    print(time.time() - start)

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        result = 0
        for v in derived:
            result ^= v
        return result == 0
        

if __name__ == '__main__':
    sys.exit(main())