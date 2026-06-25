using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution 
    {
        private int[] BIT;

        private void Update(int idx, int val) 
        {
            while (idx < BIT.Length) 
            {
                BIT[idx] += val;
                idx += idx & (-idx);
            }
        }

        private int Query(int idx) 
        {
            int s = 0;
            while (idx > 0) 
            {
                s += BIT[idx];
                idx -= idx & (-idx);
            }
            return s;
        }

        public int CountMajoritySubarrays(int[] nums, int target) 
        {
            int result = 0;
            int n = nums.Length;
            
            int[] transformed = new int[n];
            for (int i = 0; i < n; i++) 
            {
                transformed[i] = (nums[i] == target) ? 1 : -1;
            }

            BIT = new int[2 * n + 2];
            
            int curr_p_sum = 0;
            Update(curr_p_sum + n + 1, 1);
            
            foreach (int val in transformed) 
            {
                curr_p_sum += val;
                result += Query(curr_p_sum + n);
                Update(curr_p_sum + n + 1, 1);
            }
            
            return result;
        }
    }
}
