using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public string LongestCommonPrefix(string[] strs)
        {
            string result = "";
            Array.Sort(strs);
            string f = strs[0];
            string l = strs.Last();
            for (int i = 0; i < Math.Min(f.Length, l.Length); i++)
            {
                if (f[i] != l[i])
                {
                    return result;
                }
                result += strs[i];
            }
            return result;
        }
    }
}
