using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection.Metadata.Ecma335;
using System.Runtime.CompilerServices;
using System.Text;
using System.Threading.Tasks;
using System.Xml;

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
        public int PathSum(TreeNode root, int targetSum) {
            Dictionary<long, int> acc = new Dictionary<long, int>();
            acc[0] = 1;
            int dfs(TreeNode node, long curr)
            {
                if (node == null) return 0;
                curr += node.val;
                int ct = 0;
                if (acc.ContainsKey(curr - targetSum)) ct += acc[curr - targetSum];

                if (acc.ContainsKey(curr)) acc[curr]++;
                else acc[curr] = 1;

                ct += dfs(node.left, curr) + dfs(node.right, curr);
                acc[curr]--;
                return ct;
            }
            return dfs(root, 0);
        }
    }
}
