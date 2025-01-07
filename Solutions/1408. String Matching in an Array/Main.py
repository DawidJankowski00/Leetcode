from collections import defaultdict
import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.stringMatching(["leetcoder","leetcode","od","hamlet","am"]))
    print(time.time() - start)

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = set()
        for i in range(len(words)):
            for v in words : 
                if v  in words[i] and v != words[i]:
                    result.add(v)
        return list(result)  

        

if __name__ == '__main__':
    sys.exit(main())