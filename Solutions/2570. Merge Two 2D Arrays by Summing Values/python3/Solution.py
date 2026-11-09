from typing import List

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        tab = {}
        for i,v in nums1:
            tab[i] = v
        for i,v in nums2:
            if i in tab:
                tab[i] += v
            else:
                tab[i] = v
        result = []
        for i in sorted(tab.keys()):
            result.append([i, tab[i]])
        return result
