using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public long MaxScore(int[] nums1, int[] nums2, int k) {
            long result = 0;
            var paired = nums1.Zip(nums2, (a, b) => new Tuple<int, int>(a, b))
                              .OrderByDescending(x => x.Item2)
                              .ToList();
            var heap = new PriorityQueue<int, int>();
            long currentSum = 0;
            foreach (var pair in paired)
            {
                currentSum += pair.Item1;
                heap.Enqueue(pair.Item1, pair.Item1);
                if (heap.Count == k)
                {
                    result = Math.Max(result, currentSum * pair.Item2);
                    currentSum -= heap.Dequeue();
                }
            }
            return result;
        }
    }
}
