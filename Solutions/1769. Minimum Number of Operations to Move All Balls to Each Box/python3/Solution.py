from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        result = [0] * n
        ball = 0
        curr = 0
        for i in range(0, n):
            result[i] += curr
            if boxes[i] == '1':
                ball += 1
            curr += ball
        ball = 0
        curr = 0
        for i in range(n-1, -1, -1):
            result[i] += curr
            if boxes[i] == '1':
                ball += 1
            curr += ball
        return result
