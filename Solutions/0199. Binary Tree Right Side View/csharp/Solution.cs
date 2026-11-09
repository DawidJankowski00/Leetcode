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
        public IList<int> RightSideView(TreeNode root)
        {
            IList<int> res = new List<int>();
            Dictionary<int, int> result = new Dictionary<int, int>();
            void bfs(TreeNode node, int h)
            {
                if (node == null) return;
                if (h == res.Count) res.Add(node.val);
                else res[h] = node.val;
                bfs(node.left, h+1);
                bfs(node.right, h+1);
            }
            bfs(root, 0);
            return res;
        }
    }
}
