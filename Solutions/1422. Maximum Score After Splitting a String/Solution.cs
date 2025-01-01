using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int MaxScore(string s)
        {
            int n = s.Length;
            int l = 0;
            int r = 0;
            if (s[0] == '0') l = 1;
            for (int i = 1; i < n; i++) if (s[i] == '1') r++;
            int result = l+r;

            for (int i = 1; i < n; i++)
            {
                if (s[i] == '0') l++;
                else r--;

                if (result < r + l) result = r+l;
            }
            return result;
        }
    }
}
