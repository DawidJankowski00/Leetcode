using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int MinOperations(int[] nums, int k)
        {

            int result = 0;
            var minHeap = new PriorityQueue<long, long>();

            foreach (int num in nums)
            {
                if (num < k)
                    minHeap.Enqueue(num, num);
            }

            while (minHeap.Count > 1)
            {
                result++;
                long a = minHeap.Dequeue();
                long b = minHeap.Dequeue();
                long val = a * 2 + b;
                if (val < k)
                    minHeap.Enqueue(val, val);
            }
            return result + minHeap.Count;
        }
    }
}
