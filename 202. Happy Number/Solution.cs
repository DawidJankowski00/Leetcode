using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public bool IsHappy(int n)
        {
            Dictionary<int, int> dic = new Dictionary<int, int>();
            while (!dic.ContainsKey(n))
            {
                if (n == 1)
                {
                    return true;
                }
                dic.Add(n, 0);
                int tmp = 0;
                while (n != 0)
                {
                    tmp += (n%10) * (n%10);
                    n = n / 10;
                }
                n = tmp;
            
            }
            return false;
        }
    }
}
