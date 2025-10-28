using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public void MoveZeroes(int[] nums) {
            int n = nums.Length;
            int l = 0;
            for (int r = 0; r < n; r++)
            {
                if (nums[r] != 0)
                {
                    int tmp = nums[l];
                    nums[l] = nums[r];
                    nums[r] = tmp;
                    l++;
                }
            }
        }
    }
}
