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
        st = " ".join(words)
        return [v for v in words if st.count(v) >=2]

        

if __name__ == '__main__':
    sys.exit(main())