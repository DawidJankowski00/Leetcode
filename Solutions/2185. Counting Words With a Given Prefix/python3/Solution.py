from typing import List

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        result = 0
        for v in words:
            if v.startswith(pref):
                result += 1
        return result
