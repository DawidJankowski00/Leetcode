using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    using System;
    using System.Collections.Generic;

    public class Solution
    {
        public int[] GetFinalState(int[] nums, int k, int multiplier)
        {
            var heap = new PriorityQueue<int, (int Value, int Index)>(Comparer<(int Value, int Index)>
            .Create((a, b) => a.Value == b.Value ? a.Index.CompareTo(b.Index) : a.Value.CompareTo(b.Value)));

            for (int i = 0; i < nums.Length; i++)
            {
                heap.Enqueue(i, (nums[i], i));
            }

            for (int j = 0; j < k; j++)
            {
                var elem = heap.Dequeue();

                nums[elem] *= multiplier;

                heap.Enqueue(elem, (nums[elem], elem));
            }

            return nums;
        }
    }

}
