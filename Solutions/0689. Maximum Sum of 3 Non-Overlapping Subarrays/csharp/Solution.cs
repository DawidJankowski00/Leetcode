using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int[] MaxSumOfThreeSubarrays(int[] nums, int k)
        {
            int sub1 = 0, sub2 = 0, sub3 = 0;
            for (int i = 0; i < k; i++)
            {
                sub1 += nums[i];
                sub2 += nums[i + k];
                sub3 += nums[i + 2 * k];
            }

            int[] sub1Index = { 0 };
            int[] sub2Index = { 0, k };
            int[] sub3Index = { 0, k, 2 * k };

            int sum1 = sub1, sum2 = sub1 + sub2, sum3 = sub1 + sub2 + sub3;

            for (int i = 1; i <= nums.Length - 3 * k; i++)
            {
                sub1 += nums[i - 1 + k] - nums[i - 1];
                sub2 += nums[i - 1 + 2 * k] - nums[i - 1 + k];
                sub3 += nums[i - 1 + 3 * k] - nums[i - 1 + 2 * k];

                if (sub1 > sum1)
                {
                    sum1 = sub1;
                    sub1Index = new[] { i };
                }
                if (sum1 + sub2 > sum2)
                {
                    sum2 = sum1 + sub2;
                    sub2Index = new[] { sub1Index[0], i + k };
                }
                if (sum2 + sub3 > sum3)
                {
                    sum3 = sum2 + sub3;
                    sub3Index = new[] { sub2Index[0], sub2Index[1], i + 2 * k };
                }
            }

            return sub3Index;
        }
    }


}
