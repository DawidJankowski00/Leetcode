import sys
import time
import copy
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.candy([1,0,2,3,0,5]))
    print(time.time() - start)

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1]* n
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                if candies[i] < candies[i+1] + 1:
                    candies[i] = candies[i+1] + 1
        return sum(candies)
        
        

if __name__ == '__main__':
    sys.exit(main())