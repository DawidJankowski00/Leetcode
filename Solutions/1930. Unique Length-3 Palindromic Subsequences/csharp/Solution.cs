using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int CountPalindromicSubsequence(string s)
        {
            int result = 0;

            for (int i = 0; i < 26; i++) {
                char c = (char)('a' + i);
                int l = s.IndexOf(c);
                int r = s.LastIndexOf(c);
                if (l != r) {
                    HashSet<char> unique = new HashSet<char>();
                    for (int j = l + 1; j < r; j++)
                    {
                        unique.Add(s[j]);
                    }

                    result += unique.Count;
                }
            }

            return result;
        }
    }
}
