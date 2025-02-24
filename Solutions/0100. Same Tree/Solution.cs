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
        public bool IsSameTree(TreeNode p, TreeNode q) {
            if (q == null && p == null)
                return true;
            if (q == null || p == null || p.val != q.val)
                return false;
            return IsSameTree(p.left, q.left) && IsSameTree(p.right, q.right);
            
        }
    }
}
