class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1= len(text1)
        n2 = len(text2)
        dp = [[0] * (n2 + 1) for _ in range(n1)]

        for i, v1 in enumerate(text1):
            for j, v2 in enumerate(text2):
                if v1 == v2:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[n1-1][n2-1]