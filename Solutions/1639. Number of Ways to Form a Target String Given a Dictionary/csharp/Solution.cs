using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int NumWays(string[] words, string target)
        {
            int n = words[0].Length;
            int m = target.Length;
            Dictionary<char, int>[] freq = new Dictionary<char, int>[n];
            for (int i = 0; i < n; i++)
            {
                freq[i] = new Dictionary<char, int>();
                for (int j = 0; j < words.Length; j++)
                {
                    if (freq[i].ContainsKey(words[j][i]))
                    {
                        freq[i][words[j][i]]++;
                    }
                    else
                    {
                        freq[i][words[j][i]] = 1;
                    }
                }
            }
            int mod = 1_000_000_007;
            var dp = new int[m+1];
            dp[0] = 1;
            for (int i = 0; i < n; i++)
            {
                for (int j = m - 1; j > -1; j--)
                {
                    if (freq[i].ContainsKey(target[j]))
                    {
                        dp[j + 1] = (dp[j + 1] + (int)((long)dp[j] * freq[i][target[j]] % mod)) % mod;

                    }
                    
                }
            }
            return dp[m];

        }
    }
}
