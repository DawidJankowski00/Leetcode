import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.minOperations("110"))
    print(time.time() - start)

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
            
        

if __name__ == '__main__':
    sys.exit(main())