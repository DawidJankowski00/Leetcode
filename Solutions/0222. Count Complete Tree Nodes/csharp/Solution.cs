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
        public int CountNodes(TreeNode root)
        {
            if (root == null) return 0;

            int DLeft(TreeNode node)
            {
                int tmp = 0;
                while(node != null)
                {
                    tmp++;
                    node = node.left;
                }
                return tmp;
            }
            int DRight(TreeNode node)
            {
                int tmp = 0;
                while (node != null)
                {
                    tmp++;
                    node = node.right;
                }
                return tmp;
            }

            int l = DLeft(root);
            int r = DRight(root);
            if (l == r) return (1 << l) - 1;
            return CountNodes(root.left) + 1 + CountNodes(root.right);
        }
    }
}
