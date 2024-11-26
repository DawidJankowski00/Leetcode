import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.findChampion(3, [[0,1],[1,2]]))
    print(time.time() - start)

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        tab = {}
        for el in range(n):
            tab[el] = 1
        for el in edges:
            if el[1] in tab:
                del tab[el[1]]
        if len(tab.keys()) == 1:
            return list(tab.keys())[0]
        return -1


        

if __name__ == '__main__':
    sys.exit(main())