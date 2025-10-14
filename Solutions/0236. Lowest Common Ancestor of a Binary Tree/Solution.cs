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
        public TreeNode LowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q)
        {
            if (root == null || root.val == p.val || root.val == q.val) return root;

            TreeNode l = LowestCommonAncestor(root.left, p, q);
            TreeNode r = LowestCommonAncestor(root.right, p, q);
            if (l != null && r != null) return root;

            return l != null && r != null ? root : l ?? r;
        }
    }
}
