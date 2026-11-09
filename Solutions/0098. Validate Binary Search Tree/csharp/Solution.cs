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
        public bool IsValidBST(TreeNode root)
        {
            List<int> tmp = new List<int>();

            void dfs(TreeNode node)
            {
                if (node.left != null) dfs(node.left);
                tmp.Add(node.val);
                if (node.right != null) dfs(node.right);
            }
            dfs(root);
            int n = tmp.Count;
            for (int i = 0; i < n-1; i++)
            {
                if (tmp[i] >= tmp[i+1]) return false;
            }

            return true;
        }
    }
}
