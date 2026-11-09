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
        public TreeNode ConstructFromPrePost(int[] preorder, int[] postorder)
        {
            return Helper(new List<int>(preorder), new List<int>(postorder));
        }

        private TreeNode Helper(List<int> pre, List<int> post)
        {
            if (pre.Count == 0)
            {
                return null;
            }
            if (pre.Count == 1)
            {
                post.RemoveAt(post.Count - 1);
                return new TreeNode(pre[0]);
            }

            TreeNode node = new TreeNode(post[post.Count - 1]);
            post.RemoveAt(post.Count - 1);

            int ind = pre.IndexOf(post[post.Count - 1]);

            node.right = Helper(pre.GetRange(ind, pre.Count - ind), post);
            node.left = Helper(pre.GetRange(1, ind - 1), post);

            return node;
        }
    }
}
