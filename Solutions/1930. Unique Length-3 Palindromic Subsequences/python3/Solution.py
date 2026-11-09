from collections import Counter, defaultdict
from email.policy import default
from typing import List

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        result = 0
        
        for i in range(26):
            l = s.find(chr(ord('a') + i))
            r = s.rfind(chr(ord('a') + i))
            if l != r:
                result += len(set(s[l+1:r]))
        return result
