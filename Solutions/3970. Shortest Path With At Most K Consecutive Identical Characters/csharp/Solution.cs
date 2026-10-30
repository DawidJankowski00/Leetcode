using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public int ShortestPath(int n, int[][] edges, string labels, int k) {
            if (k < 1) return -1;

            List<(int to, int weight)>[] graph = new List<(int, int)>[n];
            for (int i = 0; i < n; i++) {
                graph[i] = new List<(int, int)>();
            }

            foreach (var edge in edges) {
                graph[edge[0]].Add((edge[1], edge[2]));
            }

            int[,] minCost = new int[n, k + 1];
            for (int i = 0; i < n; i++) {
                for (int s = 0; s <= k; s++) {
                    minCost[i, s] = int.MaxValue;
                }
            }

            var pq = new PriorityQueue<(int node, int streak), int>();

            minCost[0, 1] = 0;
            pq.Enqueue((0, 1), 0);

            while (pq.Count > 0) {
                pq.TryDequeue(out var current, out int cost);
                int u = current.node;
                int streak = current.streak;

                if (u == n - 1) return cost;

                if (cost > minCost[u, streak]) continue;

                foreach (var (v, weight) in graph[u]) {
                    int nextStreak = (labels[v] == labels[u]) ? streak + 1 : 1;

                    if (nextStreak <= k) {
                        int nextCost = cost + weight;
                        if (nextCost < minCost[v, nextStreak]) {
                            minCost[v, nextStreak] = nextCost;
                            pq.Enqueue((v, nextStreak), nextCost);
                        }
                    }
                }
            }

            return -1;
        }
    }
}
