class Solution:
    def guessNumber(self, n: int) -> int:
        def guess(a):
            return -1
        start = 1
        while True:
            mid = start + (n-start) // 2
            res = guess(mid)
            if res == 0:
                return mid
            elif res ==  -1:
                n = mid - 1
            else:
                start = mid + 1
    