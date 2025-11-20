class Solution:
    def tribonacci(self, n: int) -> int:
        dp = {0 : 0, 1 : 1, 2 : 1}
        l = 2
        def helper(k):
            if k in dp:
                return dp[k]
            else:
                tmp = helper(k-1) + helper(k-2) + helper(k-3)
                dp[k] = tmp
                return helper(k-1) + helper(k-2) + helper(k-3)
        
        return helper(n)