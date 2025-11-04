from collections import Counter
from typing import List


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        result = []

        for i in range(n-k+1):
            window = nums[i:i+k]
            freq = Counter(window)
            sort = sorted(freq.items(), key=lambda a: (-a[1], -a[0]))
            top_x = [num for num, _ in sort[:x]]
            tmp = 0
            for v in top_x:
                tmp += freq[v] * v
            result.append(tmp)
        return result
            