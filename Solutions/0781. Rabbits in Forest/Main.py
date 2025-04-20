import sys
import time
from typing import Counter, List
def main():
    sol = Solution()
    start = time.time()
    print(sol.numRabbits([1,1,2]))
    print(time.time() - start)

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        result = 0
        tmp = Counter(answers)
        for v in tmp.keys():
            result += (v + 1) * ((tmp[v] + v) // (v + 1))
        return result
        

if __name__ == '__main__':
    sys.exit(main())