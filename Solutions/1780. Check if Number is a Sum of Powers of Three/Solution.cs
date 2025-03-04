using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public bool CheckPowersOfThree(int n)
        {
            while (n != 0)
            {
                if (n % 3 == 2)
                {
                    return false;
                }
                n = n / 3;
            }
            return true;
        }
    }
}
