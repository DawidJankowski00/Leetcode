import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.maxScoreSightseeingPair([8,1,5,2,6]))
    print(time.time() - start)

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        dp = 0
        score=0
        for i, x in enumerate(values):
            score=max(score, dp+x-i)
            dp=max(dp, x+i)
        return score
        
        
        

if __name__ == '__main__':
    sys.exit(main())