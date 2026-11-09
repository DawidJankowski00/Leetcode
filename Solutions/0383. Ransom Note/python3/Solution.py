from typing import List
from collections import defaultdict, Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = Counter(magazine)
        for v in ransomNote:
            if v not in dic:
                return False
            if dic[v] > 0:
                dic[v] -= 1
                if dic[v] == 0:
                    del dic[v]
        return True
