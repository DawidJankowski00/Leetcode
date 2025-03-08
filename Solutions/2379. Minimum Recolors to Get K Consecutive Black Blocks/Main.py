import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.minimumRecolors("WBBWWBBWBW",7))
    print(time.time() - start)

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        curr = blocks[:k].count("W")
        l = 0
        r = k
        result = curr
        while r < len(blocks):
            if blocks[l] == "W":
                curr -= 1
            if blocks[r] == "W":
                curr += 1
            if curr < result:
                result = curr
            l += 1
            r += 1
        return result

if __name__ == '__main__':
    sys.exit(main())