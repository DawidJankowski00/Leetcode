from collections import defaultdict
from typing import List

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        result = -1
        map = defaultdict(int)
        for i, num in enumerate(nums):
            tmp = num
            Digits_sum = 0
            while tmp >= 10:
                Digits_sum += tmp % 10
                tmp //= 10
            Digits_sum += tmp
            if Digits_sum in map:
                tmp = map[Digits_sum]
                if result < tmp + num:
                    result = tmp + num
                if tmp < num:
                    map[Digits_sum] = num
            else:
                map[Digits_sum] = num
        return result
