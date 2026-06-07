using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class TreeNode
    {
        public int val;
        public TreeNode left;
        public TreeNode right;
        public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null)
        {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public class Solution {
        public TreeNode CreateBinaryTree(int[][] descriptions) {
            HashSet<int> parents = new HashSet<int>();
            Dictionary<int, TreeNode> nodes = new Dictionary<int, TreeNode>();
            foreach (var d in descriptions) {
                int parent = d[0], child = d[1], isLeft = d[2];
                
                if (!nodes.ContainsKey(parent)) {
                    parents.Add(parent);
                    nodes[parent] = new TreeNode(parent);
                }
                if (!nodes.ContainsKey(child)) {
                    nodes[child] = new TreeNode(child);
                }
                if (isLeft == 1) {
                    nodes[parent].left = nodes[child];
                } else {
                    nodes[parent].right = nodes[child];
                }
                parents.Remove(child);
            }
            return nodes[parents.First()];
        }
    }
}
