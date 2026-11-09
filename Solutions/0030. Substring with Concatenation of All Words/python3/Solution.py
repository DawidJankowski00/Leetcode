from collections import defaultdict, Counter
import copy
import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.findSubstring("barfoothefoobarman", ["foo","bar"]))
    print(time.time() - start)

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        dic = defaultdict(int)
        n = len(words[0])
        for v in words:
            dic[v] += 1
        m = len(s)
        result = []
        for i in range(n):
            l = i
            window = defaultdict(int)
            c = 0
            for j in range(i, m, n):
                word = s[j:j+n]
                if word not in dic:
                    l = j + n
                    window = defaultdict(int)
                    c = 0
                    continue
                c += 1
                window[word] += 1
                while window[word] > dic[word]:
                    window[s[l:l + n]] -= 1
                    l += n
                    c -= 1
                if c == len(words):
                    result.append(l)
        return result


if __name__ == '__main__':
    sys.exit(main())