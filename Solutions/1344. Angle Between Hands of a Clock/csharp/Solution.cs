using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public double AngleClock(int hour, int minutes) {
            double a  = 6 * minutes;
            double b = 30 * hour + 0.5 * minutes;
            double diff = Math.Abs(a - b);
            return Math.Min(diff, 360 - diff);
        }
    }
}
