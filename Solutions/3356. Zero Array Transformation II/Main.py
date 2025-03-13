import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.minZeroArray([2,0,2],[[0,2,1],[0,2,1],[1,1,3]]))
    print(time.time() - start)

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n, m = len(nums), len(queries)
        diff_array = [0] * (n + 1)
        current_sum = query_index = 0

        for i, num in enumerate(nums):
            current_sum += diff_array[i]

            while query_index < m and current_sum < num:
                left, right, value = queries[query_index]
                query_index += 1

                if i < left:
                    diff_array[left] += value
                elif i <= right:
                    current_sum += value
                    
                diff_array[right + 1] -= value

            if current_sum < num:
                return -1
        return query_index
        
        

if __name__ == '__main__':
    sys.exit(main())