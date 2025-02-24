using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class TreeNode {
        public int val;
        public TreeNode left;
        public TreeNode right;
        public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }
    public class Solution
    {
        public int MaxDepth(TreeNode root)
        {
            if (root == null) return 0;
            int dfs(TreeNode node, int d)
            {
                if (node == null) return d;
                if (node.right == null)
                {
                    if (node.left == null)
                    {
                        return d;
                    }
                    return dfs(node.left, d + 1);
                }
                return Math.Max(dfs(node.left, d + 1), dfs(node.right, d + 1));
            }
            return dfs(root, 1);
        }
    }
}
