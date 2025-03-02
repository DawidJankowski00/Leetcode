import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.mergeArrays([[1,2],[2,3],[4,5]],[[1,4],[3,2],[4,1]]))
    print(time.time() - start)

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        tab = {}
        for i,v in nums1:
            tab[i] = v
        for i,v in nums2:
            if i in tab:
                tab[i] += v
            else:
                tab[i] = v
        result = []
        for i in sorted(tab.keys()):
            result.append([i, tab[i]])
        return result

if __name__ == '__main__':
    sys.exit(main())