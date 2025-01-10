from collections import defaultdict, Counter
import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.wordSubsets(["amazon","apple","facebook","google","leetcode"],["e","o"]))
    print(time.time() - start)

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        neded = defaultdict(int)
        for v in words2:
            tmp = Counter(v)
            for k in tmp.keys():
                if neded[k] < tmp[k]:
                    neded[k] = tmp[k]
        result = []
        for v in words1:
            tmp = Counter(v)
            test = True
            for k in neded.keys():
                if tmp[k] < neded[k]:
                    test = False
            if test:
                result.append(v)
        return result

        

if __name__ == '__main__':
    sys.exit(main())