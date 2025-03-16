using System;
using System.Collections.Generic;
using System.Diagnostics.Metrics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public long RepairCars(int[] ranks, int cars)
        {
            long l = 1;
            long r = (long)ranks.Min() *cars * cars;

            bool helper(long time)
            {
                long counter = 0;
                foreach (int r in ranks) 
                {
                    counter += (long)Math.Sqrt(time / r);
                    
                    if (counter >= cars)
                        return true;

                }
                return false;
            }

            while (l < r)
            {
                long mid = (l + r) / 2;
                if (helper(mid))
                    r = mid;
                else
                    l = mid + 1;
            }
            return l;
        }
    }
}
