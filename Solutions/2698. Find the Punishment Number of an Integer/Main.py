import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.punishmentNumber(1000))
    print(time.time() - start)

class Solution:
    def punishmentNumber(self, n: int) -> int:
        def is_partition_valid(number, target):
            if number == target:
                return True
            if number == 0:
                return target == 0
            for divisor in (10, 100, 1000):
                if is_partition_valid(number // divisor, target - number % divisor):
                    return True
            return False
        
        return sum(square for num in range(1, n + 1) if is_partition_valid(square := num * num, num))
        
        

if __name__ == '__main__':
    sys.exit(main())