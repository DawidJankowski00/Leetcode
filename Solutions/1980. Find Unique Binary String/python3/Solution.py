import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.findDifferentBinaryString(["111","011","001"]))
    print(time.time() - start)

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        tab = {}
        n = len(nums)
        for v in nums:
            tab[int(v,2)] = True
        i = 0
        result = ''
        while True:
            if i in tab:
                i += 1
            else:
                result = bin(i)[2:]
                break
        while len(result) != n:
            result = '0' + result
        return result


        

if __name__ == '__main__':
    sys.exit(main())