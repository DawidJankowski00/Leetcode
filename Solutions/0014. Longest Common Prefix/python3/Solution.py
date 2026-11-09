import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.longestCommonPrefix(["flower","flow","flight"]))
    print(time.time() - start)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        strs = sorted(strs)
        f = strs[0]
        l = strs[-1]
        for i in range(min(len(f), len(l))):
            if f[i] != l[i]:
                return result
            result += f[i]
        return result

if __name__ == '__main__':
    sys.exit(main())