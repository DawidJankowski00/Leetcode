from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for v in strs:
            result["".join(sorted(v))].append(v)
        return list(result.values())
