using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public bool DivideArray(int[] nums)
        {
            var tab = new Dictionary<int, int>();
            foreach (var item in nums)
            {
                if (tab.ContainsKey(item))
                {
                    tab[item] += 1;
                }
                else
                {
                    tab[item] = 1;
                }
            }
            foreach (var v in tab.Values)
            {
                if (v % 2 == 1)
                {
                    return false;
                }
            }
            return true;
        }
    }
}
