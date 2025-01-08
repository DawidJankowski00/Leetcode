using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int CountPrefixSuffixPairs(string[] words)
        {
            int m = words.Length;
            int result = 0;
            for (int i = 0; i < m; i++)
            {
                for (int j = i + 1; j < m; j++)
                {
                    if (isPrefixAndSuffix(words[i], words[j]))
                        result++;
                }
            }
            return result;
        }
        public bool isPrefixAndSuffix(string str1, string str2)
        {
            return str2.StartsWith(str1) && str2.EndsWith(str1);
        }
    }
}
