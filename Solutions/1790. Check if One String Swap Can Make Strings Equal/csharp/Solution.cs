using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public bool AreAlmostEqual(string s1, string s2)
        {
            int n = s1.Length;
            char c1 = new char();
            char c2 = new char();
            int diff_chars_count = 0;
            for (int i = 0; i < n; i++)
            {
                if (s1[i] != s2[i] && diff_chars_count == 0)
                {
                    c1 = s1[i];
                    c2 = s2[i];
                    diff_chars_count++;
                }
                else if (s1[i] != s2[i])
                {
                    diff_chars_count++;
                    if (diff_chars_count > 2) return false;
                    if (s1[i] != c2 || s2[i] != c1) return false;
                }
            }
            if (diff_chars_count == 1) return false;
            return true;
        }
    }
}
