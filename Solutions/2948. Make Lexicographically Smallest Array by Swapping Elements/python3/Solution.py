from collections import defaultdict
from typing import List

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        num = []
        n = len(nums)
        for i in range(n):
            num.append((nums[i],i))
        num.sort()
        grups = [[num[0]]]
        for i in range(1, n):
            if num[i][0] - num[i-1][0] <= limit:
                grups[-1].append(num[i])
            else:
                grups.append([num[i]])
        for t in grups:
            ind = []
            for _, y in t:
                ind.append(y)
            ind.sort()
            for i in range(len(ind)):
                nums[ind[i]] = t[i][0]
        return nums
