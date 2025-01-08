import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.countPrefixSuffixPairs(["a","aba","ababa","aa"]))
    print(time.time() - start)

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        m = len(words)
        result = 0
        for i in range(0, m):
            for j in range(i+1, m):
                if i == j:
                    continue
                if self.isPrefixAndSuffix(words[i], words[j]):
                    result += 1
        return result
        

    def isPrefixAndSuffix(self, str1: str, str2: str):
        n = len(str1)
        l = len(str2)
        if n > len(str2):
            return False
        if str2[0:n] != str1:
            return False
        if str2[l-n:] != str1:
            return False
        return True
        

if __name__ == '__main__':
    sys.exit(main())