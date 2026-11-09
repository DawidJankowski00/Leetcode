from typing import List
from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        n = len(s)
        if k > n:
            return False
        chars = Counter(s)
        odds = 0
        for v in chars.keys():
            if chars[v] % 2 == 1:
                odds += 1
        if k < odds:
            return False
        return True
