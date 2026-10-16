from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        bit1 = [0] * (n + 2)
        bit2 = [0] * (n + 2)
        
        def add(bit: List[int], idx: int, val: int):
            while idx <= n + 1:
                bit[idx] += val
                idx += idx & (-idx)
                
        def query(bit: List[int], idx: int) -> int:
            s = 0
            while idx > 0:
                s += bit[idx]
                idx -= idx & (-idx)
            return s

        def range_add(l: int, r: int, val: int):
            add(bit1, l, val)
            add(bit1, r + 1, -val)
            add(bit2, l, val * (l - 1))
            add(bit2, r + 1, -val * r)
            
        def prefix_sum(idx: int) -> int:
            return query(bit1, idx) * idx - query(bit2, idx)
            
        def range_sum(l: int, r: int) -> int:
            return prefix_sum(r) - prefix_sum(l - 1)

        last_pos = {}
        total_ans = 0
        cur_sq_sum = 0
        
        for i, x in enumerate(nums):
            p = last_pos.get(x, -1)
            l = p + 2
            r = i + 1
            
            s = range_sum(l, r)
            
            cur_sq_sum = (cur_sq_sum + 2 * s + (r - l + 1)) % MOD
            total_ans = (total_ans + cur_sq_sum) % MOD
            
            range_add(l, r, 1)
            last_pos[x] = i
            
        return total_ans