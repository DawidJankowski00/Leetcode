import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.partitionLabels("ababcbacadefegdehijhklij"))
    print(time.time() - start)

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        htab = {}
        for i, v in enumerate(s):
            htab[v] = i
        result = []
        tmp_max = 0
        l = 0
        for i in range(len(s)):
            tmp_max = max(htab[s[i]], tmp_max)
            if i == tmp_max:
                result.append(i-l+1)
                l = i+1
        return result
        

if __name__ == '__main__':
    sys.exit(main())