using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    using System;
using System.Collections.Generic;
using System.Linq;

    public class Solution 
    {
        public long TotalCost(int[] costs, int k, int candidates) 
        {
            int n = costs.Length;
            
            int i = 0;
            int j = n - 1;
            
            var pq1 = new PriorityQueue<int, int>();
            var pq2 = new PriorityQueue<int, int>();

            long ans = 0;

            while (k > 0)
            {
                while (pq1.Count < candidates && i <= j)
                {
                    pq1.Enqueue(costs[i], costs[i]);
                    i++;
                }

                while (pq2.Count < candidates && i <= j)
                {
                    pq2.Enqueue(costs[j], costs[j]);
                    j--;
                }

                long t1 = pq1.Count > 0 ? pq1.Peek() : long.MaxValue;
                long t2 = pq2.Count > 0 ? pq2.Peek() : long.MaxValue;

                if (t1 <= t2)
                {
                    ans += t1;
                    pq1.Dequeue();
                }
                else
                {
                    ans += t2;
                    pq2.Dequeue();
                }

                k--;
            }

            return ans;
        }
    }
}
