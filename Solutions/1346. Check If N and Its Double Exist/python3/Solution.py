from collections import defaultdict
from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        elems = defaultdict(int)
        for item in arr:
            elems[item] += 1
        for item in arr:
            if item == 0:
                if elems[item*2] > 1:
                    return True
            elif elems[item*2]:
                return True
        return False
