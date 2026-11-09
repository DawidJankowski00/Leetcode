using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int StrStr(string haystack, string needle)
        {
            int n= needle.Length;
            int m = haystack.Length;
            for (int i = 0; i < m - n + 1; i++)
            {
                if (haystack.Substring(i, n) == needle)
                {
                    return i;
                }
            }
            return -1;
        }
    }
}
