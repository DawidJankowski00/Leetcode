using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int[] VowelStrings(string[] words, int[][] queries)
        {
            int[] result = new int[queries.Length];
            var vowels = new HashSet<char>(new[] { 'a', 'e', 'i', 'o', 'u' });
            int[] pre_sum = new int[words.Length + 1];
            pre_sum[0] = 0;
            for (int i = 0; i < words.Length; i++)
            {
                if (vowels.Contains(words[i][0]) && vowels.Contains(words[i][^1]))
                {
                    pre_sum[i + 1] = pre_sum[i] + 1;
                }
                else
                {
                    pre_sum[i + 1] = pre_sum[i];
                }
            }
            for (int i = 0; i < queries.Length; i++) result[i] = pre_sum[queries[i][1] + 1] - pre_sum[queries[i][0]];
             return result;

        }
    }
}
