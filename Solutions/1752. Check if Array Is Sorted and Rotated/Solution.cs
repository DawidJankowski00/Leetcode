using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution 
    {
        public bool Check(int[] nums) 
        {
            int n = nums.Length;
            int count = 0;
            for (int i = 0; i < n; i++)
            {
                if (nums[i] > nums[(i + 1) % n]) 
                {  
                    count++; 
                }
            }
            return count <= 1;
        }
    }
}
