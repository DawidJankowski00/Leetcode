using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Node {
        public int val;
        public IList<Node> neighbors;

        public Node() {
            val = 0;
            neighbors = new List<Node>();
        }

        public Node(int _val) {
            val = _val;
            neighbors = new List<Node>();
        }

        public Node(int _val, List<Node> _neighbors) {
            val = _val;
            neighbors = _neighbors;
        }
    }
    public class Solution {
        public Node CloneGraph(Node node)
        {
            if (node == null) return null;

            Dictionary<int, Node> visited = new Dictionary<int, Node>();
            Dictionary<int, Node> New_nodes = new Dictionary<int, Node>();
            void dfs(Node n)
            {
                if (visited.ContainsKey(n.val)) return;

                visited.Add(n.val, n);
                New_nodes.Add(n.val, new Node(n.val));
                foreach (Node item in n.neighbors)
                {
                    dfs(item);
                }
            }
            dfs(node);

            foreach (int v in visited.Keys)
            {
                foreach (Node n in visited[v].neighbors)
                {
                    New_nodes[v].neighbors.Add(New_nodes[n.val]);
                }
            }
            return New_nodes[1];


        }
    }
}
