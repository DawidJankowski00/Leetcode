using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution 
    {
        public int AssignEdgeWeights(int[][] edges) 
        {
            long mod = 1_000_000_007;
            var tree = new Dictionary<int, List<int>>();

            // Budowanie grafu
            foreach (var edge in edges) 
            {
                int u = edge[0];
                int v = edge[1];

                if (!tree.ContainsKey(u)) tree[u] = new List<int>();
                if (!tree.ContainsKey(v)) tree[v] = new List<int>();

                tree[u].Add(v);
                tree[v].Add(u);
            }

            int depth = Dfs(tree, 1, -1);

            int exponent = Math.Max(0, depth - 2); 


            BigInteger result = BigInteger.ModPow(2, exponent, mod);

            return (int)result;
        }

        private int Dfs(Dictionary<int, List<int>> tree, int curr, int parent) 
        {
            int maxChildDepth = 0;


            if (!tree.ContainsKey(curr)) return 1;

            foreach (int v in tree[curr]) 
            {
                if (v == parent) 
                    continue;

                int childDepth = Dfs(tree, v, curr);
                if (childDepth > maxChildDepth) 
                {
                    maxChildDepth = childDepth;
                }
            }

            return 1 + maxChildDepth;
        }
    }
}
