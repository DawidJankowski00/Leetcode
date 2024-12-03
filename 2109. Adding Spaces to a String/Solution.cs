using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public string AddSpaces(string s, int[] spaces)
        {
            char[] result = new char[s.Length + spaces.Length];
            int j = 0;
            int m = spaces.Length;
            for (int i = 0; i < s.Length; i++)
            {
                if (m > j)
                {
                    if (i == spaces[j])
                    {
                        result[i + j] = ' ';
                        j++;
                    }
                }
                result[i + j] = s[i];
            }
            return new string(result);
        }
    }
}
