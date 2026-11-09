using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
{
    public long ContinuousSubarrays(int[] nums)
    {
        int l = 0, r = 0, j = 0;
        long result = 0;

        for (int i = 0; i < nums.Length; i++)
        {
            if (i == 0)
            {
                result += 1;
                l = nums[i] - 2;
                r = nums[i] + 2;
            }
            else if (l <= nums[i] && nums[i] <= r)
            {
                l = Math.Max(l, nums[i] - 2);
                r = Math.Min(r, nums[i] + 2);
                result += (i - j + 1);
            }
            else
            {
                j = i - 1;
                l = nums[i] - 2;
                r = nums[i] + 2;

                while (j >= 0 && nums[j] >= nums[i] - 2 && nums[j] <= nums[i] + 2)
                {
                    l = Math.Max(l, nums[j] - 2);
                    r = Math.Min(r, nums[j] + 2);
                    j--;
                }

                j++;
                result += (i - j + 1);
            }
        }

        return result;
        }
    }
}
