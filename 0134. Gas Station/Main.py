import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))
    print(time.time() - start)

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        start = current_gas = 0
        for i in range(len(gas)):
            current_gas += gas[i]
            current_gas -= cost[i]
            if current_gas < 0:
                start = i + 1
                current_gas = 0
        return start

if __name__ == '__main__':
    sys.exit(main())