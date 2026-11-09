from collections import defaultdict
import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    print(time.time() - start)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for v in strs:
            result["".join(sorted(v))].append(v)
        return list(result.values())
        

if __name__ == '__main__':
    sys.exit(main())