from typing import List
from collections import Counter

class Solution:
    def minimumLength(self, s: str) -> int:
        result = 0
        for i in range(0, 26):
            tmp = s.count(chr(ord('a') + i))
            if tmp % 2 == 1:
                result += 1
            elif tmp != 0:
                result += 2
        return result
