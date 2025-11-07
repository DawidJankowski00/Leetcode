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
        public bool LeafSimilar(TreeNode root1, TreeNode root2) {
            void dfs(TreeNode node, List<int> arr)
            {
                if (node == null) return;
                if (node.left == null && node.right == null)
                {
                    arr.Add(node.val);
                    return;
                }
                dfs(node.left, arr);
                dfs(node.right, arr);
            }
            List<int> left = new List<int>();
            List<int> right = new List<int>();
            dfs(root1, left);
            dfs(root2, right);
            if (left.Count != right.Count) return false;

            for (int i = 0; i < left.Count; i++) if (left[i] != right[i]) return false;
            return true;
        }
    }
}
