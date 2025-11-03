using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public IList<IList<int>> FindDifference(int[] nums1, int[] nums2) {
            HashSet<int> n1 = new HashSet<int>(nums1);
            HashSet<int> n2 = new HashSet<int>(nums2);

            HashSet<int> r1 = new HashSet<int>(n1);
            HashSet<int> r2 = new HashSet<int>(n2);
            r1.ExceptWith(n2);
            r2.ExceptWith(n1);

            return new List<IList<int>> { r1.ToList(), r2.ToList() };
        }
    }
}
