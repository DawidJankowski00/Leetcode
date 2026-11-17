class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        divisors = [[] for _ in range(n + 1)]
        for length in range(2, n + 1):
            for d in range(1, length):
                if length % d == 0:
                    divisors[length].append(d)

        cost = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1
                min_changes = length
                for d in divisors[length]:
                    changes = 0
                    for r in range(d):
                        left = i + r
                        right = j - d + 1 + r
                        while left < right:
                            if s[left] != s[right]:
                                changes += 1
                            left += d
                            right -= d
                    if changes < min_changes:
                        min_changes = changes
                cost[i][j] = min_changes

        inf = n + 1
        dp = [inf] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = cost[0][i - 1]

        for p in range(2, k + 1):
            next_dp = [inf] * (n + 1)
            for i in range(2 * p, n + 1):
                best = inf
                for prev in range(2 * (p - 1), i - 1):
                    cand = dp[prev] + cost[prev][i - 1]
                    if cand < best:
                        best = cand
                next_dp[i] = best
            dp = next_dp

        return dp[n]

