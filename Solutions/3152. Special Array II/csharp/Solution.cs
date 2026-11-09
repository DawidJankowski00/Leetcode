using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public bool[] IsArraySpecial(int[] nums, int[][] queries)
        {
            bool[] result = new bool[queries.Length];
            int[] prefix = new int[nums.Length];
            for (int i = 1; i < nums.Length; i++)
            {
                prefix[i] = prefix[i - 1];
                if ((nums[i - 1] + nums[i]) % 2 == 0)
                {
                    prefix[i]++;
                }
            }
            for (int i = 0; i < queries.Length; i++)
            {
                result[i] = (prefix[queries[i][1]] - prefix[queries[i][0]] == 0);
            }
            return result;
        }
    }
}
