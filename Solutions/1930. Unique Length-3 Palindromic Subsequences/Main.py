from collections import Counter, defaultdict
from email.policy import default
import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.countPalindromicSubsequence("aabca"))
    print(time.time() - start)

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        result = 0
        s_set = defaultdict(list)
        s_at_least_2 = defaultdict(bool)
        for i in range(len(s)):
            if s[i] in s_set:
                if len(s_set[s[i]]) == 2:
                    s_set[s[i]][1] = i
                else:
                    s_set[s[i]].append(i)
                s_at_least_2[s[i]] = True
            else:
                s_set[s[i]].append(i)
        for v in s_at_least_2.keys():
            tmp = Counter(s[s_set[v][0]+1:s_set[v][1]])
            result += len(tmp.keys())
        return result

if __name__ == '__main__':
    sys.exit(main())