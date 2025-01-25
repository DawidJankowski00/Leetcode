using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int[] LexicographicallySmallestArray(int[] nums, int limit)
        {
            int n = nums.Length;
            var num = new List<(int Value, int Index)>();

            for (int i = 0; i < n; i++)
            {
                num.Add((nums[i], i));
            }
            num.Sort();

            var groups = new List<List<(int Value, int Index)>> { new List<(int, int)> { num[0] } };
            for (int i = 1; i < n; i++)
            {
                if (num[i].Value - num[i - 1].Value <= limit)
                {
                    groups[^1].Add(num[i]);
                }
                else
                {
                    groups.Add(new List<(int, int)> { num[i] });
                }
            }

            foreach (var group in groups)
            {
                var indices = group.Select(x => x.Index).ToList();
                indices.Sort();

                for (int i = 0; i < indices.Count; i++)
                {
                    nums[indices[i]] = group[i].Value;
                }
            }

            return nums;
        }
    }
}
