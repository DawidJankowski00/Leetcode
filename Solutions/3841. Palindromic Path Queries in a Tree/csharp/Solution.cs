using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{

    public class Solution {
        public IList<bool> PalindromePath(int n, int[][] edges, string s, string[] queries) {
            List<int>[] adj = new List<int>[n];
            for (int i = 0; i < n; i++) {
                adj[i] = new List<int>();
            }

            foreach (var edge in edges) {
                int u = edge[0];
                int v = edge[1];
                adj[u].Add(v);
                adj[v].Add(u);
            }

            int[] nodeParent = new int[n];
            int[] nodeDepth = new int[n];
            int[] bfsTraversal = new int[n];
            int bfsHead = 0, bfsTail = 0;

            bfsTraversal[bfsTail++] = 0;

            while (bfsHead < bfsTail) {
                int curr = bfsTraversal[bfsHead++];
                foreach (int nxt in adj[curr]) {
                    if (nxt != nodeParent[curr]) {
                        nodeParent[nxt] = curr;
                        nodeDepth[nxt] = nodeDepth[curr] + 1;
                        bfsTraversal[bfsTail++] = nxt;
                    }
                }
            }

            int[] subtreeSz = new int[n];
            Array.Fill(subtreeSz, 1);
            int[] heavyChild = new int[n];
            Array.Fill(heavyChild, -1);

            for (int i = n - 1; i > 0; i--) {
                int curr = bfsTraversal[i];
                int p = nodeParent[curr];
                subtreeSz[p] += subtreeSz[curr];
                if (heavyChild[p] == -1 || subtreeSz[curr] > subtreeSz[heavyChild[p]]) {
                    heavyChild[p] = curr;
                }
            }

            int[] chainLeader = new int[n];
            for (int i = 0; i < n; i++) {
                chainLeader[i] = i;
            }

            int[] tin = new int[n];
            int timer = 1;

            Stack<int> dfsStack = new Stack<int>();
            dfsStack.Push(0);

            while (dfsStack.Count > 0) {
                int curr = dfsStack.Pop();
                tin[curr] = timer++;

                for (int i = adj[curr].Count - 1; i >= 0; i--) {
                    int nxt = adj[curr][i];
                    if (nxt != nodeParent[curr] && nxt != heavyChild[curr]) {
                        dfsStack.Push(nxt);
                    }
                }

                if (heavyChild[curr] != -1) {
                    chainLeader[heavyChild[curr]] = chainLeader[curr];
                    dfsStack.Push(heavyChild[curr]);
                }
            }

            int[] fenwickTree = new int[n + 2];

            void BitToggle(int idx, int val) {
                while (idx <= n) {
                    fenwickTree[idx] ^= val;
                    idx += idx & -idx;
                }
            }

            int BitPrefix(int idx) {
                int total = 0;
                while (idx > 0) {
                    total ^= fenwickTree[idx];
                    idx -= idx & -idx;
                }
                return total;
            }

            int QuerySegment(int left, int right) {
                return BitPrefix(right) ^ BitPrefix(left - 1);
            }

            int[] charMasks = new int[n];
            for (int i = 0; i < n; i++) {
                charMasks[i] = 1 << (s[i] - 'a');
                BitToggle(tin[i], charMasks[i]);
            }

            int ComputePathXor(int nodeA, int nodeB) {
                int accumulated = 0;
                while (chainLeader[nodeA] != chainLeader[nodeB]) {
                    if (nodeDepth[chainLeader[nodeA]] < nodeDepth[chainLeader[nodeB]]) {
                        int tmp = nodeA; nodeA = nodeB; nodeB = tmp;
                    }

                    accumulated ^= QuerySegment(tin[chainLeader[nodeA]], tin[nodeA]);
                    nodeA = nodeParent[chainLeader[nodeA]];
                }

                if (nodeDepth[nodeA] > nodeDepth[nodeB]) {
                    int tmp = nodeA; nodeA = nodeB; nodeB = tmp;
                }

                accumulated ^= QuerySegment(tin[nodeA], tin[nodeB]);
                return accumulated;
            }

            List<bool> results = new List<bool>();

            foreach (string rawQuery in queries) {
                string[] parts = rawQuery.Split(' ');
                if (parts[0] == "update") {
                    int targetNode = int.Parse(parts[1]);
                    int newMask = 1 << (parts[2][0] - 'a');
                    int diff = charMasks[targetNode] ^ newMask;
                    if (diff != 0) {
                        charMasks[targetNode] = newMask;
                        BitToggle(tin[targetNode], diff);
                    }
                } else {
                    int startNode = int.Parse(parts[1]);
                    int endNode = int.Parse(parts[2]);
                    int pathMask = ComputePathXor(startNode, endNode);
                    results.Add((pathMask & (pathMask - 1)) == 0);
                }
            }

            return results;
        }
    }
}
