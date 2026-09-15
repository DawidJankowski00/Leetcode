using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public int MaxPalindromes(string s, int k) {
            int n = s.Length;
            int[] dp = new int[n + 1];

            bool IsPalindrome(int left, int right) {
                while (left < right) {
                    if (s[left] != s[right]) return false;
                    left++;
                    right--;
                }
                return true;
            }

            for (int i = 1; i <= n; i++) {
                dp[i] = dp[i - 1];
                if (i >= k && IsPalindrome(i - k, i - 1)) {
                    dp[i] = Math.Max(dp[i], dp[i - k] + 1);
                }

                if (i >= k + 1 && IsPalindrome(i - k - 1, i - 1)) {
                    dp[i] = Math.Max(dp[i], dp[i - k - 1] + 1);
                }
            }
            return dp[n];
        }
    }
}
