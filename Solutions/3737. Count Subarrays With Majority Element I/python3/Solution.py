from typing import Counter


from collections import defaultdict

class Solution:
    def countMajoritySubarrays(self, nums: list[int], target: int) -> int:
        result = 0
        n = len(nums)
        transformed = [1 if x == target else -1 for x in nums]
        BIT = [0] * (2 * n + 2)
        
        def update(idx, val):
            while idx < len(BIT):
                BIT[idx] += val
                idx += idx & (-idx)
                
        def query(idx):
            s = 0
            while idx > 0:
                s += BIT[idx]
                idx -= idx & (-idx)
            return s
        
        curr_p_sum = 0
        update(curr_p_sum + n + 1, 1)
        
        for val in transformed:
            curr_p_sum += val
            result += query(curr_p_sum + n)
            update(curr_p_sum + n + 1, 1)
            
        return result