using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int MaxCount(int[] banned, int n, int maxSum)
        {
            Dictionary<int, bool> dic = new Dictionary<int, bool>();
            foreach (var num in banned)
            {
                dic[num] = true;
            }
            int csum = 0;
            int nums = 0;
            for (int i = 1; i <= n; i++)
            {
                if (dic.Keys.Contains(i))
                {
                    continue;
                }
                csum += i;
                if (csum > maxSum)
                {
                    break;
                }
                nums++;
            }
            return nums;
        }
    }
}
