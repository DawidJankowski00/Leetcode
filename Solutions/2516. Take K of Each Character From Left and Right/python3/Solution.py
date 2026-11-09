from typing import List

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        limits = {c: s.count(c) - k for c in 'abc'}
        if min(limits.values())<0:
            return-1

        l = 0
        result = 0
        for r, val in enumerate(s):
            limits[val] -= 1
            while limits[val] < 0:
                limits[s[l]] += 1
                l += 1
            result = max(result, r-l+1)
        return len(s) - result
