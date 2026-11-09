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
        public int MaxPathSum(TreeNode root)
        {
            int result = -1001;

            int dfs(TreeNode node)
            {
                if (node == null) return 0;

                int tmp1 = dfs(node.left);
                int tmp2 = dfs(node.right);

                result = Math.Max(result, node.val + tmp1 + tmp2);

                if (tmp1 + node.val > 0 || tmp2 + node.val > 0) return Math.Max(tmp1, tmp2) + node.val;
                return 0;
            }

            dfs(root);
            return result;
        }
    }
}
