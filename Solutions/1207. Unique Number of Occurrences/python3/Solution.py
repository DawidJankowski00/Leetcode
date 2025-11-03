from collections import defaultdict
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        myset = defaultdict(int)
        for v in arr:
            myset[v] += 1
        
        return len(myset.values()) == len(set(myset.values()))
