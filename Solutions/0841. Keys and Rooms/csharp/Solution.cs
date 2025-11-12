using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public bool CanVisitAllRooms(IList<IList<int>> rooms) {
            HashSet<int> visited = new HashSet<int>();
            HashSet<int> to_visit = new HashSet<int>();
            to_visit.Add(0);
            while (to_visit.Count > 0)
            {
                int p = to_visit.First();
                visited.Add(p);
                foreach (int v in rooms[p]) if (!visited.Contains(v) && !to_visit.Contains(v)) to_visit.Add(v);
                to_visit.Remove(p);
            }

            return rooms.Count == visited.Count;
        }
    }
}
