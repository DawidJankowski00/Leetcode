import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.closestPrimes(10, 19))
    print(time.time() - start)

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        result = [-1,-1]
        is_prime = [True] * (right + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(right ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i*i, right + 1, i):
                    is_prime[j] = False
        primes = [i for i in range(left, right+1) if is_prime[i]]
        if len(primes) < 2:
            return result
        dif = primes[1] - primes[0]
        result = [primes[0], primes[1]]
        for i in range(2, len(primes)):
            tmp = primes[i] - primes[i-1]
            if tmp < dif:
                dif = tmp
                result = [primes[i-1], primes[i]]
        return result

if __name__ == '__main__':
    sys.exit(main())