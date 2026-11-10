from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_len = 0
        last_index = {}
        l = 0
        for r in range(n):
            l = max(l, last_index.get(s[r], 0))
            max_len = max(max_len, r - l + 1)
            last_index[s[r]] = r+1
        return max_len
