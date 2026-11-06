using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public int[] CountServers(int n, int[][] logs, int x, int[] queries) {
            Array.Sort(logs, (a, b) => a[1].CompareTo(b[1]));
            int totalEvents = logs.Length;

            int[] sortedQ = Enumerable.Range(0, queries.Length).ToArray();
            Array.Sort(sortedQ, (a, b) => queries[a].CompareTo(queries[b]));

            int[] serverHits = new int[n + 1];
            int uniqueActive = 0;
            int wStart = 0;
            int wEnd = 0;

            int[] res = new int[queries.Length];

            foreach (int qIdx in sortedQ) {
                int tEnd = queries[qIdx];
                int tStart = tEnd - x;

                while (wEnd < totalEvents && logs[wEnd][1] <= tEnd) {
                    int sId = logs[wEnd][0];
                    if (serverHits[sId] == 0) {
                        uniqueActive++;
                    }
                    serverHits[sId]++;
                    wEnd++;
                }

                while (wStart < wEnd && logs[wStart][1] < tStart) {
                    int sId = logs[wStart][0];
                    serverHits[sId]--;
                    if (serverHits[sId] == 0) {
                        uniqueActive--;
                    }
                    wStart++;
                }

                res[qIdx] = n - uniqueActive;
            }

            return res;
        }
    }
}
