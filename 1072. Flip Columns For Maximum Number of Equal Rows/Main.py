import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()

    print(sol.maxEqualRowsAfterFlips([[0,0,0],[0,0,1],[1,1,0]]))
    print(time.time() - start)

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        mytable = {}
        for m in matrix:
            tmp = ''.join(format(x, 'b') for x in m)
            if tmp in mytable:
                mytable[tmp] += 1
            else:
                mytable[tmp] = 1
            tmp = ''.join(format(x, 'b') for x in self.flip(m))
            if tmp in mytable:
                mytable[tmp] += 1
            else:
                mytable[tmp] = 1
        return max(mytable.values())
    def flip(self, column):
        for i in range(0, len(column)):
            if column[i] == 0:
                column[i] = 1
            else:
                column[i] = 0
        return column


if __name__ == '__main__':
    sys.exit(main())

