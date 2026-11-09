using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int MinimumLength(string s)
        {
            int[] freq = new int[26];
            int result = 0;
            for (int i = 0; i < s.Length; i++)
            {
                freq[s[i]-'a']++;
            }
            for (int i = 0; i < 26; i++)
            {
                if (freq[i] % 2 == 1)
                    result++;
                else if (freq[i] != 0)
                    result += 2;
            }
            return result;
        }
    }
}
