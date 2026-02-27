using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public int NumSteps(string s) {
            int result = 0;
            int carry = 0;
            int n = s.Length;
            for (int i = n - 1; i > 0; i--)
            {
                if ((s[i] - '0') + carry == 1)
                {
                    result += 2;
                    carry = 1;
                }
                else
                {
                    result += 1;
                }
            }
            return result + carry;
        }
    }
}
