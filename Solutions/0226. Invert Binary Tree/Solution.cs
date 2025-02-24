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
    public class Solution {
        public TreeNode InvertTree(TreeNode root) {
            if (root == null)
                return null;
            var tmp = root.left;
            root.left = InvertTree(root.right);
            root.right = InvertTree(tmp);
            return root;
        }
    }
}
