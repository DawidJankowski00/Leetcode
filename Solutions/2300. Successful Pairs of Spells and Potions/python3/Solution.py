import bisect
from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort(reverse=True)
        pairs = []
        n = len(potions)
        for v in spells:
            needed = (success + v - 1) // v
            
            pairs.append(n - bisect.bisect_left(potions, needed))
        return pairs