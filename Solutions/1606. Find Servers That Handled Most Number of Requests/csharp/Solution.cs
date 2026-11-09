using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{

    public class Solution {
        public IList<int> BusiestServers(int k, int[] arrival, int[] load) {
            var availablePool = new PriorityQueue<long, long>();
            for (int srv = 0; srv < k; srv++) {
                availablePool.Enqueue(srv, srv);
            }

            var runningTasks = new PriorityQueue<int, long>();
            int[] handledCounts = new int[k];

            for (int reqIdx = 0; reqIdx < arrival.Length; reqIdx++) {
                long startTime = arrival[reqIdx];
                long taskDuration = load[reqIdx];

                while (runningTasks.Count > 0 && runningTasks.TryPeek(out int serverId, out long finish) && finish <= startTime) {
                    runningTasks.Dequeue();
                    long virtualIndex = reqIdx + (serverId - reqIdx % k + k) % k;
                    availablePool.Enqueue(virtualIndex, virtualIndex);
                }

                if (availablePool.Count == 0) {
                    continue;
                }

                int chosenServer = (int)(availablePool.Dequeue() % k);
                handledCounts[chosenServer]++;

                long finishTime = startTime + taskDuration;
                runningTasks.Enqueue(chosenServer, finishTime);
            }

            int peakTraffic = handledCounts.Max();
            var result = new List<int>();
            for (int srv = 0; srv < k; srv++) {
                if (handledCounts[srv] == peakTraffic) {
                    result.Add(srv);
                }
            }

            return result;
        }
    }
}
