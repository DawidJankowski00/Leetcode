class Solution:
    MAX = 100001
    dp = [0] * MAX
    pref = [0] * MAX

    for i in range(100, MAX):
        r = i % 10
        m = (i // 10) % 10
        l = (i // 100) % 10

        tmp = (m > r and m > l) or (m < r and m < l)
        dp[i] = dp[i // 10] + int(tmp)
        pref[i] = pref[i-1] + dp[i]

        

    def totalWaviness(self, num1: int, num2: int) -> int:
        return self.pref[num2] - self.pref[num1-1]
