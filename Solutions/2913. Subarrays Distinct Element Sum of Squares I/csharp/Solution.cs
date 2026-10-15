using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public int SumCounts(IList<int> nums) {
            int result = 0;
            int n = nums.Count;
            for (int i = 0; i < n; i++) {
                HashSet<int> distinctElements = new HashSet<int>();
                for (int j = i; j < n; j++) {
                    distinctElements.Add(nums[j]);
                    int tmp = distinctElements.Count;
                    result += tmp * tmp;
                }
            }
            return result;
        }
    }
}
