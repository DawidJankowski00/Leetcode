using System;
using System.Collections.Generic;
using System.Linq;
using System.Numerics;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public string GcdOfStrings(string str1, string str2)
        {
            if (str1 + str2 != str2 + str1) return "";
            return str1.Substring(0, Gcd(str1.Length, str2.Length));
        }
        public int Gcd(int s1, int s2)
        {
            while (s2 != 0)
            {
                int tmp = s2;
                s2 = s1 % s2;
                s1 = tmp;
            }
            return s1;
        }
    }
}
