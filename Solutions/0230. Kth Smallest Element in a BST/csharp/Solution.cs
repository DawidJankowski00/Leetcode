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
        public int KthSmallest(TreeNode root, int k)
        {
            int curr = 0;
            int dfs(TreeNode node)
            {
                int t = -1;

                if (node.left != null)
                {
                    t = dfs(node.left);
                    if (t != -1) return t;
                }
                curr++;
                if (curr == k) return node.val;
                if (node.right != null)
                {
                    t = dfs(node.right);
                    if (t != -1) return t;
                }
                return t;
            }
            return dfs(root);
        }
    }
}
