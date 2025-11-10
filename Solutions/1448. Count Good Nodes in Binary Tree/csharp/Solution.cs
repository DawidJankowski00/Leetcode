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
        public int GoodNodes(TreeNode root) {
            int dfs(TreeNode node, int max_value)
            {
                if (node == null) return 0;
                if (node.val >= max_value)
                {
                    max_value = node.val;
                    return 1 + dfs(node.left, max_value) + dfs(node.right, max_value);
                }
                return dfs(node.left, max_value) + dfs(node.right, max_value);
            }
            return dfs(root, root.val);
        }
    }
}
