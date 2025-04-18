using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public string CountAndSay(int n)
        {
            if (n == 1) return "1";

            string tmp = CountAndSay(n - 1);
            string result = "";
            char last = tmp[0];
            int ct = 1;

            for (int i = 1; i < tmp.Length; i++)
            {
                if (tmp[i] == last) ct++;

                else
                {
                    result += ct;
                    result += last;
                    ct = 1;
                    last = tmp[i];
                }
            }
            return result + ct + last;
        }
    }
}
