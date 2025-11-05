using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public string DecodeString(string s) {
            int k = 0;
            int n = s.Length;
            string CreatePart()
            {
                StringBuilder result = new StringBuilder();
                while (k < n && s[k] != ']')
                {
                    if (char.IsDigit(s[k]))
                    {
                        int dig_start = k;
                        while (s[k] != '[') k++;
                        string tmp = s.Substring(dig_start, k - dig_start);
                        k++;
                        string tmp2 = CreatePart();
                        for (int i = 0; i < int.Parse(tmp); i++) result.Append(tmp2);
                    }
                    else
                    {
                        result.Append(s[k]);
                        k++;
                    }
                }
                k++;
                return result.ToString();
            }
            return CreatePart();
        }
    }
}
