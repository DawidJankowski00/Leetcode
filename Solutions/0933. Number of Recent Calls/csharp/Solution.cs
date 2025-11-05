using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class RecentCounter {
        List<int> records;
        int k;
        public RecentCounter() {
            records = new List<int>();
            k = 0;
        }
        
        public int Ping(int t) {
            records.Add(t);
            while (records[k] < t - 3000) k++;
            return records.Count - k;
        }
    }
}
