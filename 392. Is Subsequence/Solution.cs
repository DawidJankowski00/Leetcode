using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public bool IsSubsequence(string s, string t)
        {
            int j = 0;
            int i = 0;
            while (i < s.Length && j < t.Length)
            {
                if (s[i] == t[j]) i++;
                j++;
            }
            return i == s.Length;
        }
    }
}
