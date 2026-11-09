from typing import List

class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        l = 0
        r = 0
        if s[0] == "0":
            l = 1
        for i in range(1, n):
            if s[i] == "1":
                r += 1
        result = l + r
        for i in range(1, n-1):
            if s[i] == "0":
                l += 1
            else:
                r -= 1
            if result < r + l:
                result = r + l
        return result
