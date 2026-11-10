from typing import List
from collections import Counter

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        freq1 = Counter(tiles)
        def count_it(freq):
            tmp = 0
            for key in freq.keys():
                if freq[key] == 0:
                    continue
                freq[key] -= 1
                tmp += count_it(freq) + 1
                freq[key] += 1
            return tmp
        return count_it(freq1)
