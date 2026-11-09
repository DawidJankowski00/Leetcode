from collections import defaultdict
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = defaultdict(int)
        for i, v in enumerate(nums):
            if target - v in dic:
                return [dic[target-v], i]
            dic[v] = i
