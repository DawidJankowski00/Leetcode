from typing import List

class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        j = 0
        i = 0
        while i < len(str1) and j < len(str2):
            if (ord(str2[j]) - ord(str1[i])) % 26 < 2:
                j += 1
            i += 1
        return j == len(str2)
