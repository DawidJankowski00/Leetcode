from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        result = 1
        points.sort(key=lambda x: x[1])
        stop = points[0][1]
        for v in points[1:]:
            if v[0] > stop:
                stop = v[1]
                result += 1
        return result
