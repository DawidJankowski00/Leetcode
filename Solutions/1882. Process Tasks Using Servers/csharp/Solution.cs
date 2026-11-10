using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution 
    {
        public int[] AssignTasks(int[] servers, int[] tasks) 
        {
            var available = new PriorityQueue<(int Weight, int Index), (int Weight, int Index)>();
            for (int i = 0; i < servers.Length; i++)
            {
                var server = (servers[i], i);
                available.Enqueue(server, server);
            }

            var occupied = new PriorityQueue<(int Weight, int Index), (long ReleaseTime, int Weight, int Index)>();
            int[] res = new int[tasks.Length];

            for (int arrival = 0; arrival < tasks.Length; arrival++)
            {
                long duration = tasks[arrival];

                while (occupied.TryPeek(out _, out var busyPri) && busyPri.ReleaseTime <= arrival)
                {
                    var s = occupied.Dequeue();
                    available.Enqueue(s, s);
                }

                int sWeight, sIdx;
                long releaseTime;

                if (available.Count > 0)
                {
                    (sWeight, sIdx) = available.Dequeue();
                    releaseTime = arrival + duration;
                }
                else
                {
                    occupied.TryPeek(out _, out var earliest);
                    (sWeight, sIdx) = occupied.Dequeue();
                    releaseTime = earliest.ReleaseTime + duration;
                }

                occupied.Enqueue((sWeight, sIdx), (releaseTime, sWeight, sIdx));
                res[arrival] = sIdx;
            }

            return res;
        }
    }
}
