class Solution:
    patterns = []
    for i in range(1000):
        r = i % 10
        m = (i // 10) % 10
        l = (i // 100) % 10
        if (m > max(l, r)) | (m < min(l, r)):
            patterns.append(i)

    def totalWaviness(self, num1: int, num2: int) -> int:
        return self.waveCount(num2) - self.waveCount(num1 -1)
    
    def waveCount(self, num: int):
        if num < 100:
            return 0
        return sum(self.countWays(num, p) for p in self.patterns)

    def countWays(self, num: int, pattern: int):
        s = str(num)
        n = len(s)
        result = 0
        t = pattern < 100
        for i in range(n-2):
            l = int(s[:i] or 0)
            m = int(s[i:i+3])
            r = int(s[i+3:] or 0)
            mult = 10 ** (n - i - 3)
            tmp = 0

            if m > pattern:
                tmp = l - t + 1
            elif m == pattern:
                tmp = max(0, l-t)
                result += r + 1
            else:
                tmp = max(0, l - t)
            result += mult * tmp
                

        return result

