from collections import defaultdict, Counter
from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        neded = defaultdict(int)
        for v in words2:
            tmp = Counter(v)
            for k in tmp.keys():
                if neded[k] < tmp[k]:
                    neded[k] = tmp[k]
        result = []
        for v in words1:
            tmp = Counter(v)
            test = True
            for k in neded.keys():
                if tmp[k] < neded[k]:
                    test = False
            if test:
                result.append(v)
        return result
