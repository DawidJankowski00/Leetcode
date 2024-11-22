import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.hIndex([1,3,1]))
    print(time.time() - start)

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        citations.reverse()
        result = 0
        for i in range(0, len(citations)):
            if i+1 <= citations[i]:
                result += 1
            else:
                break
        return(result)


        

if __name__ == '__main__':
    sys.exit(main())