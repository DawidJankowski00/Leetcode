import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.addSpaces("LeetcodeHelpsMeLearn", [8,13,15]))
    print(time.time() - start)

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        t = ""
        j = 0
        m = len(spaces)
        for i, v in enumerate(s):
            if m > j:
                if i == spaces[j]:
                    j += 1
                    t += " "
            t += v
        return t

if __name__ == '__main__':
    sys.exit(main())