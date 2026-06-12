using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution 
    {
        private const int PrimeModulus = 1000000007;
        private int maxLogSteps;
        private List<int>[] graphAdjacencyList;
        private int[] nodeDepth;
        private int[][] ancestorTable;

        private int FastExponentiation(long baseVal, int exponent) {
            long result = 1;
            baseVal %= PrimeModulus;

            while (exponent > 0) {
                if ((exponent & 1) == 1) {
                    result = (result * baseVal) % PrimeModulus;
                }
                baseVal = (baseVal * baseVal) % PrimeModulus;
                exponent >>= 1;
            }

            return (int)result;
        }

        private void ComputeTreeProperties(int currentNode, int parentNode) {
            ancestorTable[currentNode][0] = parentNode;

            for (int power = 1; power < maxLogSteps; power++) {
                int intermediateNode = ancestorTable[currentNode][power - 1];
                ancestorTable[currentNode][power] = ancestorTable[intermediateNode][power - 1];
            }

            foreach (int neighbor in graphAdjacencyList[currentNode]) {
                if (neighbor == parentNode) 
                    continue;

                nodeDepth[neighbor] = nodeDepth[currentNode] + 1;
                ComputeTreeProperties(neighbor, currentNode);
            }
        }

        private int FindLowestCommonAncestor(int nodeA, int nodeB) {
            if (nodeDepth[nodeA] < nodeDepth[nodeB]) {
                int temp = nodeA;
                nodeA = nodeB;
                nodeB = temp;
            }

            int depthDifference = nodeDepth[nodeA] - nodeDepth[nodeB];

            for (int power = maxLogSteps - 1; power >= 0; power--) {
                if ((depthDifference & (1 << power)) != 0) {
                    nodeA = ancestorTable[nodeA][power];
                }
            }

            if (nodeA == nodeB) 
                return nodeA;

            for (int power = maxLogSteps - 1; power >= 0; power--) {
                if (ancestorTable[nodeA][power] != ancestorTable[nodeB][power]) {
                    nodeA = ancestorTable[nodeA][power];
                    nodeB = ancestorTable[nodeB][power];
                }
            }

            return ancestorTable[nodeA][0];
        }

        public int[] AssignEdgeWeights(int[][] edges, int[][] queries) {
            int totalNodes = edges.Length + 1;

            maxLogSteps = 1;
            while ((1 << maxLogSteps) <= totalNodes) {
                maxLogSteps++;
            }

            graphAdjacencyList = new List<int>[totalNodes + 1];
            for (int i = 0; i <= totalNodes; i++) {
                graphAdjacencyList[i] = new List<int>();
            }

            foreach (var edge in edges) {
                int u = edge[0];
                int v = edge[1];
                graphAdjacencyList[u].Add(v);
                graphAdjacencyList[v].Add(u);
            }

            nodeDepth = new int[totalNodes + 1];
            ancestorTable = new int[totalNodes + 1][];
            for (int i = 0; i <= totalNodes; i++) {
                ancestorTable[i] = new int[maxLogSteps];
            }

            ComputeTreeProperties(1, 0);

            int[] queryResults = new int[queries.Length];

            for (int i = 0; i < queries.Length; i++) {
                int u = queries[i][0];
                int v = queries[i][1];

                int commonAncestor = FindLowestCommonAncestor(u, v);
                int pathDistance = nodeDepth[u] + nodeDepth[v] - 2 * nodeDepth[commonAncestor];

                if (pathDistance == 0) {
                    queryResults[i] = 0;
                } else {
                    queryResults[i] = FastExponentiation(2, pathDistance - 1);
                }
            }

            return queryResults;
        }
    }
}
