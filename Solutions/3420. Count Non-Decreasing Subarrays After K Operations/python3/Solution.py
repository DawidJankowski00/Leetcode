from collections import deque
from typing import List

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        result = 0
        ops = 0
        dq = deque()
        
        r = n - 1
        for l in range(n - 1, -1, -1):
            curr_val = nums[l]
            count = 1
            
            while dq and dq[0][0] <= curr_val:
                prev_val, prev_count = dq.popleft()
                ops += (curr_val - prev_val) * prev_count
                count += prev_count
            
            dq.appendleft([curr_val, count])
            
            while ops > k:
                rightmost_ceil = dq[-1][0]
                ops -= (rightmost_ceil - nums[r])
                
                dq[-1][1] -= 1
                if dq[-1][1] == 0:
                    dq.pop()
                r -= 1
            
            result += (r - l + 1)
            
        return result