import random
from typing import List

class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n

        M1 = 10**9 + 7
        M2 = 10**9 + 9
        B1 = random.randint(100_003, 1_000_000)
        B2 = random.randint(100_003, 1_000_000)

        def has_unique(length: int) -> bool:
            h1 = 0
            h2 = 0
            for i in range(length):
                h1 = (h1 * B1 + nums[i]) % M1
                h2 = (h2 * B2 + nums[i]) % M2

            seen = {(h1 << 32) | h2}
            dup = set()

            p1 = pow(B1, length - 1, M1)
            p2 = pow(B2, length - 1, M2)

            for i in range(length, n):
                out_val = nums[i - length]
                in_val = nums[i]

                h1 = ((h1 - out_val * p1) * B1 + in_val) % M1
                h2 = ((h2 - out_val * p2) * B2 + in_val) % M2

                h = (h1 << 32) | h2
                if h in seen:
                    dup.add(h)
                else:
                    seen.add(h)

            return len(seen) > len(dup)

        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) // 2
            if has_unique(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo