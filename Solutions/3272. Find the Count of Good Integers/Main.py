import sys
import time
from typing import Counter, List
from itertools import product
from collections import Counter
from math import factorial
from functools import reduce
from operator import mul
def main():
    sol = Solution()
    start = time.time()
    print(sol.countGoodIntegers(3, 5))
    print(time.time() - start)

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:

        if n == 1:
            return 9 // k
        seen_pal_forms, good_count = set(), 0
        digit_combos = product(*[digits[1:]] + [digits] * ((n - 1) // 2))  # <-- 1
        
        for half_digits in digit_combos:
            mirror_part = half_digits[::-1][n % 2:]                        # <-- 2
            full_palindrome = ''.join(((*half_digits, *mirror_part)))
            if int(full_palindrome) % k == 0:                              # <-- 3
                seen_pal_forms.add(''.join(sorted(full_palindrome)))

        for pal_form in seen_pal_forms:
            freq = Counter(pal_form)                                       # <-- 4
            denom = reduce(mul, map(factorial, freq.values()))
            good_count += factorial(n) * (n - freq['0']) // (denom * n)

        return good_count


if __name__ == '__main__':
    sys.exit(main())