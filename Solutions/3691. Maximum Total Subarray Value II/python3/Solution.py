import heapq

class SubarrayValueTable:
    def __init__(self, arr: list[int]):
        size = len(arr)
        levels = size.bit_length()
        
        self.min_table = [[0] * size for _ in range(levels)]
        self.max_table = [[0] * size for _ in range(levels)]

        for i in range(size):
            self.min_table[0][i] = self.max_table[0][i] = arr[i]

        for i in range(1, levels):
            span = 1 << i
            half_span = 1 << (i - 1)
            for j in range(size - span + 1):
                self.min_table[i][j] = min(self.min_table[i - 1][j], self.min_table[i - 1][j + half_span])
                self.max_table[i][j] = max(self.max_table[i - 1][j], self.max_table[i - 1][j + half_span])

    def get_value(self, start: int, end: int) -> int:
        k = (end - start + 1).bit_length() - 1
        span = 1 << k
        
        range_max = max(self.max_table[k][start], self.max_table[k][end - span + 1])
        range_min = min(self.min_table[k][start], self.min_table[k][end - span + 1])
        
        return range_max - range_min


class Solution:
    def maxTotalValue(self, nums: list[int], k: int) -> int:
        n = len(nums)
        value_finder = SubarrayValueTable(nums)

        max_heap = []
        for i in range(n):
            val = value_finder.get_value(i, n - 1)
            heapq.heappush(max_heap, (-val, i, n - 1))

        total_max_value = 0
        
        for _ in range(k):
            if not max_heap:
                break
                
            neg_val, left, right = heapq.heappop(max_heap)
            current_value = -neg_val
            
            if current_value == 0:
                break
                
            total_max_value += current_value

            if left < right:
                next_val = value_finder.get_value(left, right - 1)
                heapq.heappush(max_heap, (-next_val, left, right - 1))

        return total_max_value