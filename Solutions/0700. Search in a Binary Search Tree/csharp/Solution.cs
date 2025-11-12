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
        public TreeNode SearchBST(TreeNode root, int val) {
            while (root != null)
            {
                if (root.val == val) return root;
                else if (root.val < val) root = root.right;
                else root = root.left;
            }
            return root;
        }
    }
}
