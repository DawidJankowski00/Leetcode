using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution 
    {
        public int[] FindXSum(int[] nums, int k, int x) 
        {
            int n = nums.Length;
            List<int> result = new List<int>();

            for (int i = 0; i <= n - k; i++)
            {
                var freq = nums.Skip(i).Take(k)
                            .GroupBy(v => v)
                            .ToDictionary(g => g.Key, g => g.Count());

                var topXItems = freq.OrderByDescending(pair => pair.Value)
                                    .ThenByDescending(pair => pair.Key)
                                    .Take(x);
                
                long tmp = 0; 
                
                foreach (var pair in topXItems)
                {
                    int value = pair.Key;
                    int frequency = pair.Value;
                    
                    tmp += (long)value * frequency;
                }

                result.Add((int)tmp);
            }

            return result.ToArray();
        }
    }
}
