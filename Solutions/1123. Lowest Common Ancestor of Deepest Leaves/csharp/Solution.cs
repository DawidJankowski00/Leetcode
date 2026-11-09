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

    public class Solution
    {
        public TreeNode LcaDeepestLeaves(TreeNode root)
        {
            (TreeNode, int) Helper(TreeNode node, int d)
            {
                if (node == null)
                    return (null, d);
                var a = Helper(node.left, d + 1);
                var b = Helper(node.right, d + 1);
                if (a.Item2 > b.Item2) return a;
                if (a.Item2 < b.Item2) return b;
                return (node, a.Item2);
            }
            return Helper(root, 0).Item1;
        }
    }
}
