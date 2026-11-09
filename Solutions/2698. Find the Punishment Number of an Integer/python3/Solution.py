from typing import List

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
