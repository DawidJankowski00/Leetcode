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
        public bool IsSymmetric(TreeNode root)
        {
            bool helper(TreeNode left, TreeNode right)
            {
                if (left == null && right == null) return true;
                if (left == null || right == null) return false;
                if (left.val != right.val) return false;

                return helper(left.left, right.right) && helper(left.right, right.left);
            }
            return helper(root.left, root.right);
        }
    }
}
