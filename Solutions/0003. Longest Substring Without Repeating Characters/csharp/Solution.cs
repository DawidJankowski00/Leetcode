using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int LengthOfLongestSubstring(string s)
        {
            int max_len = 0;
            Dictionary<char, int> lastIndex = new Dictionary<char, int>();
            int l = 0;
            for (int r = 0; r < s.Length; r++)
            {
                if (lastIndex.ContainsKey(s[r]))
                {
                    l = Math.Max(l, lastIndex[s[r]]);
                }
                max_len = Math.Max(max_len, r - l + 1);
                lastIndex[s[r]] = r + 1;
            }
            return max_len;
        }
    }
}
