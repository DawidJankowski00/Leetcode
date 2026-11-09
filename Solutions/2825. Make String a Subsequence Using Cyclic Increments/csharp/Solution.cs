using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public bool CanMakeSubsequence(string str1, string str2)
        {
            int j = 0;
            int str2len = str2.Length;
            foreach (char c in str1)
            {
                if (j < str2len && (str2[j] - c + 26) % 26 < 2)
                {
                    j++;
                }
            }
            return j == str2len;
        }
    }
}
