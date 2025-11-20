from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def backTrack(current_k, current_n, path, start):
            if current_k == 0:
                if current_n == 0:
                    result.append(path[:])
                return
            
            if current_n < 0:
                return

            for i in range(start, 10):
                path.append(i)
                backTrack(current_k - 1, current_n - i, path, i + 1)
                path.pop()

        backTrack(k, n, [], 1)
        return result
